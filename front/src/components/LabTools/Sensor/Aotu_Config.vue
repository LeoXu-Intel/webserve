<template>
  <div style="display: flex; width: 100%; justify-content: center;">
    <el-steps :active="2" finish-status="success" simple style="width: 70%; margin-top: 5px;">
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
  
    <div class="checkbox-groups-container">
      <!-- 第一组多选框 -->
  <div class="checkbox-group">
    <el-input
      v-model="searchText1"
      placeholder="搜索..."
      clearable
      @clear="filterOptions1"
      @input="filterOptions1">
    </el-input>
    <el-scrollbar style="height: 300px;">
      Test_Suite
      <el-checkbox-group v-model="checkedGroup1">
        <el-checkbox
          v-for="item in filteredOptions1"
          :key="item.value"
          :label="item.label"
          border>
        </el-checkbox>
      </el-checkbox-group>
    </el-scrollbar>
  </div>

  <!-- 第二组多选框 -->
  <div class="checkbox-group">
    <el-input
      v-model="searchText2"
      placeholder="搜索..."
      clearable
      @clear="filterOptions2"
      @input="filterOptions2">
    </el-input>
    <el-scrollbar style="height: 300px;">
      Test_Case
      <el-checkbox-group v-model="checkedGroup2">
        <el-checkbox
          v-for="item in filteredOptions2"
          :key="item.value"
          :label="item.label"
          border>
        </el-checkbox>
      </el-checkbox-group>
    </el-scrollbar>
  </div>
    </div>
      
  <div class="buttons-container" style="display: flex; justify-content: flex-start; align-items: flex-end; position: absolute; bottom: 70; right: 0; margin: 10px;">
  <div class="button-container">
    <button @click="Back">Back</button>
  </div>
    <div class="button-container">
        <button @click="Build">Build</button>
      </div>
  </div>
  </template>
  
  <script>
  import { computed, ref } from 'vue'; // 确保 ref 被导入
  import { useStore } from 'vuex';
  export default {
    setup() {
      const store = useStore();
  
      // 使用 computed 来创建只读的计算属性，它们将从 Vuex store 中获取状态
      const selection1 = computed(() => store.state.selections.selection1);
      const selection2 = computed(() => store.state.selections.selection2);
      const selection3 = computed(() => store.state.selections.selection3);
      const selection4 = computed(() => store.state.selections.selection4);
  
      // 假设你有一个 action 来加载数据
      store.dispatch('loadSelections');
  
        // 搜索文本的响应式引用
      const searchText1 = ref('');
      const searchText2 = ref('');


      const options1=ref ([
            { label: 'Suit_Marker_Mapping_1', value: 'Suit_Marker_Mapping_1' },
            { label: 'Suit_Marker_Mapping_2', value: 'Suit_Marker_Mapping_2' },
            { label: 'Suit_Marker_Mapping_3', value: 'Suit_Marker_Mapping_3' },
            { label: 'Suit_Marker_Mapping_4', value: 'Suit_Marker_Mapping_4' },
            { label: 'Suit_Marker_Mapping_5', value: 'Suit_Marker_Mapping_5' },
            { label: 'Suit_Marker_Mapping_6', value: 'Suit_Marker_Mapping_6' },
            { label: 'Suit_Marker_Mapping_7', value: 'Suit_Marker_Mapping_7' },
            { label: 'Suit_Marker_Mapping_8', value: 'Suit_Marker_Mapping_8' },
            { label: 'Suit_Marker_Mapping_9', value: 'Suit_Marker_Mapping_9' },
            { label: 'Suit_Marker_Mapping_10', value: 'Suit_Marker_Mapping_10' },
            { label: 'Suit_Marker_Mapping_11', value: 'Suit_Marker_Mapping_11' },
            
            // ...更多选项
            ]);
      const options2=ref ([
            { label: 'Case_Marker_1', value: 'Case_Marker_1' },
            { label: 'Case_Marker_2', value: 'Case_Marker_2' },
            { label: 'Case_Marker_3', value: 'Case_Marker_3' },
            { label: 'Case_Marker_4', value: 'Case_Marker_4' },
            { label: 'Case_Marker_5', value: 'Case_Marker_5' },
            { label: 'Case_Marker_6', value: 'Case_Marker_6' },
            { label: 'Case_Marker_7', value: 'Case_Marker_7' },
            { label: 'Case_Marker_8', value: 'Case_Marker_8' },
            { label: 'Case_Marker_9', value: 'Case_Marker_9' },
            { label: 'Case_Marker_10', value: 'Case_Marker_10' },
            { label: 'Case_Marker_11', value: 'Case_Marker_11' },
            
            // ...更多选项
            ]);

     // 计算属性，用于根据搜索文本过滤选项
     const filteredOptions1 = computed(() => {
      if (!searchText1.value) {
        return options1.value;
      }
      return options1.value.filter(item =>
        item.label.toLowerCase().includes(searchText1.value.toLowerCase())
      );
    });

    const filteredOptions2 = computed(() => {
      if (!searchText2.value) {
        return options2.value;
      }
      return options2.value.filter(item =>
        item.label.toLowerCase().includes(searchText2.value.toLowerCase())
      );
    });

    // 默认选中的值
    const checkedGroup1 = ref(options1.value.map(item => item.value));
    const checkedGroup2 = ref(options2.value.map(item => item.value));

    return {
      selection1,
      selection2,
      selection3,
      selection4,
      searchText1,
      searchText2,
      filteredOptions1,
      filteredOptions2,
      checkedGroup1,
      checkedGroup2,
    };
  },
    methods: {
      search() {
        // 在这里执行搜索逻辑
        console.log('执行搜索', this.selection1, this.selection2, this.selection3, this.selection4);
      },
      build() {
        //this.$router.push('/LabTools/Sensor/Aotu_Config');
      },
    Back() {
        this.$router.push('/LabTools/Sensor/Env_Config');
    },
    },filterOptions1() {
      // 这个方法会在 searchText1 改变时被调用
      // 过滤 options1 数组并更新 filteredOptions1
      this.filteredOptions1 = this.options1.filter(item =>
        item.label.toLowerCase().includes(this.searchText1.toLowerCase())
      );
    },
    filterOptions2() {
      // 这个方法会在 searchText2 改变时被调用
      // 过滤 options2 数组并更新 filteredOptions2
      this.filteredOptions2 = this.options2.filter(item =>
        item.label.toLowerCase().includes(this.searchText2.toLowerCase())
      );
    },
    
  };
  </script>
  
  
  
  
  <style scoped>
  .checkbox-groups-container {
    display: flex;
    flex-direction: row;
    justify-content: center; /* 居中对齐 */
    padding: px; /* 容器内边距 */
    gap: 30px; /* 组间间隔 */
  
  }
  
  .checkbox-group {
    flex: 0 0 20%; /* 减少宽度，不允许多选框组伸缩 */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
    border-radius: 4px; /* 圆角边框 */
    overflow: hidden; /* 隐藏溢出的子元素 */
    height: 300px; /* 增加多选框组的高度 */
    border: #a2a2a2 2px solid;
  }
  
  .el-scrollbar {
    height: 100%; /* 使滚动条高度与父容器相同 */
    margin: 10px; /* 添加一些外边距 */
  }
  
  .el-checkbox-group {
    max-height: 100%; /* 使多选框组高度与父容器相同 */
    overflow-y: auto; /* 设置垂直滚动 */
    display: flex;
    flex-direction: column; /* 设置纵向排列 */
    padding: 10px; /* 组内边距 */
  }
  
  .el-checkbox {
    margin-bottom: 10px; /* 多选框之间的间距 */
    transition: background-color 0.3s; /* 添加背景颜色过渡效果 */
    max-width: 100%; /* 限制多选框的最大宽度 */
    white-space: nowrap; /* 防止文本换行 */
    overflow: hidden; /* 隐藏溢出的文本 */
    text-overflow: ellipsis; /* 显示省略号 */
  }
  
  /* 当多选框被hover时，改变背景颜色 */
  .el-checkbox:hover {
    background-color: #f5f5f5;
  }
  </style>
  
  
  
  
  
  <style>
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
  @import "vue-multiselect/dist/vue-multiselect.css";
  
  
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
  