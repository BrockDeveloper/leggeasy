var documento = document.getElementById("documento");
var articolo = document.getElementById("articolo");
var testo = document.getElementById("testo");


function load_articles(response) {

    articolo.innerHTML = "";

    response = "<option selected disabled hidden >Seleziona un articolo</option>" + response

    articolo.insertAdjacentHTML("beforeend", response)
    articolo.disabled = false
}

function load_article(response) {

    testo.innerHTML = "";

    response = "<option selected disabled hidden >Seleziona un articolo</option>" + response

    testo.insertAdjacentHTML("beforeend", response)
}


document.addEventListener("DOMContentLoaded", function() {

    documento.addEventListener("change", function() {

        fetch("http://localhost:8080/"+documento.value)
              .then((response) => response.json())
              .then((json) => load_articles(json));
    })


    articolo.addEventListener("change", function() {

        fetch("http://localhost:8080/"+documento.value+"/"+articolo.value)
              .then((response) => response.json())
              .then((json) => load_article(json));
    })
})