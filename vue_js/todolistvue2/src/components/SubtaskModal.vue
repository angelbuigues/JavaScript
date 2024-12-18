<template>
    <div class="modal-overlay">
      <div class="modal-content">
        <h2>Add Subtask</h2>
        <input
          type="text"
          v-model="newSubtask"
          placeholder="Enter subtask"
          @keyup.enter="addSubtask"
        />
        <div class="modal-actions">
            <button @click="addSubtask">Add</button>
            <button @click="closeModal">Cancel</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SubtaskModal',
    props: {
      task: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        newSubtask: '',
      };
    },
    methods: {
      closeModal() {
        this.$emit('close-modal');
      },
      addSubtask() {
        if (this.newSubtask.trim()) {
          this.$emit('subtask-added', { task: this.task, subtask: this.newSubtask });
          this.newSubtask = '';
          this.closeModal();
        }
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
  }
  
  .modal-content {
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    width: 90%;
    max-width: 400px;
  }
  
  .modal-actions {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  }
  
  button {
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:first-of-type {
    background: #007bff;
    color: #fff;
  }

  button:last-of-type {
    background: #f5f5f5;
    color: #333;
  }
  </style>
  