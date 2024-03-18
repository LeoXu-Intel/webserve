<template>
  <div class="folder-list">
    <h2>Purchase</h2>

    <ul>
      <li v-for="(folder, index) in folders" :key="index">
        <div class="folder-link" @click="openFile(folder.link)">
          <div class="folder-item">
            <div class="folder-icon">🔗📁</div>
            <div class="folder-info">{{ folder.info }}</div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      folders: [
        { info: 'Purchase', name: 'Purchase', link: 'file://10.8.214.64/qms2/1_Cross Secrion' },
        // 添加更多文件夹数据
      ],
    };
  },
  methods: {
    openFile(link) {
      // 调用异步方法
      this.showOpenFilePicker();
    },
    async showOpenFilePicker() {
      try {
        const fileHandle = await window.showOpenFilePicker();
        console.log('Selected file:', fileHandle);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.folder-list {
  max-width: 800px;
  margin: 20px auto;
  font-family: 'Arial', sans-serif;
}

h2 {
  text-align: center;
  color: #007BFF;
  font-size: 24px;
  margin-bottom: 20px;
}

ul {
  list-style: none;
  padding: 0;
}

.folder-item {
  border: 1px solid #ddd;
  padding: 15px;
  margin: 15px 0;
  border-radius: 10px;
  transition: background-color 0.3s ease;
  display: flex;
  align-items: center;
}

.folder-item:hover {
  background-color: #f0f0f0;
}

.folder-icon {
  font-size: 24px;
  margin-right: 15px;
}

.folder-info {
  font-size: 18px;
  color: #333;
}

.folder-link {
  text-decoration: none;
  color: #007BFF;
  cursor: pointer; /* 添加指针样式，表示可点击 */
}
</style>
