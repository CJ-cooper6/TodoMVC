<template>
    <div class="add-todo">
        <input v-model="newTodo" placeholder="New Todo" class="todo-input" />
        <button @click="addTodo" class="add-button">添加</button>
    </div>
</template>

<script lang="js" setup>
import { ref } from 'vue';
import TodoService from '../service';

const newTodo = ref('');

const addTodo = () => {
    if (newTodo.value) {
        TodoService.addTodo({ title: newTodo.value })
            .then(() => {
                newTodo.value = '';
                fetchTodos();
            })
            .catch(error => {
                console.error('增加todo失败:', error);
            });
    }
};

</script>

<style>
.todo-input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 8px;
  flex-grow: 1;
}

.add-button {
  padding: 8px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
  