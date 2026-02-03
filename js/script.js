
document.addEventListener('DOMContentLoaded', () => {

    // Smooth scrolling for navigation links
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

    // Scroll Reveal Animation
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    document.querySelectorAll('.stage-card').forEach(card => {
        observer.observe(card);
    });

    // Navbar background change on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = "0 2px 10px rgba(0,0,0,0.1)";
        } else {
            navbar.style.boxShadow = "none";
        }
    });

    // Tab Component Functionality
    const initTabs = () => {
        document.querySelectorAll('.tab-container').forEach(container => {
            const tabBtns = container.querySelectorAll('.tab-btn');
            const tabPanels = container.querySelectorAll('.tab-panel');

            tabBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    const targetTab = btn.dataset.tab;

                    // Remove active class from all buttons and panels in this container
                    tabBtns.forEach(b => b.classList.remove('active'));
                    tabPanels.forEach(p => p.classList.remove('active'));

                    // Add active class to clicked button and corresponding panel
                    btn.classList.add('active');
                    const targetPanel = container.querySelector(`#${targetTab}`);
                    if (targetPanel) {
                        targetPanel.classList.add('active');
                    }
                });
            });
        });
    };

    initTabs();

    // Accordion Itinerary Functionality
    const initAccordion = () => {
        document.querySelectorAll('.accordion-item').forEach(item => {
            const header = item.querySelector('.accordion-header');

            header.addEventListener('click', () => {
                // Check if this item is already active
                const isActive = item.classList.contains('active');

                // Optional: Close all other accordions (uncomment for single-open mode)
                // item.closest('.accordion-itinerary').querySelectorAll('.accordion-item').forEach(i => {
                //     i.classList.remove('active');
                // });

                // Toggle current item
                if (isActive) {
                    item.classList.remove('active');
                } else {
                    item.classList.add('active');
                }
            });
        });

        // Open first item by default (optional)
        const firstItem = document.querySelector('.accordion-itinerary .accordion-item');
        if (firstItem) {
            firstItem.classList.add('active');
        }
    };

    initAccordion();

    // Animate cards on scroll
    const animateOnScroll = () => {
        const cards = document.querySelectorAll('.quick-nav-card, .info-card, .weather-card, .photo-spot-card, .shopping-area, .emergency-card');

        const cardObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, index * 50);
                    cardObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        cards.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            cardObserver.observe(card);
        });
    };

    animateOnScroll();

    // Parallax Effect for City Heroes
    const initParallax = () => {
        const parallaxBgs = document.querySelectorAll('.parallax-bg');

        if (parallaxBgs.length === 0) return;

        const handleParallax = () => {
            parallaxBgs.forEach(bg => {
                const hero = bg.closest('.city-hero');
                if (!hero) return;

                const rect = hero.getBoundingClientRect();
                const scrollPercent = (window.innerHeight - rect.top) / (window.innerHeight + rect.height);

                if (scrollPercent > 0 && scrollPercent < 1) {
                    const yOffset = (scrollPercent - 0.5) * 50; // -25px to +25px movement
                    bg.style.transform = `translateY(${yOffset}px) scale(1.1)`;
                }
            });
        };

        // Throttle scroll event for performance
        let ticking = false;
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    handleParallax();
                    ticking = false;
                });
                ticking = true;
            }
        });

        handleParallax(); // Initial call
    };

    initParallax();

    // Animate Visual Guide Steps on Scroll
    const animateVisualGuide = () => {
        const stepCards = document.querySelectorAll('.step-card');

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, index * 100);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });

        stepCards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;
            observer.observe(card);
        });
    };

    animateVisualGuide();

    // City Hero Content Animation
    const animateCityHero = () => {
        const heroContents = document.querySelectorAll('.city-hero-content');

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });

        heroContents.forEach(content => {
            content.style.opacity = '0';
            content.style.transform = 'translateY(30px)';
            content.style.transition = 'opacity 0.8s ease-out, transform 0.8s ease-out';
            observer.observe(content);
        });
    };

    animateCityHero();

    // Smooth number counter animation (for stats if needed)
    const animateValue = (element, start, end, duration) => {
        const range = end - start;
        let current = start;
        const increment = end > start ? 1 : -1;
        const stepTime = Math.abs(Math.floor(duration / range));

        const timer = setInterval(() => {
            current += increment;
            element.textContent = current;
            if (current === end) {
                clearInterval(timer);
            }
        }, stepTime);
    };

    // Add loading="lazy" to images that don't have it
    document.querySelectorAll('img:not([loading])').forEach(img => {
        if (!img.src.includes('hero.png')) { // Don't lazy load hero
            img.setAttribute('loading', 'lazy');
        }
    });
});
