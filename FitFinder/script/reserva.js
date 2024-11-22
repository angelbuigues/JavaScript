
// Mostrar los gimnasios
const gymInfo = document.querySelector('#gym-list');
const gyms = JSON.parse(localStorage.getItem('lista-gyms'));
let arrayGyms = JSON.parse(localStorage.getItem('arrayGyms'));


if (arrayGyms.length === 0) {
    const gymDiv = document.createElement('div');
    gymDiv.className = 'gym';
    gymDiv.innerHTML = `
        <h3>Aun no has reservado un gimnasio</h3>
        <button id="voler-btn">Atras</button>
        `;
    gymInfo.appendChild(gymDiv);
    document.querySelector('#voler-btn').addEventListener('click', () => {
        window.location.href = './index.html';
    });
}
else {
    gyms.forEach(gym => {
        arrayGyms.forEach(gymName => {
            if (gym.name === gymName) {
                const gymDiv = document.createElement('div');
                gymDiv.className = 'gym';
                gymDiv.innerHTML = `
                <h3>${gym.name}</h3>
                <img src="./img/${gym.name}.png" alt="FitFinder Logo">
                <br>
                <button id="eliminar-btn" data-name="${gym.name}">Eliminar reserva</button>
                `;
                gymInfo.appendChild(gymDiv);
            }
        })


    });

    // Añadir eventos a los botones de reservar
    document.querySelectorAll('#eliminar-btn').forEach(button => {
        button.addEventListener('click', (e) => {
            const nameGym = e.target.getAttribute('data-name'); // Obtener el nombre del gimnasio
            alert(`Has eliminado la reserva en ${nameGym}`);

            // Actualizar el array y el Local Storage
            arrayGyms = arrayGyms.filter(gymName => gymName !== nameGym);
            localStorage.setItem("arrayGyms", JSON.stringify(arrayGyms));
            window.location.href = './reservas.html';
        });
    });


}
