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


function apijokes() {
    fetch('https://api.chucknorris.io/jokes/random')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud');
            }
            return response.json(); // Convertir la respuesta a JSON
        })
        .then(data => {
            console.log(data.value); // Aquí podríamos procesar los datos
            let array = document.getElementById("array")
            let crearP = document.createElement("p")
            crearP.className = "r"
            crearP.textContent = data.value
            array.appendChild(crearP)
        })
        .catch(error => {
            console.error('Hubo un problema con la solicitud:', error);
        });


}

document.getElementById("botonApi").addEventListener('click', apijokes)
document.getElementById("botonClick").addEventListener('click',anadir)

