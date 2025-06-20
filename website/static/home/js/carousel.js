document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('carousel');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const courseCards = document.querySelectorAll('.course-card');
    const cardWidth = courseCards[0].offsetWidth + 30; // width + gap
    let position = 0;
    const maxPosition = -(cardWidth * (courseCards.length - 3));
    
    // Update carousel position
    function updateCarousel() {
        carousel.style.transform = `translateX(${position}px)`;
    }
    
    // Next button click
    nextBtn.addEventListener('click', function() {
        if (position > maxPosition) {
            position -= cardWidth;
            updateCarousel();
        }
    });
    
    // Previous button click
    prevBtn.addEventListener('click', function() {
        if (position < 0) {
            position += cardWidth;
            updateCarousel();
        }
    });
    
    // Auto slide every 5 seconds
    setInterval(function() {
        if (position > maxPosition) {
            position -= cardWidth;
            updateCarousel();
        } else {
            position = 0;
            updateCarousel();
        }
    }, 5000);
});