<script>
import titulo from "./components/titulo.vue"
console.log("perro");
export default {
  data() {
    return {
      botonText: "XD"
    }
  },
  components: {
    titulo
  }
}

</script>
<template>
  <titulo />
  <br>
  <button>{{ botonText }}</button>
</template>
<style>
button {
  color: green;
  background-color: red;
  border-radius: 10px;
  font-size: 3em;
}

button:hover {
  color: red;
  background-color: green;
}
</style>