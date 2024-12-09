<script>
export default {
    data() {
        return {
            text: "Today",
            img: "⏰ 4:50 PM",
            title: "Project retrospective"
        }
    }
}

</script>
<template>
    <div class="task-card">
        <div class="left-section">
            <div class="circle"></div>
            <div class="details">
                <div class="metadata">
                    <span class="date">{{ text }}</span>
                    <span class="time">{{ img }}</span>
                </div>
                <div class="tite">{{ title }}</div>
            </div>
        </div>
        <div class="right-section">
            <span class="menu">⋮</span>
        </div>
    </div>

</template>
<style>
.task-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 350px;
    height: 80px;
    background-color: #f0f4ff;
    border-radius: 20px;
    padding: 10px 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.task-card .left-section {
    display: flex;
    align-items: center;
}

.task-card .circle {
    width: 20px;
    height: 20px;
    border: 2px solid #4c8cff;
    border-radius: 50%;
    margin-right: 15px;
}

.task-card .details {
    display: flex;
    flex-direction: column;
}

.task-card .metadata {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 12px;
    color: #8a8a8a;
}

.task-card .metadata .time {
    display: flex;
    align-items: center;
    gap: 4px;
}

.task-card .tite {
    font-size: 16px;
    font-weight: bold;
    color: #333333;
    margin-top: 5px;
}

.task-card .right-section {
    font-size: 18px;
    color: #8a8a8a;
    cursor: pointer;
}
</style>