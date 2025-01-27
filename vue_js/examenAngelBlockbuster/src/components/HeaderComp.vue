<script setup>
import { defineProps } from 'vue';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const props = defineProps({
    ListadoLinks: {
        type: Object,
        required: false,
    },
    nombreClasse: {
        type: String,
        required: false,
    },
});

const go = (path) => {
    router.push(path);
};
</script>
<template>
    <header :class="nombreClasse">
        <h1 class="titulo">Blockbuster</h1>
        <ul>
            <li>
                <button @click="go(props.ListadoLinks.path)">{{ props.ListadoLinks.name }}</button>
                <!-- <router-link :to="ListadoLinks.path">{{ ListadoLinks.name }}</router-link> -->
            </li>
        </ul>
    </header>
</template>
<style scoped>
.titulo {
    font-size: 2em;
    text-align: center;
    margin-bottom: 10px;
}

header {
    background-color: #333;
    padding: 10px;
}

ul {
    list-style-type: none;
    padding: 0;
    display: flex;
    justify-content: center;
}

li {
    margin: 0 15px;
}

a {
    color: white;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
</style>
