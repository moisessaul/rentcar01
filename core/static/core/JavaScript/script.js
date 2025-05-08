window.addEventListener("scroll", function() {
  const navbar = document.querySelector(".custom-navbar");
  if (window.scrollY > 50) {
    navbar.classList.add("navbar-scrolled");
  } else {
    navbar.classList.remove("navbar-scrolled");
  }
});

// Resaltar elemento de navegación activo
document.addEventListener("DOMContentLoaded", function() {
  const navLinks = document.querySelectorAll(".nav-link");

  navLinks.forEach(link => {
    link.addEventListener("click", function() {
      navLinks.forEach(item => {
        item.parentElement.classList.remove("active");
      });
      this.parentElement.classList.add("active");
    });
  });

  // Animación para los enlaces de navegación
  const navItems = document.querySelectorAll(".navbar-nav .nav-item");
  navItems.forEach((item, index) => {
    item.style.animation = `fadeInDown 0.5s ease forwards ${index * 0.1 +
      0.3}s`;
    item.style.opacity = "0";
  });
});
