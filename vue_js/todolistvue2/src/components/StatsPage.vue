<script>
import Headder from './Header.vue';
import Stats from './Stats.vue';
import TaskList from './TaskList.vue';

export default {
    components: {
        Headder,
        Stats,
        TaskList,
    },
};
</script>

<template>
<div>
        <Headder />
        <main>
            <Stats />
            <TaskList />
        </main>
    </div>
</template>

<style>
main {
    padding: 20px;
}
</style>
