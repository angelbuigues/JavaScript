<template>
  <head id="header">
    <div class="header-left">
      <h1>{{ greetings[0] }}</h1>
      <p>{{ greetings[1] }}</p>
    </div>
    <div class="header-icons">
      <button class="icon-button">
        {{ notifications }}
      </button>
      <button class="icon-button">
        {{ groupedTask }}
      </button>
    </div>
  </head>
</template>


<script>
export default {
  
  data() {
    return {
      greetings: [
        'Hello Àngel,',
        'You have work today',
      ],
      notifications: '🔔',
      groupedTask: '📝',
    };
  },
};
</script>

<style scoped>
#header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #f5f5f5;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-left {
  display: flex;
  flex-direction: column;
}

.header-left h1 {
  font-size: 24px;
  margin: 0;
  color: #333;
}

.header-left p {
  font-size: 16px;
  margin: 5px 0 0;
  color: #666;
}

.header-icons {
  display: flex;
  gap: 10px;
}

.icon-button {
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  transition: transform 0.2s ease;
  text-decoration: none;
}

.icon-button:hover {
  transform: scale(1.2);
}

.icon-button:focus {
  outline: none;
}
</style>