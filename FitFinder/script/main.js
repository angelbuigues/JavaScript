import gym from '../data/gym.json' with {type: 'json'};

let gymNames = [];
gym.forEach(gymName => {
    gymNames.push(gymName.name);
});

console.log("hola")

let contador = 0

function anadir() {
    let array = document.getElementById("array")
    let crearP = document.createElement("p")
    crearP.className = "r"
    crearP.textContent = gymNames[contador]
    array.appendChild(crearP)

    contador++
}



document.getElementById("botonClick").addEventListener('click', anadir)

