<script>
export default {
    props: [
        'h1Text',
        'clase'
    ],
    data() {
        return {
            // h1Text: "hola,",
        }
    }
}

</script>
<template>
    <h1 :class="clase">{{ h1Text }}</h1>
</template>
<style>
h1 {
    color: red;
    text-shadow: 2px 2px 4px #000000;
    font-style: italic;
}
</style>