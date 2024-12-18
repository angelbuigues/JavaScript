<script>
export default {
    data() {
        return {
            text: "Scheduled",
            img: "📝",
            num: 5
        }
    }
}

</script>
<template>
    <div class="grid-container">
        <div class="container">
            <div class="icon">{{ img }}</div>
            <div class="text">
                <p>{{ text }}</p>
                <p class="number">{{ num }}</p>
            </div>
        </div>
    </div>

</template>
<style>


.containerScheduled {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 150px;
    height: 100px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    color: #fff;
    background-color: yellow;
}

.containerScheduled .icon {
    font-size: 24px;
    margin-bottom: 8px;
}

.containerScheduled .text p {
    margin: 4px 0;
}

.containerScheduled .number {
    font-size: 18px;
    font-weight: bold;
}

.containerScheduled:hover {
    color: green;
    background-color: red;
}
</style>