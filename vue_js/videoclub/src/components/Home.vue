<script>
    const movieList = JSON.parse(localStorage.getItem('movieList'))

    export default {
        data(){
            return {
                movies: movieList,
            }
        }
    }
        
</script>

<template>
    <div class="movie-list">
        <div class="movie" v-for="movie in movies">
            <router-link :to="`/movie/${movie.imdbID}`">
                <h3>
                    {{ movie.Title }}
                    <img v-for="rating in parseInt(movie.Ratings[0].Value.split('/')[0]/2)" src="../assets/star.png" alt="">
                </h3>
                <img class="poster" :src="movie.Poster" :alt="movie.Title">
            </router-link>
        </div>
    </div>
</template>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Jersey+15&display=swap');

    a {
        text-decoration: none;
        color: rgb(58, 58, 58);
    }


    .movie-list {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        column-gap: 20px;
        row-gap: 50px;
        
        width: 80%;
        margin: 20px auto;
    }

    .movie .poster {
        text-align: center;

        box-shadow: 3px 3px 8px 2px rgb(173 173 173);

        border: solid 2px rgb(16, 16, 16);
        border-radius: 12px;

        max-height: 400px;
    }

    .movie {
        font-family: "Jersey 15", serif;
        font-weight: 400;
        font-style: normal;
        font-size: 1.5em;
    }

    .movie h3 {
        margin-bottom: 5px;
    }
</style>