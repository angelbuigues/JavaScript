<template>
    <div class="modal-overlay">
      <div class="modal-content">
        <h3>Create a Task</h3>
        <form @submit.prevent="submitTask">
          <label for="title">Task Title:</label>
          <input type="text" id="title" v-model="newTask.title" required />
  
          <label for="time">Time:</label>
          <input type="time" id="time" v-model="newTask.time" required />
  
          <label for="date">Date:</label>
          <input type="date" id="date" v-model="newTask.date" required />
  
          <div class="buttons">
            <button type="submit">Add Task</button>
            <button type="button" @click="$emit('close-modal')">Cancel</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CreateTaskModal',
    data() {
      return {
        newTask: {
          title: '',
          time: '',
          date: '',
        },
      };
    },
    methods: {
      submitTask() {
        // Formatear la hora antes de enviar la tarea
        const formattedTime = this.formatTime(this.newTask.time);
        const taskToEmit = { ...this.newTask, time: formattedTime };
  
        this.$emit('task-created', taskToEmit);
        this.$emit('close-modal');
        this.resetForm();
      },
      resetForm() {
        this.newTask = {
          title: '',
          time: '',
          date: '',
        };
      },
      formatTime(time) {
        // Convierte la hora (HH:mm) en formato de 12 horas con AM/PM
        const [hours, minutes] = time.split(':');
        const hours12 = (hours % 12) || 12; // Convierte 0 a 12
        const amPm = hours >= 12 ? 'PM' : 'AM';
        return `${hours12}:${minutes} ${amPm}`;
      },
    },
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    width: 90%;
    max-width: 400px;
  }
  
  form {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  
  .buttons {
    display: flex;
    justify-content: space-between;
  }
  
  button {
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button[type="submit"] {
    background-color: #007bff;
    color: white;
  }
  
  button[type="button"] {
    background-color: #ccc;
  }
  </style>
  