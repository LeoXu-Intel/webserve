<template>
  <div style="display: flex; width: 100%; justify-content: center;">
    <el-steps  finish-status="success" simple style="width: 70%; margin-top: 5px;">
      <el-step title="Test Case Overview"></el-step>
      <el-step title="Environment Configuration"></el-step>
      <el-step title="Automation Configuration"></el-step>
    </el-steps>
  </div>
  
    <div class="search-form">
      <div class="row">
  
        <div class="input-group">
          <!-- Jenkins API  NPX Cycle中 -->
          <label for="selection1">Platform:</label>
          <el-select
            v-model="selection1Model"
            :loading="loading.selection1"
            @focus="fetchSelection1Options"
            clearable
            placeholder="请选择">
            <el-option
              v-for="item in options.selection1"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>
          <!--  https://hsdes.intel.com/appstore/community_legacy/#/1201583113?queryId=14012520543 owner team:PAIV.BKC title:npx -->
        <div class="input-group">
          <label for="selection2">Test_Cycle_Name:</label>
          <el-select
            v-model="selection2Model"
            :loading="loading.selection2"
            @focus="fetchSelection2Options"
            clearable
            placeholder="请选择"
            >
            <el-option
              v-for="item in options.selection2"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>
  
      </div>
  
      <div class="row">
  <!-- title = npx owner_team=SPIV_BKC  拿到title 然后走test case 那个界面中的test_cyccle，groupby configuration 拿到configuration -->
        <div class="input-group">
          <label for="selection3">Cycle_Config:</label>
          <el-select
            v-model="selection3Model"
            :loading="loading.selection3"
            @focus="fetchSelection3Options"
            clearable
            placeholder="请选择">
            <el-option
              v-for="item in options.selection3"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>
  <!-- 走tc中patant id 在拿到domain_detail -->
        <div class="input-group">
          <label for="selection4">Test_Domain:</label>
          <el-select id="selection4" v-model="selection4Model" multiple placeholder="请选择" >
            <el-option
              v-for="item in options.selection4"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>
      </div>
      
      <div class="row button-row">
         <el-button type="primary" :loading="searching" @click="Search">Search</el-button>
      </div>
  
    </div>
  
    

    <div style="display: flex; justify-content: right; margin-bottom: 10px; margin-right: 10%;">
      <el-input
        placeholder="Search table..."
        v-model="searchQuery"
        @input="filterTable"
        style="width: 25%;">
      </el-input>
    </div>

     <!-- 查询结果列表 -->
     <div style="display: flex; justify-content: center; align-items: center; margin-top: 0px;">
       
      
      <el-table
        :data="filteredTableData"
        height="300"
        style="width:80%"
        :row-class-name="tableRowClassName"
        :default-sort="{prop: 'ID', order: 'descending'}"
      >
      <el-table-column
        prop="ID"
        label="ID"
        sortable
        width="200%">
      </el-table-column>
      <el-table-column
        prop="Title"
        label="Title"
        sortable
        width="310%">
      </el-table-column>
      <el-table-column
        prop="Domain_Detail"
        label="DomainDetail"
        sortable
        width="150%">
      </el-table-column>
      <el-table-column
        prop="Automation_Status"
        label="AutomationStatus"
        sortable
        width="180%">
      </el-table-column>
      <el-table-column
        prop="Commendline"
        label="Commendline"
        sortable
        width="300%">
      </el-table-column>
    </el-table>
     </div>

     <el-row type="flex" justify="space-between" align="middle" style="margin-top: 10px; width: 80%; margin-left: auto; margin-right: auto;">
  <el-col :span="12">
    <div style="padding-left: 20px;">
      <span>Total Records: {{ filteredTableData.length }}</span>
    </div>
  </el-col>
  <div class="button-container">
      <button @click="navigateToOtherPage">Next</button>
    </div>
</el-row>
      
    
  
  </template>
  
  
  
  <script>
  import { mapState, mapMutations } from 'vuex';
  import axios from 'axios';
  export default {
    created() {
        this.filteredTableData = this.tableData;
      },
    data() {
      return {
        hasSearched: false, // 添加这个新属性
        searching: false,
        loading: {
          selection1: false,
          selection2: false,
          selection3: false,
        },
        loaded: {
          selection1: false,
          selection2: false,
          selection3: false,
        },

        options: {
          selection1: [],
          selection2: [],
          selection3: [],
          selection4: [
            { label: 'AI', value: 'AI' },
            { label: 'BMSM', value: 'BMSM' },
            { label: 'DLB', value: 'DLB' },
            { label: 'DPDK', value: 'DPDK' },
            { label: 'DSA', value: 'DSA' },
            { label: 'FlexRAN', value: 'FlexRAN' },
            { label: 'Graphics', value: 'Graphics' },
            { label: 'Media', value: 'Media' },
            { label: 'Networking', value: 'Networking' },
            { label: 'PCIE', value: 'PCIE' },
            { label: 'Platform', value: 'Platform' },
            { label: 'QAT', value: 'QAT' },
            { label: 'RDT', value: 'RDT' },
            { label: 'SGX', value: 'SGX' },
            { label: 'SRIOV', value: 'SRIOV' },
            { label: 'SST-BF', value: 'SST-BF' },
            { label: 'SST-CP', value: 'SST-CP' },
            { label: 'TDX', value: 'TDX' },
            { label: 'vHOST', value: 'vHOST' },
            { label: 'VT-x', value: 'VT-x' },
          ]
        },
        value1: [],
        value2: [],
  
        tableData: [],
        searchQuery: '', // 用于存储搜索关键词
        filteredTableData: [], // 用于存储过滤后的表格数据
      };
    },
    watch: {
      selection2Model(newValue, oldValue) {
        if (newValue !== oldValue) {
          // 清空 CycleConfig 下拉框的值
          this.selection3Model = '';
          // 重置 loaded 状态，以便下次点击时重新加载选项
          this.loaded.selection3 = false;
        }
      },
  //   // 监听 selection2Model 的变化
  //   selection2Model(newValue, oldValue) {
  //     // 当 selection2Model 有内容且与旧值不同时，刷新表格
  //     if (newValue && newValue !== oldValue) {
  //       this.refreshTable();
  //     }
  //   },
  //   // 监听 selection4Model 的变化
  //   selection4Model(newValue, oldValue) {
  //     // 当 selection4Model 有内容且与旧值不同时，刷新表格
  //     if (newValue && JSON.stringify(newValue) !== JSON.stringify(oldValue)) {
  //       this.refreshTable();
  //     }
  //   }
  },
    computed: {
      ...mapState({
        selection1: state => state.selections.selection1,
        selection2: state => state.selections.selection2,
        selection3: state => state.selections.selection3,
        selection4: state => state.selections.selection4,
      }),
      // 提供 getter 和 setter 的计算属性
      selection1Model: {
        get() {
          return this.selection1;
        },
        set(value) {
          this.setSelection({ key: 'selection1', value });
        }
      },
      selection2Model: {
        get() {
          return this.selection2;
        },
        set(value) {
          this.setSelection({ key: 'selection2', value });
        }
      },
      selection3Model: {
        get() {
          return this.selection3;
        },
        set(value) {
          this.setSelection({ key: 'selection3', value });
        }
      },
      selection4Model: {
        get() {
          return this.selection4;
        },
        set(value) {
          this.setSelection({ key: 'selection4', value });
        }
      },
      filteredData() {
      const searchQuery = this.searchQuery.trim().toLowerCase();
      if (!searchQuery) {
        return this.tableData; // 如果搜索关键词为空，返回原始数据
      }
      return this.tableData.filter(row => {
        // 这里假设您想要在所有列中搜索
        // 如果您只想在特定列中搜索，请调整下面的代码
        return Object.values(row).some(value =>
          String(value).toLowerCase().includes(searchQuery)
        );
      });
    }
    },
    
  
    methods: {
      ...mapMutations({
        setSelection: 'setSelection'
      }),
      logChange(fieldName, value) {
        this.setSelection({ key: fieldName, value });
      },
      navigateToOtherPage() {
        if (!this.hasSearched) {
          // 如果没有执行过搜索，显示提示框
          this.$message({
            message: 'Please perform a search before proceeding to the next page.',
            type: 'warning'
          });
        } else {
          // 如果已经执行过搜索，跳转到下一个页面
          this.$router.push('/Execution/Env_Config');
        }
      },

      tableRowClassName({ rowIndex }) {
        return rowIndex === 0 ? 'first-row' : '';
      },
      fetchSelection1Options() {
        if (!this.loaded.selection1) {
          this.loading.selection1 = true;
          axios.get('/SearchPlatform')
            .then(response => {
              this.options.selection1 = response.data;
              this.loading.selection1 = false;
              this.loaded.selection1 = true; // 设置加载标志为true
            })
            .catch(error => {
              console.error('Error fetching selection1 options:', error);
              this.loading.selection1 = false;
            });
        }
      },
      fetchSelection2Options() {
        if (!this.loaded.selection2) {
          this.loading.selection2 = true;
          axios.get('/SearchTestCycle')
            .then(response => {
              this.options.selection2 = response.data;
              this.loading.selection2 = false;
              this.loaded.selection2 = true; // 设置加载标志为true
              
            })
            .catch(error => {
              console.error('Error fetching selection2 options:', error);
              this.loading.selection2 = false;
            });
        }
      },
      fetchSelection3Options() {
          // 如果已经加载过，且 selection2Model 为空，则不再加载
          if (this.loaded.selection3 && this.selection2Model) {
            return;
          }
          this.loading.selection3 = true;
          const params = {
            testCycleName: this.selection2Model
          };
          axios.get('/SearchCycleConfig', { params })
            .then(response => {
              this.options.selection3 = response.data;
              this.loading.selection3 = false;
              this.loaded.selection3 = true; // 设置加载标志为true
            })
            .catch(error => {
              console.error('Error fetching selection3 options:', error);
              this.loading.selection3 = false;
            });
        },
      refreshTable() {
        // 这里调用您的 Search 方法来刷新表格
        this.Search();
      },
      filterTable() {
        this.filteredTableData = this.filteredData;
      },
      Search() {
          if (!this.selection1Model || !this.selection2Model) {
            this.$message({
              message: 'Platform and Test_Cycle_Name cannot be empty.',
              type: 'error'
            });
            return; // 如果任一字段为空，显示提示并退出方法
          }
          this.searching = true; // 在请求开始前设置为 true
          const params = {
            testCycleName: this.selection2Model,
            cycleConfig: this.selection3Model,
            testDomain: this.selection4Model
          };
          axios.get('/SearchTestCase', { params })
            .then(response => {
              // 假设后端返回的数据是一个数组，每个元素都是一个对象
              this.tableData = response.data.map(item => ({
                ID: item.ID,
                Title: item.Title,
                Domain_Detail: item.Domain_Detail,
                Automation_Status: item.Aotumation_Status,
                Commendline: item.Commendline,
                
              }));
              this.filterTable();
              this.hasSearched = true;
            })
            .catch(error => {
              console.error('Error fetching tableData:', error);
            })
            .finally(() => {
              this.searching = false; // 在请求结束后设置为 false
            });
        },

    },
  };
  </script>
  
  <style>
  .el-table__header-wrapper tr th {
    background-color: #0056b3 !important; /* 使用 !important 来确保样式的优先级 */
    color: white; /* 可以设置字体颜色为白色，如果需要的话 */
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
    margin-top: 0px; /* 增加按钮与上方元素的间距 */
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
  