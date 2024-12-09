<script>
export default {
    data() {
        return {
            text: "Today",
            img: "⏰",
            num: 6
        }
    }
}

</script>
<template>
    <div class="container">
        <div class="icon">{{ img }}</div>
        <div class="text">
            <p>{{ text }}</p>
            <p class="number">{{ num }}</p>
        </div>
    </div>

</template>
<style>


.container {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 150px;
    height: 100px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    color: #fff;
    background-color: blue;
}

.icon {
    font-size: 24px;
    margin-bottom: 8px;
}

.text p {
    margin: 4px 0;
}

.number {
    font-size: 18px;
    font-weight: bold;
}

.container:hover {
    color: green;
    background-color: red;
}
</style>