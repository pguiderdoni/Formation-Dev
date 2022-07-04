let cv = document.getElementById("cv");

cv.style.cursor = "zoom-in";
cv.addEventListener("click", function () {
  if (cv.classList.contains("h-100")) {
    cv.classList.replace("h-100", "h-auto");
    cv.style.cursor = "zoom-out";
  } else if (cv.classList.contains("h-auto")) {
    cv.classList.replace("h-auto", "h-100");
    cv.style.cursor = "zoom-in";
  }
});
