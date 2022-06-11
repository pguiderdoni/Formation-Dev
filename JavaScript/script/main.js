// en fonction séparée
let myImage = document.querySelector("#img1");

let swapImg = function (i) {
  let mySrc = i.getAttribute("src");
  if (mySrc == "img/pic1.webp") {
    i.setAttribute("src", "img/pic2.webp");
  } else {
    i.setAttribute("src", "img/pic1.webp");
  }
};
myImage.addEventListener("click", function () {
  swapImg(myImage);
});
//
//
//
//
// en fonction anonyme
let myImage2 = document.querySelector("#img2");

myImage2.addEventListener("click", function () {
  let mySrc = myImage2.getAttribute("src");
  if (mySrc === "img/pic3.webp") {
    myImage2.setAttribute("src", "img/pic4.webp");
  } else {
    myImage2.setAttribute("src", "img/pic3.webp");
  }
});
//
//
//
//
//en fonction anonyme
let myImage3 = document.querySelector("#img3");

myImage3.addEventListener("click", function () {
  swapImage(myImage3);
});

function swapImage(i) {
  let mySrc = i.getAttribute("src");
  if (mySrc === "img/pic5.jpeg") {
    i.setAttribute("src", "img/pic6.jpeg");
  } else {
    i.setAttribute("src", "img/pic5.jpeg");
  }
}
