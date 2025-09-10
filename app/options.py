"""
Comprehensive yt-dlp options mapping for web interface
Based on yt-dlp command line options and YoutubeDL parameters
"""

from typing import Dict, List, Any, Union
from enum import Enum

class OptionType(Enum):
    BOOLEAN = "boolean"
    STRING = "string"
    NUMBER = "number"
    SELECT = "select"
    MULTI_SELECT = "multi_select"
    FILE_PATH = "file_path"
    URL = "url"
    REGEX = "regex"
    TEMPLATE = "template"

class OptionCategory(Enum):
    GENERAL = "General Options"
    NETWORK = "Network Options" 
    VIDEO_SELECTION = "Video Selection"
    DOWNLOAD = "Download Options"
    FILESYSTEM = "Filesystem Options"
    THUMBNAIL = "Thumbnail Options"
    VERBOSITY = "Verbosity & Simulation Options"
    WORKAROUNDS = "Workarounds"
    VIDEO_FORMAT = "Video Format Options"
    SUBTITLE = "Subtitle Options"
    AUTHENTICATION = "Authentication Options"
    POST_PROCESSING = "Post-Processing Options"
    SPONSORBLOCK = "SponsorBlock Options"
    EXTRACTOR = "Extractor Options"
    GEO_RESTRICTION = "Geo Restriction"
    COOKIES = "Cookies & Headers"

# Comprehensive yt-dlp options mapping
YT_DLP_OPTIONS = {
    # General Options
    "batchfile": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.FILE_PATH,
        "cli": ["-a", "--batch-file"],
        "description": "File containing URLs to download (one per line)",
        "default": None
    },
    "default_search": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.SELECT,
        "cli": ["--default-search"],
        "description": "Use this prefix for unqualified URLs",
        "options": ["auto", "auto_warning", "error", "fixup_error", "ytsearch", "gvsearch"],
        "default": "fixup_error"
    },
    "ignore_config": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.BOOLEAN,
        "cli": ["--ignore-config"],
        "description": "Don't load any configuration files",
        "default": False
    },
    "flat_playlist": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.BOOLEAN,
        "cli": ["--flat-playlist"],
        "description": "Do not extract playlist entries",
        "default": False
    },
    "live_from_start": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.BOOLEAN,
        "cli": ["--live-from-start"],
        "description": "Download livestreams from the start",
        "default": False
    },
    "wait_for_video": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.STRING,
        "cli": ["--wait-for-video"],
        "description": "Wait for scheduled streams (MIN[-MAX] seconds)",
        "default": None,
        "placeholder": "300 or 60-600"
    },
    "color": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.SELECT,
        "cli": ["--color"],
        "description": "Whether to emit color codes in output",
        "options": ["always", "auto", "never", "no_color"],
        "default": "auto"
    },
    "compat_opts": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.STRING,
        "cli": ["--compat-options"],
        "description": "Options for compatibility with youtube-dl",
        "default": None,
        "placeholder": "youtube-dl-compatibility"
    },
    "ignore_errors": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.BOOLEAN,
        "cli": ["-i", "--ignore-errors"],
        "description": "Continue downloading if extraction errors occur",
        "default": False
    },
    "abort_on_error": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.BOOLEAN,
        "cli": ["--abort-on-error"],
        "description": "Abort downloading of remaining videos if extraction errors occur",
        "default": False
    },
    "extract_flat": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.SELECT,
        "cli": ["--flat-playlist"],
        "description": "Do not extract videos in playlists, only metadata",
        "options": [None, True, False, "in_playlist", "discard_in_playlist"],
        "default": None
    },
    "mark_watched": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.BOOLEAN,
        "cli": ["--mark-watched"],
        "description": "Mark videos as watched",
        "default": False
    },
    "no_mark_watched": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-mark-watched"],
        "description": "Do not mark videos as watched",
        "default": False
    },
    
    # Video Selection
    "playliststart": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.NUMBER,
        "cli": ["--playlist-start"],
        "description": "Playlist item to start downloading from",
        "default": 1,
        "min": 1
    },
    "playlistend": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.NUMBER,
        "cli": ["--playlist-end"],
        "description": "Playlist item to end downloading at",
        "default": None,
        "min": 1
    },
    "playlist_items": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--playlist-items"],
        "description": "Specify playlist items to download (e.g. 1,3-5,7)",
        "default": None,
        "placeholder": "1,3-5,7"
    },
    "matchtitle": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.REGEX,
        "cli": ["--match-title"],
        "description": "Download only videos matching title regex",
        "default": None
    },
    "rejecttitle": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.REGEX,
        "cli": ["--reject-title"],
        "description": "Skip videos matching title regex",
        "default": None
    },
    "min_filesize": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--min-filesize"],
        "description": "Minimum file size (e.g. 50k or 44.6m)",
        "default": None,
        "placeholder": "50k or 44.6m"
    },
    "max_filesize": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--max-filesize"],
        "description": "Maximum file size (e.g. 50k or 44.6m)",
        "default": None,
        "placeholder": "50k or 44.6m"
    },
    "date": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--date"],
        "description": "Download only videos uploaded on this date (YYYYMMDD)",
        "default": None,
        "placeholder": "20240101"
    },
    "datebefore": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--datebefore"],
        "description": "Download only videos uploaded before this date (YYYYMMDD)",
        "default": None,
        "placeholder": "20240101"
    },
    "dateafter": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--dateafter"],
        "description": "Download only videos uploaded after this date (YYYYMMDD)",
        "default": None,
        "placeholder": "20240101"
    },
    "min_views": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.NUMBER,
        "cli": ["--min-views"],
        "description": "Minimum view count for downloaded videos",
        "default": None,
        "min": 0
    },
    "max_views": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.NUMBER,
        "cli": ["--max-views"],
        "description": "Maximum view count for downloaded videos",
        "default": None,
        "min": 0
    },
    
    # Download Options
    "concurrent_fragments": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.NUMBER,
        "cli": ["-N", "--concurrent-fragments"],
        "description": "Number of fragments to download simultaneously",
        "default": 1,
        "min": 1,
        "max": 32
    },
    "limit_rate": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["-r", "--limit-rate"],
        "description": "Maximum download rate (e.g. 50K or 4.2M)",
        "default": None,
        "placeholder": "50K or 4.2M"
    },
    "throttled_rate": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--throttled-rate"],
        "description": "Minimum download rate below which throttling is assumed",
        "default": None,
        "placeholder": "100K"
    },
    "retries": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.NUMBER,
        "cli": ["-R", "--retries"],
        "description": "Number of download retries",
        "default": 10,
        "min": 0
    },
    "file_access_retries": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.NUMBER,
        "cli": ["--file-access-retries"],
        "description": "Number of file access retries",
        "default": 3,
        "min": 0
    },
    "fragment_retries": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.NUMBER,
        "cli": ["--fragment-retries"],
        "description": "Number of fragment download retries",
        "default": 10,
        "min": 0
    },
    "retry_sleep_linear": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.NUMBER,
        "cli": ["--retry-sleep"],
        "description": "Time to sleep between retries (linear component)",
        "default": None,
        "min": 0
    },
    "skip_unavailable_fragments": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--skip-unavailable-fragments"],
        "description": "Skip unavailable fragments for live streams",
        "default": True
    },
    "keep_fragments": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--keep-fragments"],
        "description": "Keep downloaded fragments after successful download",
        "default": False
    },
    
    # Network Options
    "proxy": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.URL,
        "cli": ["--proxy"],
        "description": "Use specified HTTP/HTTPS/SOCKS proxy",
        "default": None,
        "placeholder": "http://proxy.example.com:8080"
    },
    "socket_timeout": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.NUMBER,
        "cli": ["--socket-timeout"],
        "description": "Time to wait before giving up in seconds",
        "default": None,
        "min": 0
    },
    "source_address": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.STRING,
        "cli": ["--source-address"],
        "description": "Client-side IP address to bind to",
        "default": None,
        "placeholder": "192.168.1.100"
    },
    "force_ipv4": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.BOOLEAN,
        "cli": ["-4", "--force-ipv4"],
        "description": "Make all connections via IPv4",
        "default": False
    },
    "force_ipv6": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.BOOLEAN,
        "cli": ["-6", "--force-ipv6"],
        "description": "Make all connections via IPv6",
        "default": False
    },
    
    # Filesystem Options
    "outtmpl": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.TEMPLATE,
        "cli": ["-o", "--output"],
        "description": "Output filename template",
        "default": "%(title)s.%(ext)s",
        "placeholder": "%(uploader)s/%(title)s.%(ext)s"
    },
    "outtmpl_na_placeholder": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.STRING,
        "cli": ["--output-na-placeholder"],
        "description": "Placeholder for unavailable template fields",
        "default": "NA"
    },
    "restrict_filenames": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--restrict-filenames"],
        "description": "Restrict filenames to ASCII characters",
        "default": False
    },
    "no_restrict_filenames": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-restrict-filenames"],
        "description": "Allow Unicode characters in filenames",
        "default": True
    },
    "windows_filenames": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--windows-filenames"],
        "description": "Force Windows-compatible filenames",
        "default": False
    },
    "trim_filenames": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.NUMBER,
        "cli": ["--trim-filenames"],
        "description": "Limit filename length (excluding extension)",
        "default": None,
        "min": 1
    },
    "no_overwrites": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["-w", "--no-overwrites"],
        "description": "Do not overwrite existing files",
        "default": False
    },
    "continue_dl": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["-c", "--continue"],
        "description": "Resume partially downloaded files",
        "default": True
    },
    "no_continue": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-continue"],
        "description": "Do not resume partially downloaded files",
        "default": False
    },
    "no_part": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-part"],
        "description": "Do not use .part files",
        "default": False
    },
    "no_mtime": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-mtime"],
        "description": "Do not use Last-modified header to set file modification time",
        "default": False
    },
    "write_description": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-description"],
        "description": "Write video description to .description file",
        "default": False
    },
    "write_info_json": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-info-json"],
        "description": "Write video metadata to .info.json file",
        "default": False
    },
    "write_annotations": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-annotations"],
        "description": "Write video annotations to .annotations.xml file",
        "default": False
    },
    
    # Thumbnail Options
    "write_thumbnail": {
        "category": OptionCategory.THUMBNAIL,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-thumbnail"],
        "description": "Write thumbnail image to disk",
        "default": False
    },
    "write_all_thumbnails": {
        "category": OptionCategory.THUMBNAIL,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-all-thumbnails"],
        "description": "Write all thumbnail image formats to disk",
        "default": False
    },
    "list_thumbnails": {
        "category": OptionCategory.THUMBNAIL,
        "type": OptionType.BOOLEAN,
        "cli": ["--list-thumbnails"],
        "description": "List available thumbnail formats and exit",
        "default": False
    },
    
    # Verbosity Options
    "quiet": {
        "category": OptionCategory.VERBOSITY,
        "type": OptionType.BOOLEAN,
        "cli": ["-q", "--quiet"],
        "description": "Activate quiet mode",
        "default": False
    },
    "no_warnings": {
        "category": OptionCategory.VERBOSITY,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-warnings"],
        "description": "Ignore warnings",
        "default": False
    },
    "simulate": {
        "category": OptionCategory.VERBOSITY,
        "type": OptionType.BOOLEAN,
        "cli": ["-s", "--simulate"],
        "description": "Do not download video",
        "default": False
    },
    "skip_download": {
        "category": OptionCategory.VERBOSITY,
        "type": OptionType.BOOLEAN,
        "cli": ["--skip-download"],
        "description": "Do not download video but write all related files",
        "default": False
    },
    "print_json": {
        "category": OptionCategory.VERBOSITY,
        "type": OptionType.BOOLEAN,
        "cli": ["-j", "--print-json"],
        "description": "Output progress info as JSON",
        "default": False
    },
    
    # Video Format Options
    "format": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.STRING,
        "cli": ["-f", "--format"],
        "description": "Video format code",
        "default": "best/bestvideo[height<=?1080]+bestaudio/best",
        "placeholder": "best[height<=480]"
    },
    "format_sort": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.STRING,
        "cli": ["-S", "--format-sort"],
        "description": "Sort formats by given field(s)",
        "default": None,
        "placeholder": "height,tbr,lang"
    },
    "format_sort_force": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--format-sort-force"],
        "description": "Force given format_sort",
        "default": False
    },
    "no_format_sort_force": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-format-sort-force"],
        "description": "Do not force given format_sort",
        "default": True
    },
    "video_multistreams": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--video-multistreams"],
        "description": "Allow multiple video streams to be merged",
        "default": False
    },
    "audio_multistreams": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--audio-multistreams"],
        "description": "Allow multiple audio streams to be merged",
        "default": False
    },
    "prefer_free_formats": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--prefer-free-formats"],
        "description": "Prefer free video formats over non-free formats",
        "default": False
    },
    "no_prefer_free_formats": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-prefer-free-formats"],
        "description": "Do not prefer free video formats",
        "default": True
    },
    "check_formats": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.SELECT,
        "cli": ["--check-formats"],
        "description": "Check if formats are actually downloadable",
        "options": [None, "selected"],
        "default": None
    },
    "check_all_formats": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--check-all-formats"],
        "description": "Check all formats for download availability",
        "default": False
    },
    "no_check_formats": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-check-formats"],
        "description": "Do not check if formats are downloadable",
        "default": True
    },
    "list_formats": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["-F", "--list-formats"],
        "description": "List available formats and exit",
        "default": False
    },
    "youtube_skip_dash_manifest": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--youtube-skip-dash-manifest"],
        "description": "Do not download DASH manifest on YouTube videos",
        "default": False
    },
    "youtube_skip_hls_manifest": {
        "category": OptionCategory.VIDEO_FORMAT,
        "type": OptionType.BOOLEAN,
        "cli": ["--youtube-skip-hls-manifest"],
        "description": "Do not download HLS manifest on YouTube videos",
        "default": False
    },
    
    # Subtitle Options
    "writesubtitles": {
        "category": OptionCategory.SUBTITLE,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-subs"],
        "description": "Write subtitle files",
        "default": False
    },
    "writeautomaticsub": {
        "category": OptionCategory.SUBTITLE,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-auto-subs"],
        "description": "Write automatically generated subtitle files",
        "default": False
    },
    "allsubtitles": {
        "category": OptionCategory.SUBTITLE,
        "type": OptionType.BOOLEAN,
        "cli": ["--all-subs"],
        "description": "Download all available subtitle files",
        "default": False
    },
    "listsubtitles": {
        "category": OptionCategory.SUBTITLE,
        "type": OptionType.BOOLEAN,
        "cli": ["--list-subs"],
        "description": "List available subtitle files and exit",
        "default": False
    },
    "subtitlesformat": {
        "category": OptionCategory.SUBTITLE,
        "type": OptionType.SELECT,
        "cli": ["--sub-format"],
        "description": "Subtitle format preference",
        "options": ["best", "srt", "ass", "vtt", "lrc"],
        "default": "best"
    },
    "subtitleslangs": {
        "category": OptionCategory.SUBTITLE,
        "type": OptionType.STRING,
        "cli": ["--sub-langs"],
        "description": "Languages of subtitles to download (comma separated)",
        "default": None,
        "placeholder": "en,es,fr"
    },
    
    # Authentication Options
    "username": {
        "category": OptionCategory.AUTHENTICATION,
        "type": OptionType.STRING,
        "cli": ["-u", "--username"],
        "description": "Login username",
        "default": None
    },
    "password": {
        "category": OptionCategory.AUTHENTICATION,
        "type": OptionType.STRING,
        "cli": ["-p", "--password"],
        "description": "Login password",
        "default": None,
        "sensitive": True
    },
    "twofactor": {
        "category": OptionCategory.AUTHENTICATION,
        "type": OptionType.STRING,
        "cli": ["-2", "--twofactor"],
        "description": "Two-factor authentication code",
        "default": None,
        "sensitive": True
    },
    "netrc": {
        "category": OptionCategory.AUTHENTICATION,
        "type": OptionType.BOOLEAN,
        "cli": ["-n", "--netrc"],
        "description": "Use .netrc authentication data",
        "default": False
    },
    "netrc_location": {
        "category": OptionCategory.AUTHENTICATION,
        "type": OptionType.FILE_PATH,
        "cli": ["--netrc-location"],
        "description": "Location of .netrc authentication data",
        "default": None
    },
    "video_password": {
        "category": OptionCategory.AUTHENTICATION,
        "type": OptionType.STRING,
        "cli": ["--video-password"],
        "description": "Video password for protected videos",
        "default": None,
        "sensitive": True
    },
    "ap_mso": {
        "category": OptionCategory.AUTHENTICATION,
        "type": OptionType.STRING,
        "cli": ["--ap-mso"],
        "description": "Adobe Pass multiple-system operator identifier",
        "default": None
    },
    "ap_username": {
        "category": OptionCategory.AUTHENTICATION,
        "type": OptionType.STRING,
        "cli": ["--ap-username"],
        "description": "Adobe Pass username",
        "default": None
    },
    "ap_password": {
        "category": OptionCategory.AUTHENTICATION,
        "type": OptionType.STRING,
        "cli": ["--ap-password"],
        "description": "Adobe Pass password",
        "default": None,
        "sensitive": True
    },
    
    # Post-Processing Options
    "extract_audio": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["-x", "--extract-audio"],
        "description": "Convert video files to audio-only files",
        "default": False
    },
    "audio_format": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.SELECT,
        "cli": ["--audio-format"],
        "description": "Audio format for converted files",
        "options": ["best", "aac", "flac", "mp3", "m4a", "opus", "vorbis", "wav", "alac"],
        "default": "best"
    },
    "audio_quality": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.SELECT,
        "cli": ["--audio-quality"],
        "description": "Audio quality for converted files",
        "options": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "default": "5"
    },
    "recode_video": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.SELECT,
        "cli": ["--recode-video"],
        "description": "Re-encode video to given format",
        "options": [None, "mp4", "flv", "ogg", "webm", "mkv", "avi"],
        "default": None
    },
    "postprocessor_args": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.STRING,
        "cli": ["--postprocessor-args"],
        "description": "Give postprocessor arguments",
        "default": None,
        "placeholder": "-vcodec libx264"
    },
    "keep_video": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["-k", "--keep-video"],
        "description": "Keep video after post-processing",
        "default": False
    },
    "no_keep_video": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-keep-video"],
        "description": "Delete video after post-processing",
        "default": True
    },
    "no_post_overwrites": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-post-overwrites"],
        "description": "Do not overwrite post-processed files",
        "default": False
    },
    "embed_subs": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["--embed-subs"],
        "description": "Embed subtitles in video",
        "default": False
    },
    "embed_thumbnail": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["--embed-thumbnail"],
        "description": "Embed thumbnail in audio/video",
        "default": False
    },
    "embed_metadata": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["--embed-metadata"],
        "description": "Embed metadata in video/audio files",
        "default": False
    },
    "embed_chapters": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["--embed-chapters"],
        "description": "Add chapter markers to audio/video",
        "default": False
    },
    "embed_info_json": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["--embed-info-json"],
        "description": "Embed info.json as attachment",
        "default": False
    },
    "parse_metadata": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.STRING,
        "cli": ["--parse-metadata"],
        "description": "Parse additional metadata from filename/path",
        "default": None,
        "placeholder": "FROM_FIELD:TO_FIELD"
    },
    "replace_in_metadata": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.STRING,
        "cli": ["--replace-in-metadata"],
        "description": "Replace text in metadata fields",
        "default": None,
        "placeholder": "FIELD REGEX REPLACE"
    },
    "xattrs": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.BOOLEAN,
        "cli": ["--xattrs"],
        "description": "Write metadata to extended attributes",
        "default": False
    },
    "fixup": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.SELECT,
        "cli": ["--fixup"],
        "description": "Automatically correct known faults in downloaded files",
        "options": ["never", "warn", "detect_or_warn", "force"],
        "default": "detect_or_warn"
    },
    "ffmpeg_location": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.FILE_PATH,
        "cli": ["--ffmpeg-location"],
        "description": "Location of ffmpeg binary",
        "default": None
    },
    "exec": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.STRING,
        "cli": ["--exec"],
        "description": "Execute command on downloaded file",
        "default": None,
        "placeholder": "echo Downloaded {}"
    },
    
    # SponsorBlock Options
    "sponsorblock_mark": {
        "category": OptionCategory.SPONSORBLOCK,
        "type": OptionType.MULTI_SELECT,
        "cli": ["--sponsorblock-mark"],
        "description": "Categories to create chapters for",
        "options": ["sponsor", "intro", "outro", "selfpromo", "preview", "filler", "interaction", "music_offtopic", "poi_highlight"],
        "default": []
    },
    "sponsorblock_remove": {
        "category": OptionCategory.SPONSORBLOCK,
        "type": OptionType.MULTI_SELECT,
        "cli": ["--sponsorblock-remove"],
        "description": "Categories to remove from video",
        "options": ["sponsor", "intro", "outro", "selfpromo", "preview", "filler", "interaction", "music_offtopic", "poi_highlight"],
        "default": []
    },
    "sponsorblock_chapter_title": {
        "category": OptionCategory.SPONSORBLOCK,
        "type": OptionType.STRING,
        "cli": ["--sponsorblock-chapter-title"],
        "description": "Template for SponsorBlock chapter titles",
        "default": "[SponsorBlock]: %(category_names)l",
        "placeholder": "[SponsorBlock]: %(category_names)l"
    },
    "no_sponsorblock": {
        "category": OptionCategory.SPONSORBLOCK,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-sponsorblock"],
        "description": "Disable SponsorBlock",
        "default": True
    },
    "sponsorblock_api": {
        "category": OptionCategory.SPONSORBLOCK,
        "type": OptionType.URL,
        "cli": ["--sponsorblock-api"],
        "description": "SponsorBlock API URL",
        "default": "https://sponsor.ajay.app",
        "placeholder": "https://sponsor.ajay.app"
    },
    
    # Extractor Options
    "extractor_args": {
        "category": OptionCategory.EXTRACTOR,
        "type": OptionType.STRING,
        "cli": ["--extractor-args"],
        "description": "Pass arguments to extractors",
        "default": None,
        "placeholder": "youtube:skip=dash"
    },
    "youtube_include_dash_manifest": {
        "category": OptionCategory.EXTRACTOR,
        "type": OptionType.BOOLEAN,
        "cli": ["--youtube-include-dash-manifest"],
        "description": "Download DASH manifest on YouTube",
        "default": True
    },
    "youtube_include_hls_manifest": {
        "category": OptionCategory.EXTRACTOR,
        "type": OptionType.BOOLEAN,
        "cli": ["--youtube-include-hls-manifest"],
        "description": "Download HLS manifest on YouTube",
        "default": True
    },
    
    # Geo Restriction
    "geo_verification_proxy": {
        "category": OptionCategory.GEO_RESTRICTION,
        "type": OptionType.URL,
        "cli": ["--geo-verification-proxy"],
        "description": "Use proxy to verify geo location",
        "default": None,
        "placeholder": "http://proxy.example.com:8080"
    },
    "geo_bypass": {
        "category": OptionCategory.GEO_RESTRICTION,
        "type": OptionType.BOOLEAN,
        "cli": ["--geo-bypass"],
        "description": "Bypass geographic restriction via fake X-Forwarded-For",
        "default": False
    },
    "no_geo_bypass": {
        "category": OptionCategory.GEO_RESTRICTION,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-geo-bypass"],
        "description": "Do not bypass geographic restriction",
        "default": True
    },
    "geo_bypass_country": {
        "category": OptionCategory.GEO_RESTRICTION,
        "type": OptionType.STRING,
        "cli": ["--geo-bypass-country"],
        "description": "Force bypass using country code",
        "default": None,
        "placeholder": "US"
    },
    "geo_bypass_ip_block": {
        "category": OptionCategory.GEO_RESTRICTION,
        "type": OptionType.STRING,
        "cli": ["--geo-bypass-ip-block"],
        "description": "Force bypass using IP block",
        "default": None,
        "placeholder": "1.2.3.4/24"
    },
    
    # Cookies & Headers Options
    "cookiefile": {
        "category": OptionCategory.COOKIES,
        "type": OptionType.FILE_PATH,
        "cli": ["--cookies"],
        "description": "File to read cookies from",
        "default": None
    },
    "cookiesfrombrowser": {
        "category": OptionCategory.COOKIES,
        "type": OptionType.STRING,
        "cli": ["--cookies-from-browser"],
        "description": "Load cookies from browser (BROWSER[+KEYRING][:PROFILE])",
        "default": None,
        "placeholder": "chrome, firefox, safari, etc."
    },
    "no_cookies": {
        "category": OptionCategory.COOKIES,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-cookies"],
        "description": "Do not read/dump cookies from/to file",
        "default": False
    },
    "user_agent": {
        "category": OptionCategory.COOKIES,
        "type": OptionType.STRING,
        "cli": ["--user-agent"],
        "description": "Specify a custom user agent",
        "default": None,
        "placeholder": "Mozilla/5.0 ..."
    },
    "referer": {
        "category": OptionCategory.COOKIES,
        "type": OptionType.URL,
        "cli": ["--referer"],
        "description": "Specify a custom referer",
        "default": None,
        "placeholder": "https://example.com"
    },
    "add_headers": {
        "category": OptionCategory.COOKIES,
        "type": OptionType.STRING,
        "cli": ["--add-headers"],
        "description": "Add custom HTTP headers (FIELD:VALUE)",
        "default": None,
        "placeholder": "Custom-Header: value"
    },
    
    # Workarounds Options  
    "encoding": {
        "category": OptionCategory.WORKAROUNDS,
        "type": OptionType.STRING,
        "cli": ["--encoding"],
        "description": "Force the specified encoding",
        "default": None,
        "placeholder": "utf-8"
    },
    "legacy_server_connect": {
        "category": OptionCategory.WORKAROUNDS,
        "type": OptionType.BOOLEAN,
        "cli": ["--legacy-server-connect"],
        "description": "Use legacy server connect method",
        "default": False
    },
    "no_check_certificates": {
        "category": OptionCategory.WORKAROUNDS,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-check-certificates"],
        "description": "Suppress HTTPS certificate validation",
        "default": False
    },
    "prefer_insecure": {
        "category": OptionCategory.WORKAROUNDS,
        "type": OptionType.BOOLEAN,
        "cli": ["--prefer-insecure"],
        "description": "Use an unencrypted connection for extractors that support it",
        "default": False
    },
    "add_ie_names": {
        "category": OptionCategory.WORKAROUNDS,
        "type": OptionType.STRING,
        "cli": ["--add-ie-names"],
        "description": "Add extractor names to filename",
        "default": None
    },
    
    # Sleep Options
    "sleep_interval": {
        "category": OptionCategory.WORKAROUNDS,
        "type": OptionType.NUMBER,
        "cli": ["--sleep-interval"],
        "description": "Sleep between downloads (seconds)",
        "default": None,
        "min": 0
    },
    "max_sleep_interval": {
        "category": OptionCategory.WORKAROUNDS,
        "type": OptionType.NUMBER,
        "cli": ["--max-sleep-interval"],
        "description": "Maximum sleep interval (seconds)",
        "default": None,
        "min": 0
    },
    "sleep_subtitles": {
        "category": OptionCategory.WORKAROUNDS,
        "type": OptionType.NUMBER,
        "cli": ["--sleep-subtitles"],
        "description": "Sleep before subtitle download (seconds)",
        "default": None,
        "min": 0
    },
    
    # Additional Network Options
    "socket_timeout": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.NUMBER,
        "cli": ["--socket-timeout"],
        "description": "Time to wait before giving up, in seconds",
        "default": None,
        "min": 0
    },
    "source_address": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.STRING,
        "cli": ["--source-address"],
        "description": "Client-side IP address to bind to",
        "default": None,
        "placeholder": "192.168.1.100"
    },
    "impersonate": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.STRING,
        "cli": ["--impersonate"],
        "description": "Client to impersonate for requests",
        "default": None,
        "placeholder": "chrome, firefox, safari"
    },
    "force_ipv4": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.BOOLEAN,
        "cli": ["-4", "--force-ipv4"],
        "description": "Make all connections via IPv4",
        "default": False
    },
    "force_ipv6": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.BOOLEAN,
        "cli": ["-6", "--force-ipv6"],
        "description": "Make all connections via IPv6",
        "default": False
    },
    "enable_file_urls": {
        "category": OptionCategory.NETWORK,
        "type": OptionType.BOOLEAN,
        "cli": ["--enable-file-urls"],
        "description": "Enable file:// URLs (disabled by default for security)",
        "default": False
    },
    
    # Additional Video Selection Options
    "min_filesize": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--min-filesize"],
        "description": "Abort download if filesize is smaller than SIZE",
        "default": None,
        "placeholder": "50k or 44.6M"
    },
    "max_filesize": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--max-filesize"],
        "description": "Abort download if filesize is larger than SIZE",
        "default": None,
        "placeholder": "50k or 44.6M"
    },
    "date": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--date"],
        "description": "Download only videos uploaded on this date",
        "default": None,
        "placeholder": "YYYYMMDD or today-2weeks"
    },
    "datebefore": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--datebefore"],
        "description": "Download only videos uploaded on or before this date",
        "default": None,
        "placeholder": "YYYYMMDD"
    },
    "dateafter": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--dateafter"],
        "description": "Download only videos uploaded on or after this date",
        "default": None,
        "placeholder": "YYYYMMDD"
    },
    "match_filter": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.STRING,
        "cli": ["--match-filters"],
        "description": "Generic video filter (OUTPUT TEMPLATE field comparisons)",
        "default": None,
        "placeholder": "like_count>?100 & description~='cats'"
    },
    "no_playlist": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-playlist"],
        "description": "Download only the video, if URL refers to video and playlist",
        "default": False
    },
    "yes_playlist": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.BOOLEAN,
        "cli": ["--yes-playlist"],
        "description": "Download the playlist, if URL refers to video and playlist",
        "default": False
    },
    "download_archive": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.FILE_PATH,
        "cli": ["--download-archive"],
        "description": "Download only videos not listed in archive file",
        "default": None
    },
    "max_downloads": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.NUMBER,
        "cli": ["--max-downloads"],
        "description": "Abort after downloading NUMBER files",
        "default": None,
        "min": 1
    },
    "break_on_existing": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.BOOLEAN,
        "cli": ["--break-on-existing"],
        "description": "Stop download when encountering file in archive",
        "default": False
    },
    "break_per_input": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.BOOLEAN,
        "cli": ["--break-per-input"],
        "description": "Reset max-downloads and break-on-existing per input URL",
        "default": False
    },
    "skip_playlist_after_errors": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.NUMBER,
        "cli": ["--skip-playlist-after-errors"],
        "description": "Number of allowed failures until playlist is skipped",
        "default": None,
        "min": 1
    },
    
    # Additional Download Options
    "concurrent_fragments": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.NUMBER,
        "cli": ["-N", "--concurrent-fragments"],
        "description": "Number of fragments to download concurrently",
        "default": 1,
        "min": 1
    },
    "limit_rate": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["-r", "--limit-rate"],
        "description": "Maximum download rate",
        "default": None,
        "placeholder": "50K or 4.2M"
    },
    "throttled_rate": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--throttled-rate"],
        "description": "Minimum download rate below which throttling is assumed",
        "default": None,
        "placeholder": "100K"
    },
    "file_access_retries": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.NUMBER,
        "cli": ["--file-access-retries"],
        "description": "Number of times to retry on file access error",
        "default": 3,
        "min": 0
    },
    "retry_sleep": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--retry-sleep"],
        "description": "Time to sleep between retries",
        "default": None,
        "placeholder": "linear=1::2 or exp=1:20"
    },
    "skip_unavailable_fragments": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--skip-unavailable-fragments"],
        "description": "Skip unavailable fragments for DASH/HLS downloads",
        "default": True
    },
    "keep_fragments": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--keep-fragments"],
        "description": "Keep downloaded fragments on disk after downloading",
        "default": False
    },
    "buffer_size": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--buffer-size"],
        "description": "Size of download buffer",
        "default": "1024",
        "placeholder": "1024 or 16K"
    },
    "http_chunk_size": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--http-chunk-size"],
        "description": "Size of chunk for chunk-based HTTP downloading",
        "default": None,
        "placeholder": "10485760 or 10M"
    },
    "playlist_random": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--playlist-random"],
        "description": "Download playlist videos in random order",
        "default": False
    },
    "lazy_playlist": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--lazy-playlist"],
        "description": "Process entries as they are received",
        "default": False
    },
    "hls_use_mpegts": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--hls-use-mpegts"],
        "description": "Use mpegts container for HLS videos",
        "default": None
    },
    "download_sections": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--download-sections"],
        "description": "Download only chapters matching regex",
        "default": None,
        "placeholder": "*10:15-inf or intro"
    },
    "external_downloader": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--downloader"],
        "description": "Name or path of external downloader to use",
        "default": None,
        "placeholder": "aria2c, curl, wget"
    },
    "external_downloader_args": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--downloader-args"],
        "description": "Arguments to give to external downloader",
        "default": None,
        "placeholder": "aria2c:--max-tries=10"
    },
    
    # Additional Filesystem Options  
    "paths": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.STRING,
        "cli": ["-P", "--paths"],
        "description": "The paths where files should be downloaded",
        "default": None,
        "placeholder": "TYPES:PATH"
    },
    "output_na_placeholder": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.STRING,
        "cli": ["--output-na-placeholder"],
        "description": "Placeholder for unavailable fields in output",
        "default": "NA",
        "placeholder": "N/A"
    },
    "restrict_filenames": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--restrict-filenames"],
        "description": "Restrict filenames to only ASCII characters",
        "default": False
    },
    "windows_filenames": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--windows-filenames"],
        "description": "Force filenames to be Windows-compatible",
        "default": False
    },
    "trim_filenames": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.NUMBER,
        "cli": ["--trim-filenames"],
        "description": "Limit filename length (excluding extension)",
        "default": None,
        "min": 1
    },
    "no_overwrites": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["-w", "--no-overwrites"],
        "description": "Do not overwrite any files",
        "default": False
    },
    "force_overwrites": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--force-overwrites"],
        "description": "Overwrite all video and metadata files",
        "default": False
    },
    "continue_dl": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["-c", "--continue"],
        "description": "Resume partially downloaded files/fragments",
        "default": True
    },
    "no_part": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-part"],
        "description": "Do not use .part files",
        "default": False
    },
    "mtime": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--mtime"],
        "description": "Use Last-modified header to set file modification time",
        "default": False
    },
    "write_description": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-description"],
        "description": "Write video description to .description file",
        "default": False
    },
    "write_info_json": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-info-json"],
        "description": "Write video metadata to .info.json file",
        "default": False
    },
    "write_playlist_metafiles": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-playlist-metafiles"],
        "description": "Write playlist metadata in addition to video metadata",
        "default": True
    },
    "clean_infojson": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--clean-info-json"],
        "description": "Remove some internal metadata from infojson",
        "default": True
    },
    "write_comments": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--write-comments"],
        "description": "Retrieve video comments to be placed in infojson",
        "default": False
    },
    "load_info_json": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.FILE_PATH,
        "cli": ["--load-info-json"],
        "description": "JSON file containing video information",
        "default": None
    },
    "cache_dir": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.STRING,
        "cli": ["--cache-dir"],
        "description": "Location in filesystem where yt-dlp can store information permanently",
        "default": None,
        "placeholder": "/path/to/cache"
    },
    "no_cache_dir": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--no-cache-dir"],
        "description": "Disable filesystem caching",
        "default": False
    },
    "rm_cache_dir": {
        "category": OptionCategory.FILESYSTEM,
        "type": OptionType.BOOLEAN,
        "cli": ["--rm-cache-dir"],
        "description": "Delete all filesystem cache files",
        "default": False
    },
    
    # Live Stream Options
    "live_from_start": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--live-from-start"],
        "description": "Download livestreams from the start",
        "default": False
    },
    "wait_for_video": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--wait-for-video"],
        "description": "Wait for scheduled streams (MIN[-MAX] seconds)",
        "default": None,
        "placeholder": "300 or 60-600"
    },
    "hls_prefer_native": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--hls-prefer-native"],
        "description": "Use native HLS downloader instead of ffmpeg",
        "default": False
    },
    "hls_prefer_ffmpeg": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.BOOLEAN,
        "cli": ["--hls-prefer-ffmpeg"],
        "description": "Use ffmpeg instead of native HLS downloader",
        "default": False
    },
    
    # Download Sections/Chapters
    "download_sections": {
        "category": OptionCategory.DOWNLOAD,
        "type": OptionType.STRING,
        "cli": ["--download-sections"],
        "description": "Download only chapters matching regex or time ranges",
        "default": None,
        "placeholder": "*10:15-inf or intro"
    },
    "remove_chapters": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.STRING,
        "cli": ["--remove-chapters"],
        "description": "Remove chapters matching regex from video",
        "default": None,
        "placeholder": "sponsor|intro"
    },
    
    # Additional Metadata Options
    "parse_metadata": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.STRING,
        "cli": ["--parse-metadata"],
        "description": "Parse additional metadata from filename/path",
        "default": None,
        "placeholder": "FROM_FIELD:TO_FIELD"
    },
    "replace_in_metadata": {
        "category": OptionCategory.POST_PROCESSING,
        "type": OptionType.STRING,
        "cli": ["--replace-in-metadata"],
        "description": "Replace text in metadata fields",
        "default": None,
        "placeholder": "FIELD REGEX REPLACE"
    },
    
    # Update and Version Options
    "update": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.BOOLEAN,
        "cli": ["--update"],
        "description": "Update yt-dlp to the latest version",
        "default": False
    },
    "update_self": {
        "category": OptionCategory.GENERAL,
        "type": OptionType.BOOLEAN,
        "cli": ["--update-self"],
        "description": "Update yt-dlp to the latest version (alias)",
        "default": False
    },
    "version": {
        "category": OptionCategory.VERBOSITY,
        "type": OptionType.BOOLEAN,
        "cli": ["--version"],
        "description": "Print program version and exit",
        "default": False
    },
    
    # Archive Options
    "download_archive": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.FILE_PATH,
        "cli": ["--download-archive"],
        "description": "Download only videos not listed in archive file",
        "default": None
    },
    "record_download_archive": {
        "category": OptionCategory.VIDEO_SELECTION,
        "type": OptionType.BOOLEAN,
        "cli": ["--record-download-archive"],
        "description": "Record downloaded videos in archive file",
        "default": False
    }
}

def get_options_by_category() -> Dict[OptionCategory, Dict[str, Dict]]:
    """Group options by category for UI rendering"""
    grouped = {}
    for key, option in YT_DLP_OPTIONS.items():
        category = option["category"]
        if category not in grouped:
            grouped[category] = {}
        grouped[category][key] = option
    return grouped

def get_default_options() -> Dict[str, Any]:
    """Get default values for all options"""
    return {key: option.get("default") for key, option in YT_DLP_OPTIONS.items()}

def convert_to_ydl_opts(form_data: Dict[str, Any]) -> Dict[str, Any]:
    """Convert form data to yt-dlp options dictionary"""
    ydl_opts = {}
    
    for key, value in form_data.items():
        if key in YT_DLP_OPTIONS and value is not None and value != "":
            option_config = YT_DLP_OPTIONS[key]
            
            # Handle different option types
            if option_config["type"] == OptionType.BOOLEAN:
                if isinstance(value, str):
                    ydl_opts[key] = value.lower() in ('true', '1', 'on', 'yes')
                else:
                    ydl_opts[key] = bool(value)
            elif option_config["type"] == OptionType.NUMBER:
                try:
                    ydl_opts[key] = int(value) if isinstance(value, str) else value
                except ValueError:
                    continue
            elif option_config["type"] == OptionType.MULTI_SELECT:
                if isinstance(value, str):
                    ydl_opts[key] = [v.strip() for v in value.split(',') if v.strip()]
                elif isinstance(value, list):
                    ydl_opts[key] = value
            else:
                ydl_opts[key] = value
                
    return ydl_opts