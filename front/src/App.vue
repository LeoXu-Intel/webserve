<template>
  <el-container class="home-container">
    <el-header>
      <Header/>
    </el-header>
    <el-container style="height: 100%"> 
      <!-- <el-aside width="250px">
        <router-view name="menu"></router-view>
      </el-aside>
      <el-main>
        <router-view name="main"></router-view>
      </el-main> -->
      <router-view></router-view>
    </el-container>
  </el-container>
</template>

<script lang="ts" setup>

import Header from '@/components/Header.vue'
import { ref } from 'vue'


const activeName = ref('first')

// export default {
//   name: 'App',
//   components:{
//     Menu,
//     Header
//   }
// }

const options = {
    name: 'App',
    components:{
      Header
    }
}

</script>

<style>
/* html,body,#app{ height:100%; margin: 0px; padding: 0px; } */

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center;
  color: #2c3e50; */
  height: 100%; 
}

.home-container{
    height: 100%;
}


 html,body {
  height: 100%;
  margin: 0px;
}

</style>
