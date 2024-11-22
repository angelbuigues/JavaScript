
// Mostrar los gimnasios
const gymInfo = document.querySelector('#gym-list');
const gyms = JSON.parse(localStorage.getItem('lista-gyms'));
const nameGym = localStorage.getItem("gymSelector");
const arrayGyms = JSON.parse(localStorage.getItem('arrayGyms'));

if (nameGym === null) {
    const gymDiv = document.createElement('div');
    gymDiv.className = 'gym';
    gymDiv.innerHTML = `
        <h3>Aun no has seleccionado un gimnasio</h3>
        <button id="voler-btn">Atras</button>
        `;
    gymInfo.appendChild(gymDiv);
    document.querySelector('#voler-btn').addEventListener('click', () => {
        window.location.href = './index.html';
    });
}
else {
    gyms.forEach(gym => {
        if (gym.name === nameGym) {
            const gymDiv = document.createElement('div');
            gymDiv.className = 'gym';
            gymDiv.innerHTML = `
            <h3>${gym.name}</h3>
            <img src="./img/${gym.name}.png" alt="FitFinder Logo">
            <p>Dirección: ${gym.address}, ${gym.city}</p>
            <p>Calificación: ${gym.rating} ⭐</p>
            <p>Servicios: ${gym.services.join(', ')}</p>
            <button id="reserve-btn">Reservar</button>
            `;
            gymInfo.appendChild(gymDiv);
        }

    });

    // Añadir eventos a los botones de reservar
    document.querySelector('#reserve-btn').addEventListener('click', () => {
        arrayGyms.push(nameGym);
        alert(`Has reservado en ${nameGym}`);
        console.log(arrayGyms);
        localStorage.setItem("arrayGyms", JSON.stringify(arrayGyms));
    });
}
