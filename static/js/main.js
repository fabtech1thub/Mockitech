// Add fade-in animation to elements when they come into view
document.addEventListener('DOMContentLoaded', function() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    });

    // Observe all cards and sections
    document.querySelectorAll('.card, section').forEach((el) => {
        observer.observe(el);
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Add active class to current navigation item
document.addEventListener('DOMContentLoaded', function() {
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });

    // Initialize Bootstrap dropdowns
    const dropdownElementList = document.querySelectorAll('.dropdown-toggle');
    const dropdownList = [...dropdownElementList].map(dropdownToggleEl => {
        return new bootstrap.Dropdown(dropdownToggleEl, {
            offset: [0, 10],
            popperConfig: {
                modifiers: [
                    {
                        name: 'preventOverflow',
                        options: {
                            boundary: 'viewport'
                        }
                    }
                ]
            }
        });
    });

    // Close mega menu when clicking outside
    document.addEventListener('click', function(event) {
        const megaMenu = document.querySelector('.mega-menu');
        const servicesDropdown = document.getElementById('servicesDropdown');
        
        if (!megaMenu?.contains(event.target) && !servicesDropdown?.contains(event.target)) {
            const dropdown = bootstrap.Dropdown.getInstance(servicesDropdown);
            if (dropdown) {
                dropdown.hide();
            }
        }
    });
}); 