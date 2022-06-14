let alert_del = document.querySelectorAll(".alertdel");
alert_del.forEach((x) =>
  x.addEventListener("click", function () {
    // x.parentElement.classList.add("hidden");
    x.parentElement.parentElement.removeChild(x.parentElement);
  })
);
