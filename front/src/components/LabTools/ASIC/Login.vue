<!-- Login.vue -->
<template>
  <div class="login-container">
    <h2>ASIC Report Reference Login</h2>
    <form @submit.prevent="login" class="login-form">
      <label for="username">Username:</label>
      <input type="text" v-model="username" required class="input-field">
  
      <label for="password">Password:</label>
      <input type="password" v-model="password" required class="input-field">
  
      <button type="submit" class="login-button">Login</button>
    </form>
  </div>
</template>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #333;
}

.login-form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 8px;
  color: #555;
}

.input-field {
  padding: 8px;
  margin-bottom: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.login-button {
  padding: 10px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #0056b3;
}
</style>

  
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
  if (this.username === 'QEC' && this.password === '123') {
    // 登录成功，设置 isAuthenticated 状态
    this.$store.commit('setAuthentication', true);

    // 在导航守卫的 next 回调中进行跳转
    this.$router.push({
      path: this.$route.query.redirect || 'UpdateReference',
      query: { redirect: null } // 清空 redirect 查询参数
    });
  } else {
    alert('Invalid username or password');
  }
}


    }
  }
  </script>
  