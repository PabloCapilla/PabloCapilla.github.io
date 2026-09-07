(function () {
  var carousel = document.querySelector("[data-landing-carousel]");

  if (!carousel) return;

  var slides = carousel.querySelectorAll(".landing-hero__image");
  var credit = document.querySelector("[data-carousel-credit]");
  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  if (slides.length < 2 || reducedMotion.matches) return;

  var currentSlide = 0;
  var interval = Number(carousel.getAttribute("data-interval")) || 8000;
  var timer;

  function showNextSlide() {
    slides[currentSlide].classList.remove("is-active");
    slides[currentSlide].setAttribute("aria-hidden", "true");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("is-active");
    slides[currentSlide].removeAttribute("aria-hidden");

    if (credit) {
      credit.textContent = slides[currentSlide].getAttribute("data-credit") || "";
    }
  }

  function startCarousel() {
    window.clearInterval(timer);
    timer = window.setInterval(showNextSlide, interval);
  }

  startCarousel();

  document.addEventListener("visibilitychange", function () {
    if (document.hidden) {
      window.clearInterval(timer);
    } else {
      startCarousel();
    }
  });
})();
