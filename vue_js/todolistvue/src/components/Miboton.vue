<script>
export default {
    props: [
        'text',
        'clase'
    ],
    methods: {
        enviarEvento() {
            this.$emit("eventoClic", "¡Botón pulsado!");
        },
    },
}
</script>

<template>
    <button :class="clase" @click="enviarEvento">
        {{ text }}
    </button>
</template>

<style scoped>
button {
    border-radius: 5px;
    border: none;
    display: block;
    margin-bottom: 10px;
    cursor: pointer;
    padding: 10px 20px;
    width: 100%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.rojo {
    color: red;
    background-color: salmon;
}

.verde {
    color: green;
    background-color: salmon;
}

.azul {
    color: blue;
    background-color: salmon;
}
</style>