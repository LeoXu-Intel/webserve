<!-- Dashboard.vue -->
<template>
    <div>
      <h2>Dashboard</h2>
      <p>Welcome to the dashboard!</p>
    </div>
  </template>
  
  <script>
  export default {
    // 如果需要登录才能访问，则设置metaInfo
    metaInfo: {
      requiresAuth: true
    }
  }
  </script>
  