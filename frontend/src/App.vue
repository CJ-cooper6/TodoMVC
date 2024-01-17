<template>
    <div class="app">
       <!-- <router-link to="/">Login</router-link>
      <router-link to="/home">Home</router-link> -->
    <router-view></router-view>
    </div>
</template>

<script lang="js" setup>
  import Navbar from './components/Navbar.vue';
  import Auth from './views/Auth.vue';
</script>


<style>

</style>