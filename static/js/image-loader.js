document.addEventListener('DOMContentLoaded', () => {
    const imageContainers = document.querySelectorAll('.image-container');
    
    // Create Intersection Observer for lazy loading
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const container = entry.target;
                const img = container.querySelector('img');
                
                if (img && !img.src) {
                    // Load the image
                    img.src = img.dataset.src;
                    
                    // Handle WebP support
                    if (img.dataset.webp) {
                        const picture = img.closest('picture');
                        if (picture) {
                            const source = picture.querySelector('source');
                            if (source) {
                                source.srcset = img.dataset.webp;
                            }
                        }
                    }
                    
                    // Add loaded class when image is loaded
                    img.onload = () => {
                        container.classList.add('loaded');
                    };
                    
                    // Remove from observer once loaded
                    observer.unobserve(container);
                }
            }
        });
    }, {
        rootMargin: '50px 0px',
        threshold: 0.1
    });
    
    // Observe all image containers
    imageContainers.forEach(container => {
        observer.observe(container);
    });
    
    // Handle image loading errors
    document.querySelectorAll('img').forEach(img => {
        img.onerror = () => {
            const container = img.closest('.image-container');
            if (container) {
                container.classList.add('error');
                container.innerHTML = '<div class="error-message">Failed to load image</div>';
            }
        };
    });
}); 