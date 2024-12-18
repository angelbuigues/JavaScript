<template>
  <div class="tasks-summary">
    <div class="task-box today">
      <span class="emoji">{{ taskEmojis.today }}</span>
      <div class="task-content">
        <h3>{{ titles.today }}</h3>
        <p class="count">{{ taskData.today }}</p>
      </div>
    </div>

    <div class="task-box scheduled">
      <span class="emoji">{{ taskEmojis.scheduled }}</span>
      <div class="task-content">
        <h3>{{ titles.scheduled }}</h3>
        <p class="count">{{ taskData.scheduled }}</p>
      </div>
    </div>

    <div class="task-box all">
      <span class="emoji">{{ taskEmojis.all }}</span>
      <div class="task-content">
        <h3>{{ titles.all }}</h3>
        <p class="count">{{ taskData.all }}</p>
      </div>
    </div>

    <div class="task-box overdue">
      <span class="emoji">{{ taskEmojis.overdue }}</span>
      <div class="task-content">
        <h3>{{ titles.overdue }}</h3>
        <p class="count">{{ taskData.overdue }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Stats',
  data() {
    return {
      taskData: {
        today: 6,
        scheduled: 5,
        all: 14,
        overdue: 3,
      },
      taskEmojis: {
        today: '📅',
        scheduled: '⏳',
        all: '📋',
        overdue: '⚠️',
      },
      titles: {
        today: 'Today',
        scheduled: 'Scheduled',
        all: 'All',
        overdue: 'Overdue',
      }
    };
  },
};
</script>

<style scoped>
.tasks-summary {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  
  
}

.task-box {
  position: relative;
  background-color: #fff;
  border-radius: 8px;
  width: 23%;
  height: 120px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
  padding: 10px;
  color: #333;
  width: 100%;
  
}

.emoji {
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 20px;
}

.task-content {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  height: 100%;
}

h3 {
  font-size: 16px;
  margin: 0;
}

.count {
  font-size: 20px;
  font-weight: bold;
  
}

.today {
  background-color: cadetblue;
}

.scheduled {
  background-color: yellowgreen;
}

.all {
  background-color: goldenrod;
}

.overdue {
  background-color: pink;
}
</style>