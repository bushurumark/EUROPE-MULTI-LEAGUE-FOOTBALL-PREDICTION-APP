// Simple service worker for football prediction app
self.addEventListener('install', function(event) {
    console.log('Service Worker installed');
});

self.addEventListener('fetch', function(event) {
    console.log('Service Worker fetching:', event.request.url);
});
