<template>
  <el-container style="height: 100vh;">
    <!-- 左侧部分：根据 SQL 语句查询 -->
    <el-aside style="width: 50%; padding: 20px; overflow-y: auto;">
      <el-form label-position="top">
        <el-form-item label="SQL 查询">
          <el-row :gutter="22">
            <el-col :span="22">
              <el-input
                type="textarea"
                v-model="sqlQuery"
                placeholder="请输入 SQL 语句"
                :autosize="{ minRows: 3, maxRows: 6 }"
              ></el-input>
            </el-col>
            <el-col :span="2">
              <el-button type="primary" @click="executeSqlQuery">查询</el-button>
            </el-col>
          </el-row>
        </el-form-item>
        <!-- SQL 查询结果展示区域 -->
        <div v-if="sqlQueryResult" class="query-result">
          <h3>SQL 查询结果:</h3>
          <pre>{{ sqlQueryResult }}</pre>
        </div>
      </el-form>
    </el-aside>

    <el-divider direction="vertical"></el-divider>

    <!-- 右侧部分：根据 ID 查询 -->
    <el-aside style="width: 50%; padding: 20px; overflow-y: auto;">
      <el-form label-position="top">
        <el-form-item label="ID 查询">
          <el-row :gutter="20">
            <el-col :span="21">
              <el-input
                v-model="searchId"
                placeholder="请输入 ID"
              ></el-input>
            </el-col>
            <el-col :span="3">
              <el-button type="primary" @click="searchById">查询</el-button>
            </el-col>
          </el-row>
        </el-form-item>
        <!-- ID 查询结果展示区域 -->
        <div v-if="idSearchResult" class="query-result">
          <h3>ID 查询结果:</h3>
          <pre>{{ idSearchResult }}</pre>
        </div>
      </el-form>
    </el-aside>
  </el-container>
</template>

<script>
import { defineComponent, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "SplitView",
  setup() {
    const sqlQuery = ref('');
    const searchId = ref('');
    const sqlQueryResult = ref(null); // 存储 SQL 查询结果
    const idSearchResult = ref(null); // 存储 ID 查询结果

    const executeSqlQuery = async () => {
      if (sqlQuery.value.trim() === '') {
        alert('请输入 SQL 查询语句。');
        return;
      }
      try {
        const response = await axios.post('/api/executeSql', { sql: sqlQuery.value });
        sqlQueryResult.value = response.data; // 假设后端返回的数据在 response.data 中
      } catch (error) {
        console.error('SQL 查询错误:', error);
        sqlQueryResult.value = '查询出错，请检查 SQL 语句和网络连接。';
      }
    };

    const searchById = async () => {
      if (searchId.value.trim() === '') {
        alert('请输入 ID。');
        return;
      }
      try {
        const response = await axios.get(`/api/searchById/${encodeURIComponent(searchId.value)}`);
        idSearchResult.value = response.data; // 假设后端返回的数据在 response.data 中
      } catch (error) {
        console.error('ID 查询错误:', error);
        idSearchResult.value = '查询出错，请检查 ID 和网络连接。';
      }
    };

    return {
      sqlQuery,
      searchId,
      sqlQueryResult,
      idSearchResult,
      executeSqlQuery,
      searchById
    };
  }
});
</script>
<style scoped>
.el-aside {
  padding: 20px;
  border: 1px solid #ebeef5;
  height: calc(100vh - 40px); /* 调整高度以适应视口 */
  overflow-y: auto; /* 如果内容过多，允许滚动 */
}
</style>
