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
import miboton from "./components/Miboton.vue"
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
    miboton,
    contador
  },
  methods: {
    manejarEvento(mensaje) {
      alert(mensaje); // Muestra "¡Botón pulsado!"
    },
  },
}

</script>
<template>
  <titulo  h1Text="paco" clase="rojo" />

  <miboton @eventoClic="manejarEvento" text="hola" clase="rojo" />
  <miboton text="que" clase="verde" />
  <miboton text="tal" clase="azul" />

  <contador />
</template>
<style>
.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 150px);
  grid-gap: 15px;
}
</style>