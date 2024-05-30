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
        <label for="selection1">Platform:</label>
        <input id="selection1" :value="selection1" readonly>
      </div>
  
      <div class="input-group">
        <label for="selection2">Test_Cycle_Name:</label>
        <input id="selection2" :value="selection2" readonly>
      </div>
  
      <div class="input-group">
        <label for="selection3">Cycle_Config:</label>
        <input id="selection3" :value="selection3" readonly>
      </div>
  
      <div class="input-group">
        <label for="selection4">Test_Domain:</label>
        <el-select v-model="selection4" multiple placeholder="请选择" disabled>
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
              v-if="item.type === 'text'"
              :type="item.type"
              v-model="forms[tab.label][item.model]"
            />
            <el-select
              v-else-if="item.type === 'select'"
              v-model="forms[tab.label][item.model]"
              placeholder="请选择"
            >
              <el-option
                v-for="option in item.options"
                :key="option.value"
                :label="option.label"
                :value="option.value"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
  </div>
  
  <div class="buttons-container" style="display: flex; justify-content: flex-start; align-items: flex-end; position: absolute; bottom: 70; right: 0; margin: 0px;">
  <div class="button-container">
    <button @click="Back">Back</button>
  </div>
  <div class="button-container">
    <button @click="build">Build</button>
  </div>
</div>
  </template>
  
  
  <script>
  
  import { computed } from 'vue';
  import { useStore } from 'vuex';
  import configData from '@/assets/config.json';
  import { reactive } from 'vue';
  
  
  
  export default {
    setup() {
      const store = useStore();
  
      // 使用 computed 来创建只读的计算属性，它们将从 Vuex store 中获取状态
      const selection1 = computed(() => store.state.selections.selection1);
      const selection2 = computed(() => store.state.selections.selection2);
      const selection3 = computed(() => store.state.selections.selection3);
      const selection4 = computed(() => store.state.selections.selection4);
      const activeName = computed(() => store.state.activeTab); // 假设 activeTab 保存在 Vuex store 的状态中
      const combinedTabsConfig = computed(() => {
      // 始终包含"Basic"标签页的配置
      const defaultTabsConfig = configData.filter(tab => ["SUT1", "SUT2", "VM"].includes(tab.label));
      const otherTabsConfig = selection4.value.length === 0
        ? []
        : configData.filter(tab => selection4.value.includes(tab.label) && !["SUT1", "SUT2", "VM"].includes(tab.label));
      // 合并默认标签页和其他选中的标签页配置
      return [...defaultTabsConfig, ...otherTabsConfig];
    });

      const forms = reactive({}); // 为每个tab和formItem创建响应式属性
  
      // 初始化forms对象
      configData.forEach((tab) => {
        forms[tab.label] = {};
        tab.formItems.forEach((item) => {
          forms[tab.label][item.model] = item.defaultValue || '';
        });
      });
  
      // 定义build方法
      const build = () => {
        // 这里应该是你的构建逻辑
        console.log('Build function called');
        this.$router.push('/LabTools/Sensor/Aotu_Config');
      };
  
  
  
      // 返回响应式引用和函数...
      return {
        selection1,
        selection2,
        selection3,
        selection4,
        activeName,
        combinedTabsConfig,
        forms,
        build,
      };
    },
    methods: {
      
      build() {
        this.$router.push('/LabTools/Sensor/Aotu_Config');
      },
      Back() {
        this.$router.push('/LabTools/Sensor/Test_Case_Overview');
    },
    },
  };
  
  
  </script>
  
  
  <style>
  .buttons-container {
  display: flex;
  justify-content: space-between; /* 或者其他你想要的对齐方式 */
}
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
  
  
  