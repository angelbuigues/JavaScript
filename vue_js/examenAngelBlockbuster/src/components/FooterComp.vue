<script setup>
import { defineProps } from 'vue';
import { ref, onMounted } from 'vue';
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
</script>
<template>
    <footer :class="nombreClasse">
        <h1>Blockbuster</h1>
        <ul>
            <li>
                <router-link :to="ListadoLinks.path">{{ ListadoLinks.name }}</router-link>
            </li>
        </ul>
    </footer>
</template>
<style scoped>
footer {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

footer ul {
    list-style-type: none;
    padding: 0;
}

footer li {
    margin: 10px 0;
}

footer a {
    color: #fff;
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;
}
</style>