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
        <label for="select1">Platform:</label>
        <select id="select1" v-model="selection1">
          <option value="option1">SP1</option>
          <option value="option2">SP2</option>
          <!-- 更多选项 -->
        </select>
      </div>

      <div class="input-group">
        <label for="select2">Test_Cycle_Name:</label>
        <select id="select2" v-model="selection2">
          <option value="option1">Test_Cycle_1</option>
          <option value="option2">Test_Cycle_2</option>
          <!-- 更多选项 -->
        </select>
      </div>

    </div>

    <div class="row">

      <div class="input-group">
        <label for="select3">Cycle_Config:</label>
        <select id="select3" v-model="selection3">
          <option value="option1">Cycle_Config_1</option>
          <option value="option2">Cycle_Config_2</option>
          <!-- 更多选项 -->
        </select>
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

  <div class="checkbox-groups-container">
    <!-- 第一组多选框 -->
    <div class="checkbox-group">
      <el-scrollbar style="height: 300px;">
        Test_Suite
        <el-checkbox-group v-model="checkedGroup1">
          <el-checkbox
            v-for="item in options1"
            :key="item.value"
            :label="item.label"
            border>
          </el-checkbox>
        </el-checkbox-group>
      </el-scrollbar>
    </div>
    <!-- 第二组多选框 -->
    <div class="checkbox-group">
      <el-scrollbar style="height: 300px;">
        Test_Case
        <el-checkbox-group v-model="checkedGroup2">
          <el-checkbox
            v-for="item in options2"
            :key="item.value"
            :label="item.label"
            border>
          </el-checkbox>
        </el-checkbox-group>
      </el-scrollbar>
    </div>
  </div>
    

  <div class="button-container">
      <button @click="Build">Build</button>
    </div>
</template>

<script>
import Multiselect from 'vue-multiselect';

export default {
  components: { Multiselect },
  created() {
    this.loadSelections();
  },
  data() {
    return {
      selection1: '',
      selection2: '',
      selection3: '',
      selection4: [],
      options: [{
          value: 'QAT',
          label: 'QAT'
        }, {
          value: 'DLB',
          label: 'DLB'
        }, {
          value: 'DSA',
          label: 'DSA'
        }, {
          value: 'Networking',
          label: 'Networking'
        }, {
          value: 'SRIOV',
          label: 'SRIOV'
        }],
        value1: [],
        value2: [],
       checkedGroup1: [],
      checkedGroup2: [],
      options1: [
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
      ],
      options2: [
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
      ],

    };
  },
  methods: {
    loadSelections() {
      // 假设你有一个 action 来加载数据
      this.$store.dispatch('loadSelections').then(() => {
        const selections = this.$store.state.selections;
        this.selection1 = selections.selection1 || '';
        this.selection2 = selections.selection2 || '';
        this.selection3 = selections.selection3 || '';
        this.selection4 = selections.selection4 || [];
      });
    },
    search() {
      // 在这里执行搜索逻辑
      console.log('执行搜索', this.selection1, this.selection2, this.selection3, this.selection4);
    }
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

.input-group select{
  padding: 0px;
  border: 2px solid #e6e6e6;
  border-radius: 4px;
  width: 100%; /* 选择框宽度调整为100% */
  font: 1em sans-serif;
  height: 33px;
  
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
