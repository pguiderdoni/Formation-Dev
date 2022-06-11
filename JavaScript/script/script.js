// afficher le contenu du bouton Spoiler
let spoilers = document.querySelectorAll(".spoiler");
for (s of spoilers) {
  let button = s.querySelector("button");
  button.addEventListener("click", function (e) {
    console.log("test");
    let spoil = s.querySelector(".spoiler-content");
    if (spoil.classList.contains("visible")) {
      s.querySelector(".spoiler-content").classList.remove("visible");
      this.innerHTML = "Afficher le spoil";
    } else {
      s.querySelector(".spoiler-content").classList.add("visible");
      this.innerHTML = "Masquer le spoil";
    }
  });
}

// fonction pour masquer l'active et afficher le nouvel element
let afficher = function (item) {
  let li = item.parentNode;
  let div = item.parentNode.parentNode.parentNode;
  // trouve la div quo est active et enleve l'attribut 'active'
  div.querySelector(".tabs .active").classList.remove("active");
  // ajoute 'active' sur la <li> selectionnée
  li.classList.add("active");
  // enleve le texte correspondant
  div.querySelector(".tabs-content .active").classList.remove("active");
  // affiche le text qui a le meme ID que la <li>
  div.querySelector(item.getAttribute("href")).classList.add("active");
};
//fonction qui attend un click sur un element <a>
// crée une variable liste(qui contient tous les liens <a>)
let tabs = document.querySelectorAll(".tabs a");
//et boucle sur chaque element de la liste
for (let tab of tabs) {
  tab.addEventListener("click", function () {
    // au click, on execute la fonction afficher()
    afficher(tab);
  });
}
// code pour rafraichir la page en restant sur le meme element
let a = document.querySelector('a[href="' + window.location.hash + '"]');
afficher(a);
