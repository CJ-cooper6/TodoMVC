import { createStore } from 'vuex';

export default createStore({

  state: {
    add_todo_popup: false,
  },

  mutations: {
    toggleAddTodoPopup(state) {
        state.add_todo_popup = !state.add_todo_popup
        console.log(state.add_todo_popup)
      },
  },

  actions: {
  },
  getters: {
  
  },
});