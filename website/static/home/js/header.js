const header = document.querySelector("header");
let lastScroll = 0;
const scrollThreshold = 10;
const animationDuration = 0.3;

// Initialize header with original styles
header.style.transition = `transform ${animationDuration}s ease-in-out`;
header.style.transform = "translateY(0)"; // Start visible

window.addEventListener("scroll", () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > lastScroll && currentScroll > scrollThreshold) {
        header.style.transform = "translateY(-100%)";
    } 
    else if (currentScroll < lastScroll) {
        header.style.transform = "translateY(0)";
    }
    
    lastScroll = currentScroll;
});