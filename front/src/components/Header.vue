<template>
  <el-menu default-active="1" mode="horizontal" class="header-container">
    
    <el-menu-item index="0">
      <div class="menu-item-content">
        <img src="@/assets/intel-logo-blue-max.png" alt="Logo" class="menu-item-logo">
      </div>
    </el-menu-item>
    
    
    
    <el-menu-item index="1">
      <div class="menu-item-content">
        <router-link to="/Execution/Test_Case_Overview" class="menu-item-text">Execution</router-link>
      </div>
    </el-menu-item>
    <el-menu-item index="2">
      <router-link to="/History" class="menu-item-text">Execution History</router-link>
    </el-menu-item>
    <el-menu-item index="3">
      <router-link to="" class="menu-item-text">Server</router-link>
    </el-menu-item>
  </el-menu>
</template>

<script lang="ts" setup>
</script>

<style scoped>
.header-container {
  padding: 10px 20px; /* 添加内边距 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 可选：添加阴影效果 */
}

.menu-item-content {
  display: flex;
  align-items: center;
  justify-content: center;
}

.menu-item-logo {
  height: 50px; /* 减小图片大小 */
  margin-right: 10px;
}

.menu-item-text {
  font-size: 18px; /* 调整文本大小 */
  color: #333;
  font-weight: bold;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

.el-menu-item {
  display: flex;
  align-items: center;
  justify-content: center; /* 确保内容水平居中 */
  padding: 0 15px; /* 添加左右内边距 */
  margin-right: 10px; /* 添加右外边距 */
}

/* 选中状态的样式 */
.el-menu-item.is-active .menu-item-text {
  color: #f0efef;
}
.el-menu-item.is-active {
  background-color: #0161aa;
}

/* 悬停状态的样式 */
.el-menu-item:hover {
  background-color: #0161aa !important;
}

/* 确保菜单项不会被压缩到小于其内容的宽度 */
.el-menu-item {
  flex-shrink: 0;
}

/* 为菜单添加最小高度 */
.el-menu {
  min-height: 80px; /* 根据实际情况调整 */
}
</style>



