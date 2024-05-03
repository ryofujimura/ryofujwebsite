document.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("fade-in");
            } else {
                entry.target.classList.remove("fade-in");
            }
        });
    }, {
        threshold: 0.5
    });

    document.querySelectorAll('.experience-block').forEach(block => {
        observer.observe(block);
    });
});
