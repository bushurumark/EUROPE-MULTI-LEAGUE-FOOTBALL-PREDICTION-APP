// Football Predictor Pro - Advanced JavaScript Enhancements

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeAnimations();
    initializeInteractiveElements();
    initializeFormEnhancements();
    initializePerformanceTracking();
    initializeResponsiveFeatures();
});

// Animation System
function initializeAnimations() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.card, .feature-card, .stat-card').forEach(el => {
        observer.observe(el);
    });

    // Parallax effect for hero sections
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.hero-section');
        
        parallaxElements.forEach(element => {
            const speed = 0.5;
            element.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });
}

// Interactive Elements
function initializeInteractiveElements() {
    // Enhanced hover effects
    document.querySelectorAll('.card, .btn, .feature-card').forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });
        
        element.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Loading states for buttons
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function() {
            if (!this.classList.contains('btn-loading')) {
                this.classList.add('btn-loading');
                this.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Loading...';
                
                // Reset after 2 seconds (for demo purposes)
                setTimeout(() => {
                    this.classList.remove('btn-loading');
                    this.innerHTML = this.getAttribute('data-original-text') || this.innerHTML;
                }, 2000);
            }
        });
    });

    // Tooltip system
    initializeTooltips();
}

// Form Enhancements
function initializeFormEnhancements() {
    // Real-time form validation
    document.querySelectorAll('input, select, textarea').forEach(input => {
        input.addEventListener('blur', validateField);
        input.addEventListener('input', clearValidation);
    });

    // Auto-save form data
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('input', debounce(saveFormData, 500));
        loadFormData(form);
    });

    // Enhanced select dropdowns
    document.querySelectorAll('select').forEach(select => {
        select.addEventListener('change', function() {
            this.classList.add('selected');
            setTimeout(() => {
                this.classList.remove('selected');
            }, 200);
        });
    });
}

// Performance Tracking
function initializePerformanceTracking() {
    // Track page load performance
    window.addEventListener('load', () => {
        const loadTime = performance.now();
        console.log(`Page loaded in ${loadTime.toFixed(2)}ms`);
        
        // Send analytics data
        if (typeof gtag !== 'undefined') {
            gtag('event', 'page_load', {
                'load_time': loadTime,
                'page_title': document.title
            });
        }
    });

    // Track user interactions
    document.addEventListener('click', (e) => {
        const target = e.target.closest('a, button, .card');
        if (target) {
            trackInteraction(target);
        }
    });
}

// Responsive Features
function initializeResponsiveFeatures() {
    // Mobile menu enhancements
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', () => {
            navbarCollapse.classList.toggle('show');
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navbarToggler.contains(e.target) && !navbarCollapse.contains(e.target)) {
                navbarCollapse.classList.remove('show');
            }
        });
    }

    // Responsive table handling
    const tables = document.querySelectorAll('.table-responsive');
    tables.forEach(table => {
        if (table.scrollWidth > table.clientWidth) {
            table.classList.add('has-horizontal-scroll');
        }
    });

    // Dynamic font sizing
    adjustFontSize();
    window.addEventListener('resize', debounce(adjustFontSize, 250));
}

// Utility Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function validateField(event) {
    const field = event.target;
    const value = field.value.trim();
    
    if (field.hasAttribute('required') && !value) {
        showFieldError(field, 'This field is required');
    } else if (field.type === 'email' && value && !isValidEmail(value)) {
        showFieldError(field, 'Please enter a valid email address');
    } else {
        clearFieldError(field);
    }
}

function clearValidation(event) {
    const field = event.target;
    clearFieldError(field);
}

function showFieldError(field, message) {
    clearFieldError(field);
    field.classList.add('is-invalid');
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    field.parentNode.appendChild(errorDiv);
}

function clearFieldError(field) {
    field.classList.remove('is-invalid');
    const errorDiv = field.parentNode.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.remove();
    }
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function saveFormData(event) {
    const form = event.target.closest('form');
    if (form) {
        const formData = new FormData(form);
        const data = {};
        
        for (let [key, value] of formData.entries()) {
            data[key] = value;
        }
        
        localStorage.setItem(`form_${form.id || 'default'}`, JSON.stringify(data));
    }
}

function loadFormData(form) {
    const savedData = localStorage.getItem(`form_${form.id || 'default'}`);
    if (savedData) {
        const data = JSON.parse(savedData);
        Object.keys(data).forEach(key => {
            const field = form.querySelector(`[name="${key}"]`);
            if (field && !field.value) {
                field.value = data[key];
            }
        });
    }
}

function initializeTooltips() {
    // Custom tooltip implementation
    document.querySelectorAll('[data-tooltip]').forEach(element => {
        element.addEventListener('mouseenter', showTooltip);
        element.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(event) {
    const element = event.target;
    const tooltipText = element.getAttribute('data-tooltip');
    
    const tooltip = document.createElement('div');
    tooltip.className = 'custom-tooltip';
    tooltip.textContent = tooltipText;
    
    document.body.appendChild(tooltip);
    
    const rect = element.getBoundingClientRect();
    tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
    tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';
    
    element.tooltip = tooltip;
}

function hideTooltip(event) {
    const element = event.target;
    if (element.tooltip) {
        element.tooltip.remove();
        element.tooltip = null;
    }
}

function trackInteraction(element) {
    const interactionData = {
        element: element.tagName.toLowerCase(),
        text: element.textContent.trim().substring(0, 50),
        timestamp: new Date().toISOString(),
        url: window.location.pathname
    };
    
    console.log('User interaction:', interactionData);
    
    // Send to analytics if available
    if (typeof gtag !== 'undefined') {
        gtag('event', 'user_interaction', interactionData);
    }
}

function adjustFontSize() {
    const width = window.innerWidth;
    const html = document.documentElement;
    
    if (width < 768) {
        html.style.fontSize = '14px';
    } else if (width < 1024) {
        html.style.fontSize = '16px';
    } else {
        html.style.fontSize = '18px';
    }
}

// Advanced Features
function initializeAdvancedFeatures() {
    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + K for search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            focusSearch();
        }
        
        // Escape to close modals
        if (e.key === 'Escape') {
            closeModals();
        }
    });

    // Progressive Web App features
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    }
}

function focusSearch() {
    const searchInput = document.querySelector('input[type="search"], .search-input');
    if (searchInput) {
        searchInput.focus();
    }
}

function closeModals() {
    const modals = document.querySelectorAll('.modal.show');
    modals.forEach(modal => {
        const modalInstance = bootstrap.Modal.getInstance(modal);
        if (modalInstance) {
            modalInstance.hide();
        }
    });
}

// Initialize advanced features
initializeAdvancedFeatures();

// Analytics Dashboard Functions
function initializeAnalyticsCharts() {
    console.log('🔍 Initializing analytics charts...');
    
    // Check if we're on the result page
    const strengthChart = document.getElementById('strengthChart');
    const probabilityChart = document.getElementById('probabilityChart');
    const formChart = document.getElementById('formChart');
    const h2hChart = document.getElementById('h2hChart');
    
    console.log('🔍 Chart elements found:', {
        strengthChart: !!strengthChart,
        probabilityChart: !!probabilityChart,
        formChart: !!formChart,
        h2hChart: !!h2hChart
    });
    
    if (strengthChart) {
        console.log('📊 Creating strength chart...');
        createStrengthChart();
    }
    
    if (probabilityChart) {
        console.log('📊 Creating probability chart...');
        createProbabilityChart();
    }
    
    if (formChart) {
        console.log('📊 Creating form chart...');
        createFormChart();
    }
    
    if (h2hChart) {
        console.log('📊 Creating H2H chart...');
        createH2HChart();
    }
}

function createStrengthChart() {
    console.log('🔍 Creating strength chart...');
    const ctx = document.getElementById('strengthChart').getContext('2d');
    
    // Get data from the page
    const homeStrengthElement = document.getElementById('home-strength');
    const awayStrengthElement = document.getElementById('away-strength');
    
    console.log('🔍 Strength elements:', {
        homeStrengthElement: homeStrengthElement?.textContent,
        awayStrengthElement: awayStrengthElement?.textContent
    });
    
    const homeStrength = parseFloat(homeStrengthElement?.textContent.replace('%', '') || '65');
    const awayStrength = parseFloat(awayStrengthElement?.textContent.replace('%', '') || '60');
    const homeTeam = document.querySelector('.home-team-name')?.textContent || 'Home Team';
    const awayTeam = document.querySelector('.away-team-name')?.textContent || 'Away Team';
    
    console.log('🔍 Chart data:', { homeStrength, awayStrength, homeTeam, awayTeam });
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [homeTeam, awayTeam],
            datasets: [{
                label: 'Team Strength (%)',
                data: [homeStrength, awayStrength],
                backgroundColor: [
                    'rgba(59, 130, 246, 0.8)',
                    'rgba(239, 68, 68, 0.8)'
                ],
                borderColor: [
                    'rgba(59, 130, 246, 1)',
                    'rgba(239, 68, 68, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

function createProbabilityChart() {
    console.log('🔍 Creating probability chart...');
    const ctx = document.getElementById('probabilityChart').getContext('2d');
    
    // Get probability data from the page
    const homeProbElement = document.getElementById('home-prob');
    const drawProbElement = document.getElementById('draw-prob');
    const awayProbElement = document.getElementById('away-prob');
    
    console.log('🔍 Probability elements:', {
        homeProb: homeProbElement?.textContent,
        drawProb: drawProbElement?.textContent,
        awayProb: awayProbElement?.textContent
    });
    
    const homeProb = parseFloat(homeProbElement?.textContent.replace('%', '') || '40');
    const drawProb = parseFloat(drawProbElement?.textContent.replace('%', '') || '30');
    const awayProb = parseFloat(awayProbElement?.textContent.replace('%', '') || '30');
    
    console.log('🔍 Chart probabilities:', { homeProb, drawProb, awayProb });
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Home Win', 'Draw', 'Away Win'],
            datasets: [{
                data: [homeProb, drawProb, awayProb],
                backgroundColor: [
                    'rgba(59, 130, 246, 0.8)',
                    'rgba(156, 163, 175, 0.8)',
                    'rgba(239, 68, 68, 0.8)'
                ],
                borderColor: [
                    'rgba(59, 130, 246, 1)',
                    'rgba(156, 163, 175, 1)',
                    'rgba(239, 68, 68, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

function createFormChart() {
    const ctx = document.getElementById('formChart').getContext('2d');
    
    // Create form data (W=Win, D=Draw, L=Loss)
    const formData = {
        labels: ['Last 5 Matches'],
        datasets: [
            {
                label: 'Home Team Form',
                data: [3], // Example: 3 points from last 5 matches
                backgroundColor: 'rgba(59, 130, 246, 0.6)',
                borderColor: 'rgba(59, 130, 246, 1)',
                borderWidth: 2
            },
            {
                label: 'Away Team Form',
                data: [2], // Example: 2 points from last 5 matches
                backgroundColor: 'rgba(239, 68, 68, 0.6)',
                borderColor: 'rgba(239, 68, 68, 1)',
                borderWidth: 2
            }
        ]
    };
    
    new Chart(ctx, {
        type: 'bar',
        data: formData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 15,
                    ticks: {
                        stepSize: 3
                    }
                }
            }
        }
    });
}

function createH2HChart() {
    const ctx = document.getElementById('h2hChart').getContext('2d');
    
    // Example head-to-head data
    const h2hData = {
        labels: ['Home Wins', 'Draws', 'Away Wins'],
        datasets: [{
            label: 'Head-to-Head Results',
            data: [3, 2, 1], // Example: 3 home wins, 2 draws, 1 away win
            backgroundColor: [
                'rgba(59, 130, 246, 0.8)',
                'rgba(156, 163, 175, 0.8)',
                'rgba(239, 68, 68, 0.8)'
            ],
            borderColor: [
                'rgba(59, 130, 246, 1)',
                'rgba(156, 163, 175, 1)',
                'rgba(239, 68, 68, 1)'
            ],
            borderWidth: 2
        }]
    };
    
    new Chart(ctx, {
        type: 'bar',
        data: h2hData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

// Initialize analytics charts when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeAnimations();
    initializeInteractiveElements();
    initializeFormEnhancements();
    initializePerformanceTracking();
    initializeResponsiveFeatures();
    initializeAnalyticsCharts();
});

// Export functions for global access
window.FootballPredictor = {
    trackInteraction,
    saveFormData,
    loadFormData,
    validateField,
    showTooltip,
    hideTooltip,
    initializeAnalyticsCharts,
    createStrengthChart,
    createProbabilityChart,
    createFormChart,
    createH2HChart
}; 