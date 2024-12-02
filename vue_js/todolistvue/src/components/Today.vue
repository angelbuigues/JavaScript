<script>
export default {
    data() {
        return {
            text: "hola",
            img: "https://img.freepik.com/foto-gratis/imagen-campamento-espacial_23-2148751306.jpg?w=2000",
            num: 0
        }
    }
}

</script>
<template>
    <div class="today">
        <img :src="img" alt="">
        <p class="text">{{ text }}</p>
        <p class="num">{{ num }}</p>
    </div>
</template>
<style>
div.today {
    color: red;
    background-color: green;
    border-radius: 10px;
    font-size: 3em;
}
div.today:hover {
    color: green;
    background-color: red;
}
div.today img {
    border-radius: 10px;
    width: 20%;
    height: 20%;
}

div.today p{
    display: grid;
    grid-template-columns: 1fr 1fr;
}


</style>