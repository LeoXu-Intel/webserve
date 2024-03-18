<template>
    <el-aside width="250px">
        <!-- <Menu/> -->
        <router-view name="menu"></router-view>
    </el-aside>
    <el-main>
        <router-view name="main"></router-view>
    </el-main>
</template>
