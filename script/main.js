console.log("mi primer XD")
//alert("tonto")
function miBoton(){
    console.error("boton clickado")
    console.warn("boton clickado")
}

function noClick(){
    console.log("rrr")
}

function bAlert(){
    alert("tonto")
}

document.addEventListener("DOMContentLoaded", () => {
    //console.log("dom cargado")

    let bnoClick = document.getElementById("no-click")
    //console.log(bnoClick)

    bnoClick.addEventListener('click', noClick)

    document.getElementById("noAlert").addEventListener('click', bAlert)
})