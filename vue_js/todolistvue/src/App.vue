<script>
import titulo from "./components/Titulo.vue"
import subtitulo from "./components/Subtitulo.vue"
import today from "./components/Today.vue"
console.log("perro");
export default {
  data() {
    return {
      botonText: "XD"
    }
  },
  components: {
    titulo,
    subtitulo,
    today
  }
}

</script>
<template>
  <titulo />
  <br>
  <subtitulo />
  <br>
  <today />
  <today />
  <today />
  <today />
</template>
<style>

</style>