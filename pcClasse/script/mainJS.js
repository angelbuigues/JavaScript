let usuario = ["34"]
let boolArray = []
console.log("hola")
let contador = 0
function anadir(){
    boolArray.push(isNaN(usuario[contador]))
    let array = document.getElementById("array")
    let crearP = document.createElement ("p")
    crearP.className = "r"
    crearP.textContent = usuario[contador] + " " + boolArray[contador]
    array.appendChild(crearP)
    
    contador++
    usuario.push("paco" + contador)
    console.log(isNaN(usuario[contador]))
    console.log(parseInt(usuario[contador]))
    
}

document.getElementById("botonClick").addEventListener('click',anadir)

