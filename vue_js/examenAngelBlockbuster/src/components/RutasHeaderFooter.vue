<script setup>
import { ref } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import HeaderComp from '@/components/HeaderComp.vue';
import FooterComp from '@/components/FooterComp.vue';

const ListadoLinks = [
    { name: 'Inicio', path: '/' },
    { name: 'ListadoPeliculas', path: '/ListadoPeliculas' },
    { name: 'PeliculaInfo', path: '/PeliculaInfo' },
    { name: 'Socios', path: '/Socios' },
    { name: 'Top10Peliculas', path: '/Top10Peliculas' },
];

</script>
<template>
    <HeaderComp 
    v-for="ListadoLinks in ListadoLinks"
    :key="ListadoLinks.name"
    :ListadoLinks="ListadoLinks"
    :nombreClasse="headerclass"
    />
    <FooterComp 
    v-for="ListadoLinks in ListadoLinks"
    :key="ListadoLinks.name"
    :ListadoLinks="ListadoLinks"
    :nombreClasse="footerclass"

    />
  
</template>