<template>
  <el-menu default-active="1" mode="horizontal" class="header-container">
    
    <el-menu-item index="0">
      <div class="menu-item-content">
        <img src="@/assets/intel-logo-blue-max.png" alt="Logo" class="menu-item-logo">
      </div>
    </el-menu-item>
    
    
    
    <el-menu-item index="1">
      <div class="menu-item-content">
        <router-link to="/LabTools/Sensor/Test_Case_Overview" class="menu-item-text">Execution</router-link>
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
.menu-item-content {
  display: flex;
  align-items: center;
  justify-content: center; /* 居中内容 */
  width: 100%; /* 填充整个菜单项 */
}

.menu-item-logo {
  height: 75px; /* 调整图片大小 */
  margin-right: 10px; /* 在图片和文本之间添加一些间隔 */
}

.menu-item-text {
  font-size: 25px; /* 调整文本大小 */
  color: #333; /* 调整文本颜色，根据需要更改 */
  font-weight: bold; /* 加粗文本 */
  text-decoration: none; /* 去掉下划线 */
  width: 130%; /* 填充整个菜单项 */
  height: 130%;
  display: flex; /* 使用 flex 布局 */
  align-items: center; /* 垂直居中文本 */
  justify-content: center; /* 水平居中文本 */

}

.el-menu-item {
  display: flex; 
  align-items: center;
  width: 14%; /* 根据内容自动调整宽度*/
}

.header-container {
  height: 130%;
}



/* 设置选中状态的文本颜色 */
.el-menu-item.is-active .menu-item-text {
  color: #f0efef; /* 设置选中状态下的文本颜色为白色 */
}
.el-menu-item.is-active {
  background-color: #0161aa; /* 设置选中状态下的文本颜色为白色 */
}
.el-menu-item:hover {
  background-color: #0161aa !important; /* 设置悬停时背景色为透明，并确保覆盖默认样式 */
}
</style>



