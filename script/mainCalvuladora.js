


document.addEventListener("DOMContentLoaded", () => {
    //console.log("dom cargado")

    var boton = document.getElementById("num").innerText
    console.log(boton.innerText)
    boton.addEventListener('click', document.getElementById("txt").innerText = boton)


})