from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import asyncio
import json
import os
from pathlib import Path
import yt_dlp
from typing import Dict, Any
import uuid
import logging
from .options import convert_to_ydl_opts, get_options_by_category, YT_DLP_OPTIONS, OptionType, OptionCategory

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="yt-dlp-co2", description="Modern web interface for yt-dlp")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

HTML_FILE = Path("index.html")
active_downloads: Dict[str, Dict[str, Any]] = {}
connected_websockets = []
DOWNLOAD_DIR = Path("/app/downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

class WebSocketProgressHook:
    def __init__(self, download_id: str):
        self.download_id = download_id
        
    def __call__(self, d):
        if d['status'] == 'downloading':
            progress_data = {
                'download_id': self.download_id,
                'status': 'downloading',
                'percentage': d.get('_percent_str', '0%'),
                'speed': d.get('_speed_str', 'N/A'),
                'eta': d.get('_eta_str', 'N/A'),
                'filename': d.get('filename', 'Unknown')
            }
        elif d['status'] == 'finished':
            progress_data = {
                'download_id': self.download_id,
                'status': 'completed',
                'filename': d.get('filename', 'Unknown')
            }
        else:
            progress_data = {
                'download_id': self.download_id,
                'status': d['status'],
                'message': str(d)
            }
        
        download_id = self.download_id
        if download_id not in active_downloads:
            active_downloads[download_id] = {}
        active_downloads[download_id]['progress'] = progress_data

async def broadcast_progress(data):
    if connected_websockets:
        message = json.dumps(data)
        disconnected = []
        for websocket in connected_websockets:
            try:
                await websocket.send_text(message)
            except:
                disconnected.append(websocket)
        
        for ws in disconnected:
            connected_websockets.remove(ws)

@app.get("/", response_class=HTMLResponse)
async def home():
    return FileResponse(HTML_FILE)

@app.post("/download", response_class=HTMLResponse)
async def download_video(request: Request):
    form_data = await request.form()
    url = form_data.get("url")
    format_id = form_data.get("format_id")
    batch_file = form_data.get("batchfile")
    
    # Handle batch file upload
    if batch_file and hasattr(batch_file, 'read'):
        try:
            batch_content = await batch_file.read()
            urls = [line.strip() for line in batch_content.decode('utf-8').splitlines() if line.strip()]
            
            if not urls:
                return HTMLResponse(content="<div class='error-neon card p-3 mb-3'>Batch file contains no valid URLs</div>", status_code=400)
                
            # Process batch download
            download_id = str(uuid.uuid4())
            asyncio.create_task(perform_batch_download(download_id, urls, format_id, 
                                                     {k: v for k, v in form_data.items() if k not in ["batchfile", "format_id"] and v}))
            
            html_response = f'''<div id="download-{download_id}" class="card p-4 mb-4 relative">
                <button onclick="this.parentElement.remove()" class="close-btn absolute top-2 right-2 text-gray-400 hover:text-white opacity-0 transition-opacity">
                    <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                    </svg>
                </button>
                <div class="flex items-center">
                    <svg class="animate-spin h-4 w-4 mr-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    <span>Batch download started: {len(urls)} URLs</span>
                </div>
                <div id="progress-{download_id}" class="mt-2 text-sm">
                    Processing batch file...
                </div>
            </div>'''
            return HTMLResponse(content=html_response)
            
        except Exception as e:
            return HTMLResponse(content=f"<div class='error-neon card p-3 mb-3'>Batch file error: {str(e)}</div>", status_code=400)
    
    if not url:
        return HTMLResponse(content="<div class='error-neon card p-3 mb-3'>URL is required</div>", status_code=400)
    
    # Convert form data to options dict
    options_dict = {}
    for key, value in form_data.items():
        if key not in ["url", "format_id"] and value:
            # Handle multi-select values (comma-separated)
            if "," in str(value):
                options_dict[key] = [v.strip() for v in str(value).split(",")]
            else:
                options_dict[key] = value
    
    download_id = str(uuid.uuid4())
    
    try:
        logger.info(f"Creating download task for {download_id}")
        task = asyncio.create_task(perform_download(download_id, url, format_id, options_dict))
        logger.info(f"Download task created successfully for {download_id}")
    except Exception as e:
        logger.error(f"Failed to create download task: {e}")
    safe_url = str(url).replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    
    # Show options count if any advanced options are set
    options_count = len([k for k, v in options_dict.items() if v])
    options_text = f" ({options_count} options)" if options_count > 0 else ""
    
    html_response = f'''<div id="download-{download_id}" class="card p-4 mb-4 relative">
    <button onclick="this.parentElement.remove()" class="close-btn absolute top-2 right-2 text-gray-400 hover:text-white opacity-0 transition-opacity">
        <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
    </button>
    <div class="flex items-center">
        <svg class="animate-spin h-4 w-4 mr-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        <span>Download started{options_text}: {safe_url}</span>
    </div>
    <div id="progress-{download_id}" class="mt-2 text-sm">
        Initializing...
    </div>
</div>'''
    
    return HTMLResponse(content=html_response)

def get_quality_string(format_info):
    """Generate human-readable quality string like the UI formats endpoint"""
    if format_info.get('height'):
        return f"{format_info['height']}p"
    elif format_info.get('abr'):
        return f"{format_info['abr']}kbps"
    else:
        return "unknown"

async def perform_download(download_id: str, url: str, format_id: str = None, options_dict: Dict[str, Any] = None):
    try:
        # Extract video info once for all checks
        info_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        info = None
        expected_path = None
        
        try:
            # First get video info to generate human-readable filename
            info_opts = {
                'quiet': True,
                'no_warnings': True,
            }
            
            # Add format if specified
            if format_id:
                info_opts['format'] = format_id
                
            # Convert and merge user options
            if options_dict:
                user_opts = convert_to_ydl_opts(options_dict)
                info_opts.update(user_opts)
            
            with yt_dlp.YoutubeDL(info_opts) as ydl:
                info = await asyncio.get_event_loop().run_in_executor(None, ydl.extract_info, url, False)
                
                # Find the selected format to get quality info
                selected_format = None
                if format_id and 'formats' in info:
                    for f in info['formats']:
                        if f['format_id'] == format_id:
                            selected_format = f
                            break
                
                # Generate quality string like the UI does
                if selected_format:
                    quality_str = get_quality_string(selected_format)
                    # Create filename with readable quality
                    filename = f"{info.get('title', 'Unknown')} [{quality_str}].{selected_format.get('ext', 'webm')}"
                else:
                    # Fallback to format_id if we can't find the format
                    ext = info.get('ext', 'webm')
                    filename = f"{info.get('title', 'Unknown')} [{format_id or 'default'}].{ext}"
                
                expected_path = DOWNLOAD_DIR / filename
                
            # Only check if the exact expected file exists - no fuzzy matching
            file_found = None
            if expected_path.exists():
                file_found = expected_path
            
            if file_found:
                
                # Create the entry in active_downloads and mark as skipped
                active_downloads[download_id] = {
                    'url': url,
                    'status': 'skipped',
                    'format_id': None,
                    'options': {}
                }
                
                skip_data = {
                    'download_id': download_id,
                    'status': 'completed',
                    'message': f'Already downloaded',
                    'filename': file_found.name
                }
                await broadcast_progress(skip_data)
                logger.info(f"Detected duplicate download {download_id}: {file_found.name}")
                return
                    
        except Exception as e:
            # If we can't check, proceed with download
            logger.warning(f"Could not check for existing files: {str(e)}")
        
        # Use the same human-readable filename for the actual download
        human_readable_template = str(expected_path) if expected_path else str(DOWNLOAD_DIR / '%(title)s [%(format_id)s].%(ext)s')
        
        # Base options
        ydl_opts = {
            'outtmpl': human_readable_template,
            'progress_hooks': [WebSocketProgressHook(download_id)],
            'no_overwrites': True,  # This will help us detect duplicates
        }
        
        # Add format if specified
        if format_id:
            ydl_opts['format'] = format_id
            
        # Convert and merge user options
        if options_dict:
            user_opts = convert_to_ydl_opts(options_dict)
            ydl_opts.update(user_opts)
            logger.info(f"Download {download_id} using options: {list(user_opts.keys())}")
            
        active_downloads[download_id] = {
            'url': url,
            'status': 'downloading',
            'format_id': format_id,
            'options': options_dict or {}
        }
        
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                result = await asyncio.get_event_loop().run_in_executor(None, ydl.download, [url])
                        
            except Exception as download_error:
                logger.error(f"Download failed for {download_id}: {download_error}")
                raise download_error
            
        active_downloads[download_id]['status'] = 'completed'
        
    except Exception as e:
        logger.error(f"Download error for {download_id}: {e}")
        # Ensure the download entry exists before setting error status
        if download_id not in active_downloads:
            active_downloads[download_id] = {'url': url, 'status': 'error', 'format_id': format_id, 'options': options_dict or {}}
        else:
            active_downloads[download_id]['status'] = 'error'
        active_downloads[download_id]['error'] = str(e)
        
        error_data = {
            'download_id': download_id,
            'status': 'error',
            'error': str(e)
        }
        await broadcast_progress(error_data)

async def perform_batch_download(download_id: str, urls: list, format_id: str = None, options_dict: Dict[str, Any] = None):
    """Process batch download of multiple URLs"""
    try:
        total_urls = len(urls)
        completed = 0
        
        for i, url in enumerate(urls, 1):
            try:
                # Base options
                ydl_opts = {
                    'outtmpl': str(DOWNLOAD_DIR / '%(title)s [%(format_id)s].%(ext)s'),
                    'progress_hooks': [WebSocketProgressHook(download_id)],
                }
                
                # Add format if specified
                if format_id:
                    ydl_opts['format'] = format_id
                    
                # Convert and merge user options
                if options_dict:
                    user_opts = convert_to_ydl_opts(options_dict)
                    ydl_opts.update(user_opts)
                    
                # Update progress
                progress_data = {
                    'download_id': download_id,
                    'status': 'downloading',
                    'message': f'Processing URL {i}/{total_urls}: {url[:50]}...',
                    'batch_progress': f'{completed}/{total_urls}'
                }
                await broadcast_progress(progress_data)
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    await asyncio.get_event_loop().run_in_executor(None, ydl.download, [url])
                    
                completed += 1
                logger.info(f"Batch download {download_id}: completed {url}")
                
            except Exception as e:
                logger.error(f"Batch download {download_id}: error with {url}: {e}")
                error_data = {
                    'download_id': download_id,
                    'status': 'warning',
                    'message': f'Failed URL {i}/{total_urls}: {str(e)[:100]}'
                }
                await broadcast_progress(error_data)
                continue
                
        # Final completion status
        active_downloads[download_id]['status'] = 'completed'
        completion_data = {
            'download_id': download_id,
            'status': 'completed',
            'message': f'Batch completed: {completed}/{total_urls} successful'
        }
        await broadcast_progress(completion_data)
        
    except Exception as e:
        logger.error(f"Batch download error for {download_id}: {e}")
        # Ensure the download entry exists before setting error status
        if download_id not in active_downloads:
            active_downloads[download_id] = {'url': 'batch', 'status': 'error', 'format_id': format_id, 'options': options_dict or {}}
        else:
            active_downloads[download_id]['status'] = 'error'
        active_downloads[download_id]['error'] = str(e)
        
        error_data = {
            'download_id': download_id,
            'status': 'error',
            'error': str(e)
        }
        await broadcast_progress(error_data)

@app.get("/formats/{url:path}")
async def get_formats(url: str):
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            formats = []
            if 'formats' in info:
                for f in info['formats']:
                    if f.get('height'):
                        quality = f"{f['height']}p"
                    elif f.get('abr'):
                        quality = f"{f['abr']}kbps"
                    else:
                        quality = "Unknown"
                        
                    formats.append({
                        'format_id': f['format_id'],
                        'ext': f.get('ext', 'unknown'),
                        'quality': quality,
                        'filesize': f.get('filesize'),
                        'vcodec': f.get('vcodec', 'none'),
                        'acodec': f.get('acodec', 'none')
                    })
            
            return {
                'title': info.get('title', 'Unknown'),
                'duration': info.get('duration'),
                'formats': formats[:20]
            }
            
    except Exception as e:
        logger.error(f"Format extraction error: {e}")
        return {'error': str(e)}

@app.get("/info/{url:path}")
async def get_video_info(url: str, info_type: str = "basic"):
    """Extract video information without downloading"""
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            if info_type == "formats":
                formats = []
                if 'formats' in info:
                    for f in info['formats']:
                        formats.append({
                            'format_id': f['format_id'],
                            'ext': f.get('ext', 'unknown'),
                            'quality': f"{f['height']}p" if f.get('height') else f"{f.get('abr', 'unknown')}kbps",
                            'filesize': f.get('filesize'),
                            'vcodec': f.get('vcodec', 'none'),
                            'acodec': f.get('acodec', 'none'),
                            'fps': f.get('fps'),
                            'tbr': f.get('tbr')
                        })
                return {'formats': formats}
                
            elif info_type == "subtitles":
                subs = info.get('subtitles', {})
                auto_subs = info.get('automatic_captions', {})
                return {
                    'subtitles': subs,
                    'automatic_captions': auto_subs,
                    'available_languages': list(set(list(subs.keys()) + list(auto_subs.keys())))
                }
                
            elif info_type == "thumbnails":
                thumbnails = info.get('thumbnails', [])
                return {
                    'thumbnails': [
                        {
                            'id': t.get('id'),
                            'url': t.get('url'),
                            'width': t.get('width'),
                            'height': t.get('height')
                        } for t in thumbnails
                    ]
                }
                
            else:  # basic info
                return {
                    'title': info.get('title', 'Unknown'),
                    'uploader': info.get('uploader', 'Unknown'),
                    'duration': info.get('duration'),
                    'description': info.get('description', ''),
                    'view_count': info.get('view_count'),
                    'upload_date': info.get('upload_date'),
                    'webpage_url': info.get('webpage_url'),
                    'thumbnail': info.get('thumbnail'),
                    'tags': info.get('tags', []),
                    'categories': info.get('categories', [])
                }
                
    except Exception as e:
        logger.error(f"Info extraction error: {e}")
        return {'error': str(e)}

@app.get("/search/{query}")
async def search_videos(query: str, search_type: str = "ytsearch", max_results: int = 10):
    """Search for videos using yt-dlp search functionality"""
    try:
        search_query = f"{search_type}{max_results}:{query}"
        
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True  # Only get basic info, don't extract full details
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(search_query, download=False)
            
            results = []
            if info and 'entries' in info:
                for entry in info['entries']:
                    if entry:
                        results.append({
                            'title': entry.get('title', 'Unknown'),
                            'url': entry.get('url', ''),
                            'id': entry.get('id', ''),
                            'duration': entry.get('duration'),
                            'uploader': entry.get('uploader', 'Unknown'),
                            'view_count': entry.get('view_count'),
                            'description': entry.get('description', '')
                        })
                        
            return {
                'query': query,
                'results': results,
                'total': len(results)
            }
            
    except Exception as e:
        logger.error(f"Search error: {e}")
        return {'error': str(e)}

@app.websocket("/ws/progress")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_websockets.append(websocket)
    
    try:
        while True:
            for download_id, data in active_downloads.items():
                if 'progress' in data:
                    progress_data = data['progress']
                    await websocket.send_text(json.dumps(progress_data))
                    del data['progress']
            await asyncio.sleep(0.5)
    except WebSocketDisconnect:
        if websocket in connected_websockets:
            connected_websockets.remove(websocket)

@app.get("/downloads")
async def list_downloads():
    return active_downloads

@app.get("/options")
async def get_options():
    """Return all available yt-dlp options organized by category"""
    return {
        "categories": get_options_by_category(),
        "options": YT_DLP_OPTIONS
    }

@app.post("/save-config")
async def save_configuration(request: Request):
    """Save current configuration to file"""
    try:
        form_data = await request.form()
        config_name = form_data.get("config_name", "default")
        
        # Convert form data to config dict
        config_dict = {}
        for key, value in form_data.items():
            if key != "config_name" and value:
                config_dict[key] = value
                
        # Save to config directory
        config_dir = Path("/app/configs")
        config_dir.mkdir(exist_ok=True)
        config_file = config_dir / f"{config_name}.json"
        
        import json
        with open(config_file, 'w') as f:
            json.dump(config_dict, f, indent=2)
            
        return {"message": f"Configuration saved as {config_name}.json", "success": True}
        
    except Exception as e:
        logger.error(f"Config save error: {e}")
        return {"error": str(e), "success": False}

@app.get("/load-config/{config_name}")
async def load_configuration(config_name: str):
    """Load configuration from file"""
    try:
        config_dir = Path("/app/configs")
        config_file = config_dir / f"{config_name}.json"
        
        if not config_file.exists():
            return {"error": f"Configuration {config_name} not found", "success": False}
            
        import json
        with open(config_file, 'r') as f:
            config_dict = json.load(f)
            
        return {"config": config_dict, "success": True}
        
    except Exception as e:
        logger.error(f"Config load error: {e}")
        return {"error": str(e), "success": False}

@app.get("/list-configs")
async def list_configurations():
    """List all saved configurations"""
    try:
        config_dir = Path("/app/configs")
        if not config_dir.exists():
            return {"configs": [], "success": True}
            
        configs = []
        for config_file in config_dir.glob("*.json"):
            configs.append({
                "name": config_file.stem,
                "modified": config_file.stat().st_mtime
            })
            
        return {"configs": sorted(configs, key=lambda x: x["modified"], reverse=True), "success": True}
        
    except Exception as e:
        logger.error(f"Config list error: {e}")
        return {"error": str(e), "success": False}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)