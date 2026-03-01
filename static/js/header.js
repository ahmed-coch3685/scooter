



document.addEventListener("DOMContentLoaded", function () {


//   const header = document.querySelector(".header");

//   window.addEventListener("scroll", function () {
//     if (window.scrollY > 50) {
//       header.classList.add("scrolled");
//     } else {
//       header.classList.remove("scrolled");
//     }
//   });


  /* =========================
     BURGER MENU + OVERLAY
  ==========================*/
  const burger = document.getElementById("burger");
  const menu = document.getElementById("nav-menu");
  const overlay = document.getElementById("overlay");

  function openMenu() {
    burger.classList.add("active");
    menu.classList.add("show");
    overlay.classList.add("show");
    document.body.style.overflow = "hidden";
  }

  function closeMenu() {
    burger.classList.remove("active");
    menu.classList.remove("show");
    overlay.classList.remove("show");
    document.body.style.overflow = "auto";
  }

  if (burger) {
    burger.addEventListener("click", function (e) {
      e.stopPropagation();
      if (menu.classList.contains("show")) {
        closeMenu();
      } else {
        openMenu();
      }
    });
  }

  if (overlay) {
    overlay.addEventListener("click", closeMenu);
  }

  // قفل لو ضغط بره المينيو
  document.addEventListener("click", function (e) {
    if (menu && menu.classList.contains("show")) {
      if (!menu.contains(e.target) && !burger.contains(e.target)) {
        closeMenu();
      }
    }
  });


  /* =========================
     SEARCH OVERLAY
  ==========================*/
  const searchOverlay = document.getElementById("searchOverlay");
  const searchField = document.getElementById("searchFeild");

  window.openSearch = function () {
    if (searchOverlay) {
      searchOverlay.style.display = "flex";
      document.body.style.overflow = "hidden";
      setTimeout(() => {
        if (searchField) searchField.focus();
      }, 200);
    }
  };

  window.closeSearch = function () {
    if (searchOverlay) {
      searchOverlay.style.display = "none";
      document.body.style.overflow = "auto";
    }
  };

  window.resetSearch = function () {
    if (searchField) {
      searchField.value = "";
      searchField.focus();
    }
  };


  /* =========================
     CLOSE WITH ESC
  ==========================*/
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeMenu();
      closeSearch();
    }
  });


  /* =========================
     DARK MODE + SAVE
  ==========================*/
  const darkToggle = document.getElementById("darkToggle");

  function enableDark() {
    document.body.classList.add("dark");
    localStorage.setItem("theme", "dark");
  }

  function disableDark() {
    document.body.classList.remove("dark");
    localStorage.setItem("theme", "light");
  }

  if (darkToggle) {
    darkToggle.addEventListener("click", function () {
      if (document.body.classList.contains("dark")) {
        disableDark();
      } else {
        enableDark();
      }
    });
  }

  // تحميل الوضع المحفوظ
  if (localStorage.getItem("theme") === "dark") {
    enableDark();
  }


  /* =========================
     TO TOP BUTTON
  ==========================*/
  const toTopBtn = document.getElementById("toTop");

  window.addEventListener("scroll", function () {
    if (toTopBtn) {
      if (window.scrollY > 200) {
        toTopBtn.style.display = "block";
      } else {
        toTopBtn.style.display = "none";
      }
    }
  });

  if (toTopBtn) {
    toTopBtn.addEventListener("click", function () {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  }


  /* =========================
     ACCESSIBILITY
  ==========================*/
  let fontSize = 16;
  const accessBtn = document.querySelector(".access-btn");
  const accessMenu = document.querySelector(".access-menu");

  if (accessBtn) {
    accessBtn.addEventListener("click", function () {
      if (accessMenu.style.display === "block") {
        accessMenu.style.display = "none";
      } else {
        accessMenu.style.display = "block";
      }
    });
  }

  window.changeFont = function (val) {
    fontSize += val;

    if (fontSize <6) fontSize =6;
    if (fontSize > 96) fontSize = 96;

    document.body.style.fontSize = fontSize + "px";
  };

  window.toggleContrast = function () {
    document.body.classList.toggle("high-contrast");
  };

  window.resetAccess = function () {
    fontSize = 16;
    document.body.style.fontSize = "16px";
    document.body.classList.remove("high-contrast");
  };

});