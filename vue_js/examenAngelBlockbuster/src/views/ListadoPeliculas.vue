<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

// const movieList = JSON.parse(localStorage.getItem('movieList'))

const movieList = ref([]); 
// Cargar datos al montar el componente
onMounted(() => {
    movieList.value = JSON.parse(localStorage.getItem('movieList') || '[]');
    console.log('Peliculas cargadas:', movieList.value);
});


const router = useRouter();
const goToMovieDetail = (titlePeli) => {
    localStorage.setItem('titlePeli', titlePeli);
    // router.push({ name: 'PeliculaInfo', params: { titlePeli } });
    router.push({ name: 'PeliculaInfo' });
};
</script>
<template>

<div class="movie-list-container">
    <div id="movie-list">
        
        <div v-for="(movie, index) in movieList" :key="index" class="movie" @click="goToMovieDetail(movie.Title)">
            <h3 >{{ movie.Title }}</h3>
            <img :src="movie.Poster" :alt="movie.Title" />

        </div>
    </div>
</div>
</template>