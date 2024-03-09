var documento = document.getElementById("documento");
var articolo = document.getElementById("articolo");
var articoloSelezionato = document.getElementById("selectArticoli")
var ricercaArticolo = document.getElementById("ricercaArticolo")
var testo = document.getElementById("testo");


function load_articles(response) {

    articolo.innerHTML = "";

    response = "<option selected disabled hidden >Seleziona un articolo</option>" + response

    articolo.insertAdjacentHTML("beforeend", response)
    selectArticoli.disabled = false
}

function load_article(response) {

    testo.innerHTML = "";

    response = "<option selected disabled hidden >Seleziona un articolo</option>" + response

    testo.insertAdjacentHTML("beforeend", response)
}


document.addEventListener("DOMContentLoaded", function() {

    documento.addEventListener("change", function() {

        fetch("https://leggeasy.vercel.app/"+documento.value)
              .then((response) => response.json())
              .then((json) => load_articles(json));
    })


    ricercaArticolo.addEventListener("click", function() {

        fetch("https://leggeasy.vercel.app/"+documento.value+"/"+ articoloSelezionato.value)
              .then((response) => response.json())
              .then((json) => load_article(json));
    })
})
