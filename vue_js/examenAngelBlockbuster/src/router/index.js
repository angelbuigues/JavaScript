import { createRouter, createWebHistory } from 'vue-router'
import Inicio from '@/views/Inicio.vue';
import ListadoPeliculas from '@/views/ListadoPeliculas.vue';
import PeliculaInfo from '@/views/PeliculaInfo.vue';
import Socios from '@/views/Socios.vue';
import Top10Peliculas from '@/views/Top10Peliculas.vue';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Inicio',
      component: Inicio,
    },
    { 
      path: '/ListadoPeliculas',
      name: 'ListadoPeliculas',
      component: ListadoPeliculas,
    },
    {
      path: '/PeliculaInfo',
      name: 'PeliculaInfo',
      component: PeliculaInfo,
    },
    {
      path: '/Socios',
      name: 'Socios',
      component: Socios,
    },
    {
      path: '/Top10Peliculas',
      name: 'Top10Peliculas',
      component: Top10Peliculas,
    },
  ],
})

export default router
