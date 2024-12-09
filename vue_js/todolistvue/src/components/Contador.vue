<template>
    <div>
      <p>Contador: {{ contador }}</p>
      <button @click="incrementar">Incrementar</button>
      <button @click="decrementar">Decrementar</button>
    </div>
    <div>
    <p v-if="contador === 10">Crack Mastodonte Mamut</p>
    <p v-if="contador === -5">Lamentable Sepillo bastardo</p>
    <p v-else>Nada de nada</p>
    <p v-show="contador === 5">show</p>
  </div>
    <div>
    <!-- El valor del input está vinculado a la propiedad message -->
    <input v-model="message" placeholder="Escribe algo...">
    <p>El mensaje es: {{ message }}</p>
  </div>
  <div>
    <ul>
  <li v-for="(nombre, index) in nombres" :key="index">
    {{ index + 1 }}. {{ nombre }}
  </li>
</ul>
  </div>
  </template>
  
  <script>

  export default {
    
    data() {
      return {
        contador: 0,
        message: '',
        nombres: ["Juan", "María", "Carlos", "Ana"],
      };
    },
    methods: {
      incrementar() {
        this.contador++;
      },
      decrementar() {
        this.contador--;
      },
      
    },
  };
  </script>
<style scoped>
p{
    color: red;

}
</style>