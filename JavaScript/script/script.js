let canvas = document.querySelectorAll("canvas");
let tourCount = 0;
let coupJoue = [0, 0, 0, 0, 0, 0, 0, 0, 0];

function drawRond(y) {
  if (canvas[y].getContext) {
    let ctx = canvas[y].getContext("2d");
    ctx.beginPath();
    ctx.arc(75, 75, 50, 0, Math.PI * 2, true);
    ctx.stroke();
  }
}
function drawCroix(y) {
  if (canvas[y].getContext) {
    let ctx = canvas[y].getContext("2d");
    ctx.beginPath();
    ctx.moveTo(25, 125);
    ctx.lineTo(125, 25);
    ctx.moveTo(25, 25);
    ctx.lineTo(125, 125);
    ctx.stroke();
    ctx.closePath();
  }
}
for (let i = 0; i < canvas.length; i++) {
  canvas[i].addEventListener("click", function () {
    if (tourCount % 2 == 0) {
      drawCroix(i);
      coupJoue[i] = "X";
      tourCount += 1;
    } else {
      drawRond(i);
      coupJoue[i] = "O";
      tourCount += 1;
    }
    console.log("tour: " + tourCount);
    console.log("liste de coups: " + coupJoue);
  });
}
