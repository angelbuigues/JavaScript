<script>
export default {
    data() {
        return {
            text: "Overdue",
            img: "🎡",
            num: 3
        }
    }
}

</script>
<template>
    <div class="containerOverdue">
        <div class="icon">{{ img }}</div>
        <div class="text">
            <p>{{ text }}</p>
            <p class="number">{{ num }}</p>
        </div>
    </div>

</template>
<style>


.containerOverdue {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 150px;
    height: 100px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    color: #fff;
    background-color: pink;
}

.containerOverdue .icon {
    font-size: 24px;
    margin-bottom: 8px;
}

.containerOverdue .text p {
    margin: 4px 0;
}

.containerOverdue .number {
    font-size: 18px;
    font-weight: bold;
}

.containerOverdue:hover {
    color: green;
    background-color: red;
}
</style>