<template>
  <div style="position: relative; height: 65vh; padding: 50px; width:90%">
    <el-table
      :data="pagedTableData"
      style="width: 100%;">

      <el-table-column
        label="ID"
        prop="ID">
      </el-table-column>

      <el-table-column
        label="Platform"
        prop="Platform">
      </el-table-column>
      <el-table-column
        label="Cycle"
        prop="Cycle">
      </el-table-column>
      <el-table-column
        label="Configuration"
        prop="Configuration">
      </el-table-column>
      <el-table-column
        label="Domain"
        prop="Domain">
      </el-table-column>
      <el-table-column
        label="Time"
        prop="Time">
      </el-table-column>
      
      <el-table-column
        label="Env_URL"
        prop="Env_URL">
        <template #default="scope">
          <a href="#" style="color: blue; text-decoration: underline;">{{ scope.row.Env_URL }}</a>
        </template>
      </el-table-column>
      <el-table-column
        label="Case_URL"
        prop="Case_URL">
        <template #default="scope">
          <a href="#" style="color: blue; text-decoration: underline;">{{ scope.row.Case_URL }}</a>
        </template>
      </el-table-column>
      <el-table-column
        label="Rebuild">
        <template #default="scope">
          <el-button type="text" @click="handleRebuild(scope.row)">Rebuild</el-button>
        </template>
      </el-table-column>

    </el-table>
      


     <div style="position: absolute; right: 20px; bottom: -60px;">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="tableData.length"
        :page-size="10"
        @current-change="handlePageChange">
      </el-pagination>
    </div>
    <div style="position: absolute; top: 10px; right: 20px;">
      <el-input
        v-model="search"
        size="medium"
        placeholder="输入关键字搜索"
        style="width: 350px;"
        @input="handleSearch">
      </el-input>
    </div>
  </div>
</template>

<style>
  .el-table .cell {
    white-space: nowrap;
  }
</style>

<script>
  export default {
    data() {
      return {
        tableData: [{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        }, {
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain15',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'1',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },{
          ID:'10  ',
          Platform:'Platform1',
          Cycle:'Cycle1',
          Configuration:'Configuration1',
          Domain:'Domain1',
          Time:'2019-09-09 12:00:00',
          Env_URL:'Env_URL1',
          Case_URL:'Case_URL1',
          Rebuild:'Rebuild'
        },],
        search: '',
        currentPage: 1
      }
    },
    computed: {
    pagedTableData() {
      const start = (this.currentPage - 1) * 10;
      const end = this.currentPage * 10;
      return this.filteredData.slice(start, end);
    },
     filteredData() {
      if (!this.search) {
        return this.tableData;
      }
      const searchLower = this.search.toLowerCase();
      return this.tableData.filter(data =>
        data.Platform.toLowerCase().includes(searchLower) ||
        data.Domain.toLowerCase().includes(searchLower)||
        data.ID.toLowerCase().includes(searchLower)
      );
    },
  },
  methods: {
    handleRebuild(row) {
      console.log('Rebuild clicked', row);
    },
    handlePageChange(newPage) {
      this.currentPage = newPage;
    },
    handleSearch() {
      this.currentPage = 1; // Reset to first page on search
    }
  },
  }
</script>


