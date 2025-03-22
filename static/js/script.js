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

  // Handle honour button click
  function toggleHonour(button) {
    const timelineId = button.dataset.timelineId;

    fetch(`/timeline/honour/${timelineId}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
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
        // Toggle honoured state
        button.classList.toggle("honoured", data.honoured);

        // Update heart icon
        const iconElement = button.querySelector("span:first-child");
        if (data.honoured) {
          iconElement.className = "icon-[tabler--mug-filled] size-5";
        } else {
          iconElement.className = "icon-[tabler--mug] size-5";
        }

        // Update count
        const countElem = button.querySelector(".honour-count");
        if (countElem) {
          countElem.textContent = data.honour_count;
        }
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
});
