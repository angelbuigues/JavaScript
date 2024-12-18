<template>
    <div class="task-categories-page">
        <header class="categories-header">
            <button class="back-button" @click="goBack">{{ backIcon }}</button>
            <h1>{{ title }}</h1>
        </header>

        <div class="categories-list">
            <div class="category-box grocery">
                <div class="category-content">
                    <h3>{{ title1 }}</h3>
                    <p>{{ notes1 }}</p>
                </div>
                <div class="category-stats">
                    <span class="completed">{{ completed1 }}</span>
                    <button class="details-button">{{ button }}</button>
                </div>
            </div>
            <div class="category-box educational">
                <div class="category-content">
                    <h3>{{ title2 }}</h3>
                    <p>{{ notes2 }}</p>
                </div>
                <div class="category-stats">
                    <span class="completed">{{ completed2 }}</span>
                    <button class="details-button">{{ button }}</button>
                </div>
            </div>
            <div class="category-box home">
                <div class="category-content">
                    <h3>{{ title3 }}</h3>
                    <p>{{ notes3 }}</p>
                </div>
                <div class="category-stats">
                    <span class="completed">{{ completed3 }}</span>
                    <button class="details-button">{{ button }}</button>
                </div>
            </div>
            <div class="category-box work">
                <div class="category-content">
                    <h3>{{ title4 }}</h3>
                    <p>{{ notes4 }}</p>
                </div>
                <div class="category-stats">
                    <span class="completed">{{ completed4 }}</span>
                    <button class="details-button">{{ button }}</button>
                </div>
            </div>
            <div class="category-box mandatory">
                <div class="category-content">
                    <h3>{{ title5 }}</h3>
                    <p>{{ notes5 }}</p>
                </div>
                <div class="category-stats">
                    <span class="completed">{{ completed5 }}</span>
                    <button class="details-button">{{ button }}</button>
                </div>
            </div>
            <div class="category-box personal">
                <div class="category-content">
                    <h3>{{ title6 }}</h3>
                    <p>{{ notes6 }}</p>
                </div>
                <div class="category-stats">
                    <span class="completed">{{ completed6 }}</span>
                    <button class="details-button">{{ button }}</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            title: 'All Task List',
            backIcon: '⬅️',
            title1: 'Grocery',
            notes1: '15 notes',
            completed1: '7 Completed',
            title2: 'Educational',
            notes2: '6 notes',
            completed2: '2 Completed',
            title3: 'Home',
            notes3: '8 notes',
            completed3: '5 Completed',
            title4: 'Work',
            notes4: '14 notes',
            completed4: '12 Completed',
            title5: 'Mandatory Work',
            notes5: '3 notes',
            completed5: '2 Completed',
            title6: 'Personal Notes',
            notes6: '3 notes',
            completed6: '2 Completed',
            button: '↗',
        };
    },
};
</script>

<style scoped>
.task-categories-page {
    padding: 20px;
}

.categories-header {
    display: flex;
    align-items: center;
    gap: 10px;
}

.back-button {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
}

.category-box {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out;
}

.category-box.grocery {
    background-color: gainsboro;
}

.category-box.educational {
    background-color: cornflowerblue;
}

.category-box.home {
    background-color: greenyellow;
}

.category-box.work {
    background-color: coral;
}

.category-box.mandatory {
    background-color: red;
}

.category-box.personal {
    background-color: palevioletred;
}

.category-box:hover {
    transform: translateY(-2px);
}

.category-content h3 {
    margin: 0;
    font-size: 18px;
}

.category-content p {
    margin: 0;
    color: #555;
    font-size: 14px;
}

.category-stats {
    display: flex;
    align-items: center;
    gap: 10px;
}

.completed {
    font-size: 14px;
    color: #555;
}

.details-button {
    background: none;
    border: none;
    font-size: 18px;
    cursor: pointer;
    color: #333;
}

.categories-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-top: 20px;
}
</style>