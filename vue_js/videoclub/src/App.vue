<script>
    import { RouterView } from 'vue-router';
    import HeaderView from './views/HeaderView.vue'
    import FooterView from './views/FooterView.vue'

    export default {
        components: {
            HeaderView,
            FooterView,
        }
    }
</script>

<template>
    <div>
        <HeaderView />
        <RouterView />
        <FooterView />
    </div>
</template>

<style>
    body{
        background-color: rgb(240, 240, 240);
    }
</style>