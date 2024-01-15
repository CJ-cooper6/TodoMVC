<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        {{ todo.title }}
        <button @click="editTodo(todo.id)">编辑</button>
        <button @click="deleteTodo(todo.id)">删除</button>
      </li>
    </ul>
    <div>
      <input v-model="newTodo" placeholder="New Todo" />
      <button @click="addTodo">添加</button>
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
