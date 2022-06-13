function drawRond() {
  var canvas = document.getElementById("canvas");
  if (canvas.getContext) {
    var ctx = canvas.getContext("2d");

    ctx.beginPath();
    ctx.arc(75, 75, 50, 0, Math.PI * 2, true); // Cercle extérieur
    ctx.moveTo(110, 75);
  }
}

let canvas = document.querySelectorAll("");
