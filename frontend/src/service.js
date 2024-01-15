import axios from 'axios';

const apiBaseUrl = 'http://localhost:5000/api/todos';

export default {
  getTodos() {
    return axios.get(apiBaseUrl);
  },

  addTodo(todo) {
    return axios.post(apiBaseUrl, todo);
  },

  updateTodo(todoId, data) {
    return axios.put(`${apiBaseUrl}/${todoId}`, data);
  },

  deleteTodo(todoId) {
    return axios.delete(`${apiBaseUrl}/${todoId}`);
  },

  loginSubmit(data) {
    return axios.post(`${apiBaseUrl}/login`, data);
  }
};
