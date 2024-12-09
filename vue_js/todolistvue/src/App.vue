<script>
import titulo from "./components/Titulo.vue"
import subtitulo from "./components/Subtitulo.vue"
import today from "./components/Today.vue"
import scheduled from "./components/Scheduled.vue"
import all from "./components/All.vue"
import overdue from "./components/Overdue.vue"
import titleTaskToday from "./components/TitleTaskToday.vue"
import menuu from "./components/Menu.vue"
import contador from "./components/Contador.vue"
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
    today,
    scheduled,
    all,
    overdue,
    titleTaskToday,
    menuu,
    contador
  }
}

</script>
<template>
  <titulo />
  <br>
  <subtitulo />
  
  <br>
  <today /> 
  <scheduled />
  <all />
  <overdue />
  <titleTaskToday />
  
  <br>
  <menuu />
  <br>
  <menuu />
  <br>
  <menuu />
  <br>
  <menuu />
  <br>
  <contador />
</template>
<style>

</style>