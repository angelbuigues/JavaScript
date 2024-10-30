console.log("mi primer XD")
let conta = 0
function enviar(){ 
    
    let input = document.getElementById("tarea").value;
    console.log(input);
    
    let miDiv = document.getElementById("f");
    
    let nuevoParrafo = document.createElement("p");
    nuevoParrafo.className = "r";
    nuevoParrafo.textContent = conta + " " + input; 
    
    miDiv.appendChild(nuevoParrafo);
    conta += 1
    
}


document.addEventListener("DOMContentLoaded", () => {
    //console.log("dom cargado")
    

    let bnoClick = document.getElementById("lclick")
    //console.log(bnoClick)

    bnoClick.addEventListener('click', enviar)

})











// Función para mostrar el aviso de cookies si no ha sido aceptado o rechazado
function verificarCookies() {
    if (!getCookie("cookiesAceptadas")) {
        document.getElementById("cookiess").style.display = "block";
    }
}

// Función para crear una cookie
function setCookie(nombre, valor, dias) {
    let fecha = new Date();
    fecha.setTime(fecha.getTime() + (dias * 24 * 60 * 60 * 1000));
    let expiracion = "expires=" + fecha.toUTCString();
    document.cookie = nombre + "=" + valor + ";" + expiracion + ";path=/";
}

// Función para obtener el valor de una cookie
function getCookie(nombre) {
    let nombreIgual = nombre + "=";
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let c = cookies[i].trim();
        if (c.indexOf(nombreIgual) === 0) {
            return c.substring(nombreIgual.length, c.length);
        }
    }
    return "";
}

// Función para aceptar cookies
function aceptarCookies() {
    setCookie("cookiesAceptadas", "true", 365);
    document.getElementById("cookiess").style.display = "none";
}

// Función para rechazar cookies
function rechazarCookies() {
    setCookie("cookiesAceptadas", "false", 365);
    document.getElementById("cookiess").style.display = "none";
}

// Asignar eventos a los botones
document.addEventListener("DOMContentLoaded", function () {
    verificarCookies();

    document.querySelector("#cookiess button:nth-of-type(1)").addEventListener("click", aceptarCookies);
    document.querySelector("#cookiess button:nth-of-type(2)").addEventListener("click", rechazarCookies);
});
