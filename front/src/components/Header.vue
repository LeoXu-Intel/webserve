<template>
    <el-menu
        default-active="1"
        mode="horizontal"
    >
        
        <el-menu-item index="1" >
          <router-link to="/LabTools">Header1</router-link>
        </el-menu-item>
        <el-menu-item index="2">
          <router-link to="/ManagementSystem">Header2</router-link>
        </el-menu-item>
        <el-menu-item index="3">
          <router-link to="/GeneralTools">Header3</router-link>
        </el-menu-item>
    </el-menu>
</template>
  
<script lang="ts" setup>
</script>
  