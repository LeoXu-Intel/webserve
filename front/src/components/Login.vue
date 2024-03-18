<!-- Login.vue -->
<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <label for="username">Username:</label>
        <input type="text" v-model="username" required>
  
        <label for="password">Password:</label>
        <input type="password" v-model="password" required>
  
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
        login() {
  // 模拟登录逻辑，实际应用中应该发送请求到后端进行验证
  if (this.username === 'xa' && this.password === '123') {
    // 登录成功，设置 isAuthenticated 状态
    this.$store.commit('setAuthentication', true);

    // 在导航守卫的 next 回调中进行跳转
    this.$router.push({
      path: this.$route.query.redirect || 'LabTools/ASIC/UpdateReference',
      query: { redirect: null } // 清空 redirect 查询参数
    });
  } else {
    alert('Invalid username or password');
  }
}


    }
  }
  </script>
  