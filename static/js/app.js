// Theme Management
function themeManager() {
    return {
        currentTheme: localStorage.getItem('theme') || 'vaporwave',
        
        init() {
            this.applyTheme(this.currentTheme);
        },
        
        toggleTheme() {
            this.currentTheme = this.currentTheme === 'vaporwave' ? 'matrix' : 'vaporwave';
            this.applyTheme(this.currentTheme);
            localStorage.setItem('theme', this.currentTheme);
        },
        
        applyTheme(theme) {
            const existingThemeLink = document.getElementById('theme-css');
            
            if (existingThemeLink) {
                const newHref = theme === 'matrix' ? '/static/css/matrix.css' : '/static/css/vaporwave.css';
                existingThemeLink.href = newHref;
            }
        }
    }
}

// Matrix Rain Effect
function createMatrixRain() {
    const matrixContainer = document.getElementById('matrix-rain');
    if (!matrixContainer) return;
    
    matrixContainer.innerHTML = '';
    
    const columnWidth = 20;
    const columns = Math.floor(window.innerWidth / columnWidth);
    
    for (let i = 0; i < columns; i++) {
        const column = document.createElement('div');
        column.className = 'matrix-column';
        column.style.left = i * columnWidth + 'px';
        column.style.animationDuration = (Math.random() * 3 + 2) + 's';
        column.style.animationDelay = Math.random() * 2 + 's';
        
        const charCount = 7;
        const binaryString = Array.from({length: 7}, () => Math.random() > 0.5 ? '1' : '0');
        
        for (let j = 0; j < charCount; j++) {
            const char = document.createElement('span');
            char.className = 'char';
            char.textContent = binaryString[j];
            
            if (j > charCount - 2) {
                char.classList.add('fade');
            }
            
            column.appendChild(char);
        }
        
        matrixContainer.appendChild(column);
    }
    
    setInterval(() => {
        const columns = matrixContainer.querySelectorAll('.matrix-column');
        columns.forEach(column => {
            if (Math.random() > 0.98) {
                const chars = column.querySelectorAll('.char');
                const newBinaryString = Array.from({length: 7}, () => Math.random() > 0.5 ? '1' : '0');
                chars.forEach((char, index) => {
                    char.textContent = newBinaryString[index];
                });
            }
        });
    }, 200);
}

function stopMatrixRain() {
    const matrixContainer = document.getElementById('matrix-rain');
    if (matrixContainer) {
        matrixContainer.innerHTML = '';
    }
}

function createAudioVisualizer() {
    let visualizerContainer = document.getElementById('audio-visualizer');
    if (!visualizerContainer) {
        visualizerContainer = document.createElement('div');
        visualizerContainer.id = 'audio-visualizer';
        document.body.appendChild(visualizerContainer);
    }
    
    visualizerContainer.innerHTML = '';
    
    const barWidth = 6;
    const barCount = Math.floor(window.innerWidth / (barWidth + 2));
    
    for (let i = 0; i < barCount; i++) {
        const bar = document.createElement('div');
        bar.className = 'audio-bar';
        bar.style.left = i * (barWidth + 2) + 'px';
        bar.style.width = barWidth + 'px';
        
        bar.style.animationDuration = (Math.random() * 1.5 + 0.5) + 's';
        bar.style.animationDelay = Math.random() * 2 + 's';
        const hue = (i / barCount) * 360;
        bar.style.background = `linear-gradient(to top, hsl(${hue}, 70%, 50%), hsl(${hue + 60}, 80%, 60%))`;
        bar.style.boxShadow = `0 0 8px hsl(${hue}, 70%, 50%)`;
        
        visualizerContainer.appendChild(bar);
    }
    
    setInterval(() => {
        const bars = visualizerContainer.querySelectorAll('.audio-bar');
        bars.forEach((bar, index) => {
            const baseHeight = Math.random() * 80 + 10;
            const beatIntensity = Math.sin(Date.now() * 0.001 + index * 0.1) * 30 + 30;
            bar.style.height = (baseHeight + beatIntensity) + 'px';
        });
    }, 150);
}

function stopAudioVisualizer() {
    const visualizerContainer = document.getElementById('audio-visualizer');
    if (visualizerContainer) {
        visualizerContainer.innerHTML = '';
    }
}

function createCatToys() {
    let toyContainer = document.getElementById('cat-toys');
    if (!toyContainer) {
        toyContainer = document.createElement('div');
        toyContainer.id = 'cat-toys';
        document.body.appendChild(toyContainer);
    }
    
    // Clear existing toys
    toyContainer.innerHTML = '';
    
    const funObjects = ['🐭', '🧶', '🐟', '🦴', '🏀', '🎾', '🪶', '🧸'];
    
    // Create initial floating objects
    for (let i = 0; i < 8; i++) {
        const toy = document.createElement('div');
        toy.className = 'cat-toy';
        toy.textContent = funObjects[Math.floor(Math.random() * funObjects.length)];
        toy.style.left = Math.random() * 100 + '%';
        toy.style.animationDuration = (Math.random() * 8 + 6) + 's';
        toy.style.animationDelay = Math.random() * 4 + 's';
        
        toyContainer.appendChild(toy);
    }
    
    // Continuously add new floating objects
    setInterval(() => {
        if (document.getElementById('cat-toys')) {
            const toy = document.createElement('div');
            toy.className = 'cat-toy';
            toy.textContent = funObjects[Math.floor(Math.random() * funObjects.length)];
            toy.style.left = Math.random() * 100 + '%';
            toy.style.animationDuration = (Math.random() * 8 + 6) + 's';
            
            toyContainer.appendChild(toy);
            
            // Remove object after animation
            setTimeout(() => {
                if (toy.parentNode) {
                    toy.parentNode.removeChild(toy);
                }
            }, 14000);
        }
    }, 2000);
}

function stopCatToys() {
    const toyContainer = document.getElementById('cat-toys');
    if (toyContainer) {
        toyContainer.remove();
    }
}

// Starry Night Particles Effect
function createStarryParticles() {
    let particleContainer = document.getElementById('starry-particles');
    if (!particleContainer) {
        particleContainer = document.createElement('div');
        particleContainer.id = 'starry-particles';
        document.body.appendChild(particleContainer);
    }
    
    // Clear existing particles
    particleContainer.innerHTML = '';
    
    // Create twinkling stars
    for (let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.className = 'star-particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDuration = (Math.random() * 3 + 2) + 's';
        particle.style.animationDelay = Math.random() * 3 + 's';
        
        // Vary star sizes and intensities
        const size = Math.random() * 2 + 1;
        particle.style.width = size + 'px';
        particle.style.height = size + 'px';
        
        // Some stars are brighter
        if (Math.random() > 0.8) {
            particle.style.boxShadow = '0 0 12px #ffd700';
        }
        
        particleContainer.appendChild(particle);
    }
    
    // Add some larger, slower-moving celestial bodies
    for (let i = 0; i < 8; i++) {
        const celestial = document.createElement('div');
        celestial.className = 'star-particle';
        celestial.style.left = Math.random() * 100 + '%';
        celestial.style.top = Math.random() * 60 + '%'; // Keep in upper part of sky
        celestial.style.width = (Math.random() * 4 + 3) + 'px';
        celestial.style.height = (Math.random() * 4 + 3) + 'px';
        celestial.style.animationDuration = (Math.random() * 6 + 4) + 's';
        celestial.style.animationDelay = Math.random() * 4 + 's';
        celestial.style.background = '#fff8dc';
        celestial.style.boxShadow = '0 0 15px #ffd700, 0 0 25px #fff8dc';
        
        particleContainer.appendChild(celestial);
    }
}

function stopStarryParticles() {
    const particleContainer = document.getElementById('starry-particles');
    if (particleContainer) {
        particleContainer.innerHTML = '';
    }
}

// No animated carbonation effects - keeping it simple and fast
function createCarbonationBubbles() {
    // No animated bubbles - just static background pattern
}

function stopCarbonationBubbles() {
    // No intervals to clear
}


// Direct theme selection function
function setTheme(themeName) {
    
    const themeLink = document.getElementById('theme-css');
    
    if (themeLink) {
        if (themeName === 'matrix') {
            themeLink.href = '/static/css/matrix.css';
        } else if (themeName === 'kelethin') {
            themeLink.href = '/static/css/kelethin.css';
        } else if (themeName === 'music') {
            themeLink.href = '/static/css/music.css';
        } else if (themeName === 'fun') {
            themeLink.href = '/static/css/fun.css';
        } else if (themeName === 'starry-night') {
            themeLink.href = '/static/css/starry-night.css';
        } else if (themeName === 'carbonation') {
            themeLink.href = '/static/css/carbonation.css';
        } else {
            themeLink.href = '/static/css/vaporwave.css';
        }
    }
    
    // Handle special effects - stop all first
    stopMatrixRain();
    stopAudioVisualizer();
    stopCatToys();
    stopStarryParticles();
    stopCarbonationBubbles();
    
    // Start appropriate effect
    if (themeName === 'matrix') {
        setTimeout(() => createMatrixRain(), 100);
    } else if (themeName === 'music') {
        setTimeout(() => createAudioVisualizer(), 100);
    } else if (themeName === 'fun') {
        setTimeout(() => createCatToys(), 100);
    } else if (themeName === 'starry-night') {
        setTimeout(() => createStarryParticles(), 100);
    } else if (themeName === 'carbonation') {
        setTimeout(() => createCarbonationBubbles(), 100);
    }
    
    // Update active button state
    document.querySelectorAll('.theme-option').forEach(btn => {
        btn.classList.remove('active');
    });
    document.getElementById(`theme-${themeName}`)?.classList.add('active');
    
    localStorage.setItem('theme', themeName);
}

// WebSocket Connection for Progress Updates
document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme buttons
    document.querySelectorAll('.theme-option').forEach(button => {
        button.addEventListener('click', function() {
            const themeName = this.getAttribute('data-theme');
            setTheme(themeName);
        });
    });
    
    // Make title and tagline clickable to apply CARBONATION theme
    const titleElement = document.getElementById('title-carbonation');
    const taglineElement = document.getElementById('tagline-carbonation');
    
    if (titleElement) {
        titleElement.addEventListener('click', function() {
            setTheme('carbonation');
        });
    }
    
    if (taglineElement) {
        taglineElement.addEventListener('click', function() {
            setTheme('carbonation');
        });
    }
    
    // Apply stored theme on load - CARBONATION is now the default!
    const currentTheme = localStorage.getItem('theme') || 'carbonation';
    setTheme(currentTheme);
    
    // Use current hostname for WebSocket connection
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const ws = new WebSocket(`${protocol}//${window.location.host}/ws/progress`);
    
    ws.onopen = function() {
        // WebSocket connected
    };
    
    ws.onerror = function(error) {
        // WebSocket error handling
    };
    
    ws.onclose = function() {
        // WebSocket disconnected
    };
    
    ws.onmessage = function(event) {
        const data = JSON.parse(event.data);
        const progressElement = document.getElementById(`progress-${data.download_id}`);
        
        if (progressElement) {
            if (data.status === 'downloading') {
                progressElement.innerHTML = `
                    <div class="flex justify-between items-center">
                        <span>Downloading: ${data.filename || 'Unknown'}</span>
                        <span>${data.percentage}</span>
                    </div>
                    <div class="flex justify-between text-xs mt-1">
                        <span>Speed: ${data.speed}</span>
                        <span>ETA: ${data.eta}</span>
                    </div>
                `;
            } else if (data.status === 'completed') {
                const downloadDiv = document.getElementById(`download-${data.download_id}`);
                if (downloadDiv) {
                    downloadDiv.className = 'success-neon card p-4 mb-4 relative group';
                    downloadDiv.innerHTML = `
                        <button onclick="this.parentElement.remove()" class="close-btn absolute top-2 right-2 text-gray-400 hover:text-white opacity-0 transition-opacity">
                            <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                            </svg>
                        </button>
                        <div class="flex items-center">
                            <div class="h-4 w-4 bg-green-600 rounded-full mr-3"></div>
                            <span>Download completed: ${data.filename}</span>
                        </div>
                    `;
                }
            } else if (data.status === 'error') {
                const downloadDiv = document.getElementById(`download-${data.download_id}`);
                if (downloadDiv) {
                    downloadDiv.className = 'error-neon card p-4 mb-4 relative group';
                    downloadDiv.innerHTML = `
                        <button onclick="this.parentElement.remove()" class="close-btn absolute top-2 right-2 text-gray-400 hover:text-white opacity-0 transition-opacity">
                            <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                            </svg>
                        </button>
                        <div class="flex items-center">
                            <div class="h-4 w-4 bg-red-600 rounded-full mr-3"></div>
                            <span>Download failed: ${data.error}</span>
                        </div>
                    `;
                }
            }
        }
    };
});