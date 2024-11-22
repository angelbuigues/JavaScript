import gyms from '../data/gym.json' with { type: 'json' };

console.log('JS Cargado');
console.log(gyms);

localStorage.setItem("lista-gyms", JSON.stringify(gyms));
const gymList = document.querySelector('#gym-list');


gyms.forEach(gym => {
    const gymDiv = document.createElement('div');
    gymDiv.className = 'gym';
    gymDiv.innerHTML = `
        <h3>${gym.name}</h3>
        <img src="./img/${gym.name}.png" alt="FitFinder Logo">
        `;
    gymList.appendChild(gymDiv);
});


document.querySelectorAll('.gym').forEach((gymSelector, index) => {
    gymSelector.addEventListener('click', () => {
        localStorage.setItem("gymSelector", `${gyms[index].name}`);
        window.location.href = './gyms.html';
    });
});