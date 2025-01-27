<script>
export default {
    props: ['imdbID'],
    data() {
        return {
            movie: null  
        }
    },
    created() {
        const movieList = JSON.parse(localStorage.getItem('movieList')) || []
        
        this.movie = movieList.find(movie => movie.imdbID === this.imdbID)
    }
}
</script>

<template>
    <div v-if="movie">
        <h1>{{ movie.Title }}</h1>
        <img :src="movie.Poster" :alt="movie.Title">

        <p><strong>Year:</strong> {{ movie.Year }}</p>
        <p><strong>Director:</strong> {{ movie.Director }}</p>
        <p><strong>Plot:</strong> {{ movie.Plot }}</p>
    </div>
    <div v-else>
        <p>Cargando...</p>
    </div>
</template>



<style>
</style>
