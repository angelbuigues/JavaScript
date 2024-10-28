console.log("mi primer XD")
let conta 
function fenviar(){ 
    
    let ninput = document.getElementById("nombre").value;
    let einput = document.getElementById("email").value;

    document.getElementById("nombre2").innerText = ninput;
    document.getElementById("email2").innerText = einput;

    document.getElementById("nombre").value = null;
    document.getElementById("email").value = null;
    
    let checkinput1 = document.getElementById("miCheckbox").checked;
    let checkinput2 = document.getElementById("miCheckbox2").checked;
    let checkinput3 = document.getElementById("miCheckbox3").checked;

    document.getElementById("miCheckbox.").innerText = checkinput1;
    document.getElementById("miCheckbox.2").innerText = checkinput2;
    document.getElementById("miCheckbox.3").innerText = checkinput3;        

    document.getElementById("miCheckbox").checked = false;
    document.getElementById("miCheckbox2").checked = false;
    document.getElementById("miCheckbox3").checked = false;
}

function feditar(){
    let nenviado = document.getElementById("nombre2").value;
    let eenviado = document.getElementById("email2").value;

    document.getElementById("nombre").value = nenviado;
    document.getElementById("email").value = eenviado;
}

document.addEventListener("DOMContentLoaded", () => {
    //console.log("dom cargado")

    document.getElementById("enviar").addEventListener('click', fenviar)
    document.getElementById("editar").addEventListener('click', feditar)


})

