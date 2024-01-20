<template>
  <div class="todo-app">
    <ul class="todo-list">
      <li v-for="todo in todos" :key="todo.id" class="todo-item">
        <div class="todo-title">{{ todo.title }}</div>
        <div class="todo-due-by">{{ todo.end_time }}</div>
        <div class="todo-status">{{ todo.completed }}</div>
        <div class="todo-buttons">
          <button @click="editTodo(todo.id)" class="edit-button">编辑</button>
          <button @click="deleteTodo(todo.id)" class="delete-button">删除</button>
        </div>
      </li>
    </ul>
  </div>
</template>


<script>
import { ref, onMounted } from 'vue';
import TodoService from '../service';

export default {
  setup() {
    const todos = ref([]);

    const fetchTodos = () => {
      TodoService.getTodos()
        .then(response => {
          todos.value = response.data;
          console.log(todos.value)
        })
        .catch(error => {
          console.error('获取失败:', error);
        });
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
      fetchTodos,
      editTodo,
      deleteTodo,
    };
  },
};
</script>

<style>
.todo-app {
  font-family: 'Arial', sans-serif;
  background-color: #fff;
  border-color: #fff;
  color: rgba(0,0,0,.87);
}

.todo-app .todo-list {
  list-style-type: none;
  padding: 0;
}

.todo-app .todo-list .todo-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 16px;
}

.todo-app .todo-list .todo-item .todo-title {

}

.todo-app .todo-list .todo-item .todo-due-by {

}

.todo-app .todo-list .todo-item .todo-status {

}

.todo-app .todo-list .todo-item .todo-buttons {

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