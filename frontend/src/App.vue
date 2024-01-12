<template>
    <div class="app">
        <h1>TodoMVC</h1>
        <TodoList />
    </div>
</template>

<script lang="js">
  import TodoList from './components/TodoList.vue';

    export default{
        name:'APP',
        components: {
            TodoList,
        },
    }
</script>


<style>

</style>