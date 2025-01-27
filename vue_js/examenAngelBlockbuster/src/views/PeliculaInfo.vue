<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const movieList = ref([]); 
const movie = ref([]); 
const title = ref(localStorage.getItem('titlePeli'));
// const title = ref(route.params.titlePeli);
console.log('Titulo:', title.value);
console.log('movie:', movie.value);

onMounted(() => {
    movieList.value = JSON.parse(localStorage.getItem('movieList') || '[]');
    if (title.value) {
    movie.value = movieList.value.find(movie => movie.Title === title.value);
    }
});

const goBack = () => {
    router.push('/ListadoPeliculas');

};

</script>
<template>
  <div>
    <div v-if="!title">
      <h3>La película seleccionada no existe.</h3>
      <button id="volver-btn" @click="goBack">Atrás</button>
    </div>

    <div v-else>
      <div class="movie">
        <h3>{{ movie.Title }}</h3>
            <img :src="movie.Poster" :alt="movie.Title" />
            <p>Director: {{ movie.Director }}</p>
            <p>Año: {{ movie.Year }}</p>
            <p>Calificación: {{ movie.Rating }} ⭐</p>
            <p>Descripción: {{ movie.Description }}</p>
      </div>
    </div>
  </div>

</template>