<template>
  <div class="todo-app">
    <ul class="todo-list">
      <li v-for="todo in todos" :key="todo.id" class="todo-item">
        <div class="todo-title">{{ todo.title }}</div>
        <div class="todo-due-by">{{ todo.end_time }}</div>
        <button :class="getButtonClass(todo.completed)">
          {{ getButtonText((todo.completed)) }}
        </button>
        <div class="spacer"></div>
        <div class="todo-buttons">
          <button @click="editTodo(todo.id)" class="edit-button">编辑</button>
          <button @click="deleteTodo(todo.id)" class="delete-button">删除</button>
        </div>
      </li>
    </ul>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import TodoService from '../service';


const todos = ref([]);

const fetchTodos = () => {
  TodoService.getTodos()
    .then(response => {
      todos.value = response.data;
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

const getButtonClass = (completed) => {
  return {
    'button-completed-true': completed === true,
    'button-completed-false': completed === false,
  };
};

const getButtonText = (completed) => {
      return completed === true ? '已完成' : '未完成';
    };

onMounted(() => {
  fetchTodos();
});

</script>

<style scoped>
.todo-app {
  font-family: 'Arial', sans-serif;
  background-color: #fff;
  border-color: #fff;
  color: rgba(0, 0, 0, .87);
}

.todo-app .todo-list {
  list-style-type: none;
  padding: 0;
}

.todo-app .todo-list .todo-item {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  align-items: center;
  padding: 10px 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 16px;
}

.todo-app .todo-list .todo-item .todo-title {
  width: 40%;
}

.todo-app .todo-list .todo-item .todo-due-by {
  width: 34%;
}

.todo-app .todo-list .todo-item .todo-status {
  font-size: 15px;
  font-weight: 550;
  width: 7%;
}

.todo-app .todo-list .todo-item .todo-buttons {
  width: 7%;
  display: flex;
  justify-content: space-between;
}

.spacer {
  flex-grow: 1;
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

.button-completed-true,
.button-completed-false {
  width: 7%; 
  font-size: 15px;
  font-weight: 550;
  height: 24px; 
  border-radius: 15px; 
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.button-completed-true {
  background-color: #3cd1c2;
  color: white;
  
}

.button-completed-false {
  background-color: #ffaa2c;
  color: white;
}
</style>