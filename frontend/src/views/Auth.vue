
<template>
<div class="login-body">
<div class="login-container">
    <h2>Login</h2>
    <div>
        <label for="username">用户名:</label>
        <input v-model="username"/>
        <label for="password">密码:</label>
        <input v-model="password"/>
        <button @click="login">登录</button>
    </div>
</div>
</div>
</template>

<script lang="js" setup>
import { ref, onMounted } from 'vue';
import TodoService from '../service';
    const username = ref('');
    const password = ref('');

const login = () => {
    console.log(username)
    console.log(password)
    TodoService.loginSubmit({
             username: username.value,
             password: password.value
        })
          .then(() => {
            newTodo.value = '';
            fetchTodos();
          })
          .catch(error => {
            console.error('登录失败:', error);
          }); 
};
</script>

<style>
        .login-body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }

        .login-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        .login-container input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
        }

        .login-container button {
            width: 100%;
            padding: 10px;
            background-color: #4caf50;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .login-container button:hover {
            background-color: #45a049;
        }
    </style>