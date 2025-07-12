self.addEventListener('install', (e) => {
  console.log('Service Worker installed');
});

self.addEventListener('fetch', function(event) {
  // Optional: Add caching here
});
