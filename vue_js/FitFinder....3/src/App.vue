<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Headerino from './components/Header.vue';
import Footerino from './components/Footer.vue';
//import './assets/body.js';
</script>

<template>
  <div class="cuerpo">
    <Headerino />
    <RouterView />
    <Footerino />
  </div>
</template>

<style scoped>
.cuerpo{
  display: grid;
  grid-template-rows: 1000px auto;
  height: 100vh;
}
canvas{
  position:fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}
</style>
