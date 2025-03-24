"use strict";

document.addEventListener("DOMContentLoaded", () => {
  // Get CSRF token from cookies
  function getCookie(name) {
    const cookie = document.cookie
      .split(";")
      .map((cookie) => cookie.trim())
      .find((cookie) => cookie.startsWith(`${name}=`));
    return cookie ? decodeURIComponent(cookie.split("=")[1]) : null;
  }

  // Redirect to login page
  function redirectToLogin() {
    window.location.href = `/accounts/login/?next=${window.location.pathname}`;
  }

  // Update honor button state based on response
  function updateButtonState(button, isHonoured, count) {
    const isHomePage = button.classList.contains("flex");
    const svg = button.querySelector("svg");
    const iconElement = button.querySelector("span:first-child");

    // Handle SVG-based buttons (used in some templates)
    if (svg) {
      svg.setAttribute("fill", isHonoured ? "currentColor" : "none");

      if (isHonoured) {
        button.classList.remove("text-gray-500");
        button.classList.add("text-red-500");
      } else {
        button.classList.remove("text-red-500");
        button.classList.add("text-gray-500");
      }
    }
    // Handle icon-based buttons (used across templates)
    else if (iconElement) {
      iconElement.className = isHonoured
        ? "icon-[tabler--heart-filled] size-5"
        : "icon-[tabler--heart] size-5";

      if (isHomePage) {
        if (isHonoured) {
          button.classList.remove("text-gray-500");
          button.classList.add("text-red-500", "honoured");
        } else {
          button.classList.remove("text-red-500", "honoured");
          button.classList.add("text-gray-500");
        }
      } else {
        // For honour.html and timeline.html style
        button.classList.toggle("honoured", isHonoured);
      }
    }

    // Update count (works across all templates)
    const countElem = button.querySelector(".honour-count");
    if (countElem) {
      countElem.textContent = count;
    }
  }

  // Handle honour button click
  function toggleHonour(button) {
    const timelineId = button.dataset.timelineId;

    // Use consistent endpoint
    fetch(`/timeline/honour/${timelineId}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
      credentials: "same-origin",
    })
      .then((response) => {
        if (!response.ok) {
          if (response.status === 403) {
            redirectToLogin();
          }
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        // Update button state with unified function
        updateButtonState(button, data.honoured, data.honour_count);
      })
      .catch((error) => console.error("Error:", error));
  }

  // Add click event listeners to all honour buttons
  const honourButtons = document.querySelectorAll(".honour-btn");
  honourButtons.forEach((button) => {
    button.addEventListener("click", () => {
      if (!document.body.classList.contains("user-logged-in")) {
        redirectToLogin();
        return;
      }
      toggleHonour(button);
    });
  });

  // Mobile menu toggle
  const burgerBtn = document.getElementById("navbar-burger");
  const dropdown = document.getElementById("navbar-dropdown");

  if (burgerBtn && dropdown) {
    burgerBtn.addEventListener("click", () => {
      dropdown.classList.toggle("hidden");
    });
  }
});
