document.getElementById("name").addEventListener("input", function (event) {
  document.getElementById("res-name").innerHTML = event.target.value;
});

document.getElementById("gender").addEventListener("change", function (event) {
  document.getElementById("res-gender").innerHTML = event.target.value;
});

document.getElementById("map").addEventListener("mousemove", function (event) {
  document.getElementById("mouse-x").innerHTML = event.offsetX;
  document.getElementById("mouse-y").innerHTML = event.offsetY;
});

let parentCount = 0;
let childCount = 0;

document.getElementById("parent").addEventListener("click", function (event) {
  parentCount += 1;
  document.getElementById("parent-count").innerHTML = parentCount;
});

document.getElementById("child").addEventListener("click", function (event) {
  childCount += 1;
  event.preventDefault();
  event.stopPropagation();
  document.getElementById("child-count").innerHTML = childCount;
});
