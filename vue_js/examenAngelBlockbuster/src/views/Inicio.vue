<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();

const go = (path) => {
    router.push(path);
};
</script>
<template>
    <div>
        <h1>¡Bienvenido a Blockbuster!</h1>
        <p>En este sitio podrás encontrar información sobre las películas más populares, los socios más activos y las películas más rentadas.</p>
        <p>¡Disfruta de tu visita!</p>
    </div>
    <button @click="go('/ListadoPeliculas')">Ver Películas</button>
</template>