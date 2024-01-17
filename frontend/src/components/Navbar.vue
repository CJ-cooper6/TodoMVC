<template>
    <div class="wrapper">
    <div class="sidebar">
        <h2>TODO</h2>
        <ul>
            <li>计划列表</li>
            <li>个人中心</li>
        </ul>
    </div>
    <div class="main_content">
        <div class="header">
            <!-- <div>
                <span>Out</span>
                <ArrowRightOutlined />
            </div> -->
        </div>

        <div class="main">
            <TodoList />
        </div>

    </div>
</div>
  </template>
  <script lang="js" setup>
   import TodoList from './TodoList.vue';
  import { ref } from 'vue';
  import {
    ArrowRightOutlined
} from '@ant-design/icons-vue';
  </script>
  <style>
.wrapper .sidebar{
    width: 250px;
    height: 100%;
    background-color: #4b4276;
    padding: 30px 0px;
    position: fixed;
}

.wrapper .sidebar h2{
    color: #fff;
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 30px;
}


.wrapper .sidebar ul li{
    color: #fff;
    padding: 15px;
    border-bottom: 1px solid #bdb8d7;
    border-bottom: 1px solid rgba(0, 0, 0,0.05);
    border-top: 1px solid rgba(255, 255, 255,0.05);
}

.wrapper .sidebar ul li:hover{
    background-color: #594f8d;
}


.wrapper .sidebar ul li a{
    color: #bdb8d7;
    display: block;
}

.wrapper .sidebar ul li:hover a{
    color: #fff;
}

.wrapper .sidebar ul li a .fas{
    width: 25px;
}
.wrapper .main_content{
    width: 100%;
    margin-left: 250px;
}
.wrapper .main_content .main{
    margin-top: 50px;
    width: 100%;
    display: flex;
    justify-content: center;
}
.wrapper .main_content .header{
    padding: 41px;
    background: #ffffff;
    font-size:30px;
    color: #535050;
}
  </style>
  