<template>
  <section id="tasks">
    <h2>Today's Task</h2>
    <ul>
      <li v-for="task in todayTasks" :key="task.id">
        <div class="task-header">
          <span class="time">{{ taskTitle }} {{ task.time }}</span>
          <p>{{ task.title }}</p>
          <button class="options-button" @click="openSubtaskModal(task)">
            ...
          </button>
        </div>
        <ul v-if="task.subtasks && task.subtasks.length">
          <li v-for="(subtask, index) in task.subtasks" :key="index">{{ subtask }}</li>
        </ul>
      </li>
    </ul>

    <!-- Botón para abrir el modal de creación de tareas -->
    <AddTaskButton @click="showTaskModal = true" />

    <!-- Modal para añadir una tarea -->
    <CreateTaskModal
      v-if="showTaskModal"
      @close-modal="showTaskModal = false"
      @task-created="addTask"
    />

    <!-- Modal para añadir subtasks -->
    <SubtaskModal
      v-if="showSubtaskModal"
      :task="selectedTask"
      @close-modal="closeSubtaskModal"
      @subtask-added="addSubtask"
    />
  </section>
</template>

<script>
import AddTaskButton from './AddTaskButton.vue';
import CreateTaskModal from './CreateTaskModal.vue';
import SubtaskModal from './SubtaskModal.vue';

export default {
  name: 'TaskList',
  components: {
    AddTaskButton,
    CreateTaskModal,
    SubtaskModal,
  },
  data() {
    return {
      tasks: [], // Lista general de tareas
      today: new Date().toISOString().split('T')[0], // Fecha actual en formato YYYY-MM-DD
      taskTitle: 'Today 📅 ',
      showTaskModal: false,
      showSubtaskModal: false,
      selectedTask: null, // Tarea seleccionada para añadir subtasks
    };
  },
  computed: {
    todayTasks() {
      // Filtra las tareas cuya fecha coincida con la fecha actual
      return this.tasks.filter((task) => task.date === this.today);
    },
  },
  methods: {
    addTask(newTask) {
      if (!newTask.subtasks) {
        newTask.subtasks = []; // Aseguramos que la tarea tiene subtasks
      }
      this.tasks.push(newTask);
      this.saveTasksToLocalStorage(); // Guarda las tareas en localStorage
    },
    openSubtaskModal(task) {
      this.selectedTask = task;
      this.showSubtaskModal = true;
    },
    closeSubtaskModal() {
      this.showSubtaskModal = false;
      this.selectedTask = null;
    },
    addSubtask({ task, subtask }) {
      if (!task.subtasks) {
        this.$set(task, 'subtasks', []); // Inicializamos subtasks si no existe
      }
      task.subtasks.push(subtask);
      this.saveTasksToLocalStorage(); // Guarda las tareas actualizadas en localStorage
    },
    saveTasksToLocalStorage() {
      localStorage.setItem('tasks', JSON.stringify(this.tasks));
    },
    loadTasksFromLocalStorage() {
      const savedTasks = localStorage.getItem('tasks');
      if (savedTasks) {
        this.tasks = JSON.parse(savedTasks);
      }
    },
  },
  mounted() {
    this.loadTasksFromLocalStorage(); // Carga las tareas al montar el componente
  },
};
</script>

<style scoped>
#tasks {
  position: relative;
  padding: 20px 0;
  background-color: #f8f9fa;
  border-radius: 8px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 15px;
  padding: 10px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.task-header {
  display: flex;
  flex-direction: column; /* Asegura que los elementos estén en columnas */
  justify-content: flex-start;
  position: relative;
}

.time {
  font-weight: bold;
  margin-bottom: 5px; /* Espacio entre la hora y el título */
}

p {
  margin: 0;
  font-size: 16px;
  color: #333;
  line-height: 1.4; /* Mejor separación entre líneas */
}

.options-button {
  position: absolute;
  top: 0;
  right: 0;
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
  color: #555;
}

.options-button:hover {
  color: #000; /* Efecto hover para el botón */
}
</style>
