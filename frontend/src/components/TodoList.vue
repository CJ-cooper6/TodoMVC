<template>
  <div class="todo-app">
    <ul class="todo-list">
      <li v-for="todo in todos" :key="todo.id" class="todo-item">
        <span class="todo-title">{{ todo.title }}</span>
        <div class="todo-buttons">
          <button @click="editTodo(todo.id)" class="edit-button">编辑</button>
          <button @click="deleteTodo(todo.id)" class="delete-button">删除</button>
        </div>
      </li>
    </ul>
    <div class="add-todo">
      <input v-model="newTodo" placeholder="New Todo" class="todo-input" />
      <button @click="addTodo" class="add-button">添加</button>
    </div>
  </div>
</template>


<script>
import { ref, onMounted } from 'vue';
import TodoService from '../service';

export default {
  setup() {
    const todos = ref([]);
    const newTodo = ref('');

    const fetchTodos = () => {
      TodoService.getTodos()
        .then(response => {
          todos.value = response.data;
        })
        .catch(error => {
          console.error('获取失败:', error);
        });
    };

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

    const editTodo = (todoId) => {
      const newText = prompt('重新输入一个todo:');
      if (newText !== null) {
        TodoService.updateTodo(todoId, { title: newText })
          .then(() => {
            fetchTodos();
          })
          .catch(error => {
            console.error('更新失败:', error);
          });
      }
    };

    const deleteTodo = (todoId) => {
      if (confirm('确定删除?')) {
        TodoService.deleteTodo(todoId)
          .then(() => {
            fetchTodos();
          })
          .catch(error => {
            console.error('删除失败:', error);
          });
      }
    };

    onMounted(fetchTodos);

    return {
      todos,
      newTodo,
      fetchTodos,
      addTodo,
      editTodo,
      deleteTodo,
    };
  },
};
</script>

<style>
.todo-app {
  max-width: 600px;
  margin: auto;
  font-family: 'Arial', sans-serif;
}

.todo-list {
  list-style-type: none;
  padding: 0;
}

.todo-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}

.todo-title {
  flex-grow: 1;
}

.todo-buttons {
  display: flex;
  gap: 8px;
}

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

.edit-button,
.delete-button {
  padding: 8px;
  background-color: #2196f3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>