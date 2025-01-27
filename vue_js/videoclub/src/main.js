// import './assets/main.css'

import { createApp } from 'vue'
import { createWebHashHistory, createRouter } from 'vue-router'
import { movieList, getMovieInfo } from './script/functions'

import App from './App.vue'
import Home from './components/Home.vue'
import MoviesView from './views/MoviesView.vue'
import Movie from './views/Movie.vue'

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



const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/movies',
            name: 'movies',
            component: MoviesView
        },
        {
            path: '/movie/:imdbID',
            name: 'movie',
            component: Movie,
            props: true
        }
    ]
})

createApp(App)
    .use(router)
    .mount('#app')
