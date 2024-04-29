<template>
<div style="display: flex; width: 100%; justify-content: center;">
  <el-steps :active="1" finish-status="success" simple style="width: 70%; margin-top: 5px;">
    <el-step title="Test Case Overview"></el-step>
    <el-step title="Environment Configuration"></el-step>
    <el-step title="Aotumation Configuration"></el-step>
  </el-steps>
</div>

  <div class="search-form">
    <div class="row">

      <div class="input-group">
        <label for="input1">Platform:</label>
        <input id="input1" v-model="selection1" readonly>
      </div>

      <div class="input-group">
        <label for="input2">Test_Cycle_Name:</label>
        <input id="input2" v-model="selection2" readonly>
      </div>

      <div class="input-group">
        <label for="input3">Cycle_Config:</label>
        <input id="input3" v-model="selection3" readonly>
      </div>


      <div class="input-group">
        <label for="select4">Test_Domain:</label>
          <el-select v-model="value1" multiple placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
      </div>

    </div>
  </div>

    


   <div class="tabs-container">
    <el-tabs v-model="activeName" type="card">
  <el-tab-pane
    v-for="tab in combinedTabsConfig"
    :key="tab.label"
    :label="tab.label"
    :name="tab.label"
  >
    <el-form label-position="top">
      <el-form-item
        v-for="item in tab.formItems"
        :key="item.model"
        :label="item.label"
      >
        <el-input
          :type="item.type"
          v-model="forms[tab.label][item.model]"
        />
      </el-form-item>
    </el-form>
  </el-tab-pane>
</el-tabs>
  </div>

  <div class="button-container">
      <button @click="build">Build</button>
    </div>
</template>


<script>

import { useRoute } from 'vue-router';
import { ref, reactive, onMounted, watch } from 'vue';
import configData from '@/assets/config.json';

export default {
  setup() {
    const route = useRoute();
    const selection1 = ref('');
    const selection2 = ref('');
    const selection3 = ref('');
    const value1 = ref([]); // 使用value1而不是selection4
    const activeName = ref('first');
    const combinedTabsConfig = ref(configData); // 这里应该是你的标签页配置数组
    const forms = reactive({});

    // 初始化forms对象，为每个tab和formItem创建响应式属性
    const initializeForms = (config) => {
      const formsData = {};
      config.forEach((tab) => {
        formsData[tab.label] = {};
        tab.formItems.forEach((item) => {
          formsData[tab.label][item.model] = '';
        });
      });
      return formsData;
    };

    // 使用初始化函数设置forms的初始值
    Object.keys(initializeForms(configData)).forEach(key => {
      forms[key] = initializeForms(configData)[key];
    });

    // 更新表单的方法
    const updateForms = () => {
      // 根据value1中的选择更新forms对象
      value1.value.forEach((selectedTabLabel) => {
        const tabConfig = configData.find(tab => tab.label === selectedTabLabel);
        if (tabConfig) {
          tabConfig.formItems.forEach((item) => {
            if (forms[selectedTabLabel]) {
              forms[selectedTabLabel][item.model] = item.label || '';
            }
          });
        }
      });
    };

    watch(value1, updateForms, { immediate: true });

      // 在组件挂载后获取路由查询参数并赋值
    onMounted(() => {
      selection1.value = route.query.selection1 || '';
      selection2.value = route.query.selection2 || '';
      selection3.value = route.query.selection3 || '';
      try {
        value1.value = JSON.parse(route.query.selection4 || '[]');
      } catch (e) {
        value1.value = [];
      }
    });

    // 定义build方法
    const build = () => {
      // 这里应该是你的构建逻辑
      console.log('Build function called');
    };


    // 返回响应式引用和函数...
    return {
      selection1,
      selection2,
      selection3,
      value1, // 返回value1
      activeName,
      combinedTabsConfig,
      forms, // 返回forms对象
      build, // 返回build函数
    };
  }
};


</script>


<style>
.tabs-container {
  max-width: 600px; /* 最大宽度，宽度可以根据内容自动调整 */
  min-height: 400px; /* 最小高度，高度可以根据内容自动调整 */
  margin: 20px auto; /* 上下边距和自动左右边距 */
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  border-radius: 4px; /* 圆角边框 */
  border-color: #000000;
  background-color: #00000010; /* 设置背景颜色为浅灰色 */
  padding: 20px; /* 内边距 */
  font-size: 1em; /* 字体大小 */
  font-family: sans-serif; /* 字体家族 */
  color: #000000; /* 字体颜色设置为黑色 */
  font-weight: bold; /* 字体加粗 */
  
}

/* 选中的选项卡样式 */
.tabs-container .el-tabs__item.is-active {
  background-color: #409EFF; /* 蓝色背景 */
  color: white; /* 白色文字 */
  font-family: sans-serif; /* 字体家族 */
  color: #000000; /* 字体颜色设置为黑色 */
  font-weight: bold; /* 字体加粗 */
}

/* 未选中的选项卡样式 */
.tabs-container .el-tabs__item {
  background-color: white; /* 白色背景 */
  color: #606266; /* 文字颜色 */
  border-color: #dcdfe6; /* 边框颜色 */
  font-family: sans-serif; /* 字体家族 */
  color: #000000; /* 字体颜色设置为黑色 */
  font-weight: bold; /* 字体加粗 */
}

.el-form-item {
  margin-bottom: 20px; /* 增加表单项之间的间距 */
  
}

.el-input {
  width: 100%; /* 输入框宽度设置为100% */
  
}

.button-container {
  display: flex;
  justify-content: flex-end; /* 将按钮对齐到右边 */
  margin-right: 85px; /* 右边距20px */
}

.button-container button {
  margin-top: 1%;
  padding: 10px 35px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 15px;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.button-container button:hover {
  background-color: #0056b3;
}
</style>


<style scoped>

.search-form {
  max-width: 90%;
  margin: 10px auto;
  padding: 10px;
  border: 3px solid #f7f6f6;
  border-radius: 10px;
  background: #ffffff;
  
}

.row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.input-group {
  display: flex;
  flex-direction: column;
  margin: 0 20px;
  width: calc(50% - 20px); /* 减去间距的一半 */
  
}

.input-group label {
  margin-bottom: 10px;
  font-weight: bold;

}

.input-group input{
  padding: 0px;
  border: 2px solid #e6e6e6;
  border-radius: 4px;
  width: 100%; /* 选择框宽度调整为100% */
  font: 1em sans-serif;
  height: 33px;
  background: #c9c8c8;
  
}

.button-row {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px; /* 增加按钮与上方元素的间距 */
}

.row button {
  margin-top:1% ;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 15px;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.row button:hover {
  background-color: #0056b3;
}



</style>


