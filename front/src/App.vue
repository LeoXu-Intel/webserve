<template>
  <el-container class="home-container">
    <!-- 只有在非登录页面时显示 Header -->
    <el-header v-if="shouldShowHeader">
      <Header/>
    </el-header>
    <el-container> 
      <router-view></router-view>
    </el-container>
  </el-container>
</template>

<script lang="ts" setup>
import Header from './components/Header.vue'
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const shouldShowHeader = computed(() => route.path !== '/login')

const activeName = ref('first')

const options = {
  name: 'App',
  components: {
    Header
  }
}
</script>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
  padding: 0;
}

.home-container, .content-container {
  height: 100%;
}

/* 如果你的Header组件有固定高度，你可能需要为content-container设置一个top margin */
.content-container {
  margin-top: 60px; /* 假设Header高度为60px */
}
</style>