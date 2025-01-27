// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { movieList } from './script/functions'

const app = createApp(App)

app.use(router)

app.mount('#app')



// Inicializamos un arreglo vacío para almacenar los resultados
const movieListData = [];

// Limpiar movieList en localStorage antes de empezar
localStorage.setItem('movieList', JSON.stringify([]));

// Usar Promise.all para esperar que todas las peticiones fetch se resuelvan
Promise.all(movieList.map(movieTitle => {
    return fetch(`http://www.omdbapi.com/?apikey=c0316915&t=${movieTitle}`)
        .then(response => response.json())
        .then(data => movieListData.push(data))
        .catch(error => console.error('Error al cargar la película:', error));
})).then(() => {
    // Una vez que todas las peticiones hayan terminado, guardar en localStorage
    localStorage.setItem('movieList', JSON.stringify(movieListData));
});