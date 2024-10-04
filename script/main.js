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
function colorRojo() {
    let misClases = document.getElementsByClassName("f")
    misClases[0].classList.add('rojo')
}

document.addEventListener("DOMContentLoaded", () => {
    //console.log("dom cargado")

    let bnoClick = document.getElementById("no-click")
    //console.log(bnoClick)

    bnoClick.addEventListener('click', noClick)

    document.getElementById("noAlert").addEventListener('click', bAlert)

    let misClases = document.getElementsByClassName("f")
    console.log(misClases)

    misClases[2].classList.add('negrita')
    misClases[3].classList.remove("f")

    for (let index = 0; index < misClases.length; index++) {
        misClases[index].classList.add("hola")
        
    }
    document.getElementById("color").addEventListener('click', colorRojo)

})