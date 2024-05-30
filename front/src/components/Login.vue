<template>

  <div class="common-layout">
    
    <el-container class="container">    
    <el-header class="header">NPI-BKC Automation Console</el-header>      
      <el-main class="main">
        <el-card class="login-card">
          <el-form ref="loginForm" :model="loginForm" @submit.prevent="handleLogin">
            
            <h1 style="text-align: center; font-size: 2em;">Please Login in</h1>

            <el-form-item label="Username:" prop="username" class="bold-and-large">
                 <el-input v-model="loginForm.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="Password:" prop="password" class="bold-and-large">
                 <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
            </el-form-item>

            <el-form-item class="login-button-container">
              <el-button type="primary" style="width:20% " @click="handleLogin">Login</el-button>
            </el-form-item>

            

          </el-form>
        </el-card>
      </el-main>
    </el-container>
  </div>
</template>



<script>
export default {
  data() {
  return {
    loginForm: {
      username: '',
      password: '',
    },
  };
},

  methods: {
    async handleLogin() {
      try {
        // 发送登录请求到Django后端
        const response = await this.$axios.post('/api/login/', {
          username: this.loginForm.username,
          password: this.loginForm.password
        });
        // 登录成功，设置登录状态并导航到 /LabTools
        if (response.data.success) {
          localStorage.setItem('isUserLoggedIn', 'true');
          this.$router.push('/LabTools');
        } else {
          // 登录失败，显示错误消息
          alert('Incorrect username or password.');
        }
      } catch (error) {
        // 处理错误情况
        alert('Login failed. Please try again.');
      }
    },
},

};
</script>


<style scoped>
.bold-and-large {
  font-size: 1.9 em; /* 放大字体大小 */
  font-weight: bold; 
}
.common-layout {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%; /* 确保占满父容器的高度 */
  background-color: #0161aa; /* 蓝色背景 */
  width: 100%;
}

.container {
  width: 100%;
  max-width: 100%; /* 或者你希望的最大宽度 */
}

.header {
 width: 100%;
 position: absolute; /* 绝对定位 */
  top: 0; /* 距离顶部 0px */
  left: 0; /* 距离左侧 0px */
  font-size: 50px; /* 标题字体大小，根据需要调整 */
  color: #fff;
  margin: 0px; /* 添加一些边距，根据需要调整 */
  line-height: normal; /* 重置行高 */
  background: linear-gradient(to bottom, #0074B9, #003458);
  height: 13%;
  text-align: start;
}

.main {
  display: flex;
  justify-content: center;
}

.login-card {
  width: 35%;
  padding: 20px;
}

.el-form-item {
  margin-bottom: 24px; /* 增加表单项之间的间距 */
}

.login-button-container {
  display: flex;
  justify-content: center; /* 居中按钮 */
  padding: 0; /* 如果需要，移除内边距 */
}


</style>



