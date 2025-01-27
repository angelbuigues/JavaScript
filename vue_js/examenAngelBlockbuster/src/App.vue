<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Headerino from './components/HeaderComp.vue';
import Footerino from './components/FooterComp.vue';

</script>

<template>
  <div class="cuerpo">
    <!-- <Headerino /> -->
    <RouterView />
    <!-- <Footerino /> -->
  </div>
</template>

<style>

.cuelpo {
  display: grid;
  grid-template-rows: 2000px auto;
  height: 100vh;
}
canvas {
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
  width: 100%;
  height: 100%;
}
</style>
