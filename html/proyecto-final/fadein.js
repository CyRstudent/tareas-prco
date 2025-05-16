const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.5
});

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
});