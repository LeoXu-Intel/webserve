<template>
  <div class="folder-list">
    <h2>文件夹列表</h2>

    <!-- 输入框和添加按钮 -->
    <div class="add-folder">
      <input v-model="newFolderName" placeholder="文件夹名称" />
      <input v-model="newFolderLink" placeholder="链接" />
      <button @click="addFolder">添加</button>
    </div>

    <ul>
      <li v-for="(folder, index) in folders" :key="index">
        <a :href="folder.link" target="_blank">
          <div class="folder-item">
            <div class="folder-info">{{ folder.info }}</div>
          </div>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      folders: [
        { info: '文件夹1 - 链接1', name: '文件夹1', link: '链接1' },
        { info: '文件夹2 - 链接2', name: '文件夹2', link: '链接2' },
        // 添加更多文件夹数据
      ],
      newFolderName: '',
      newFolderLink: '',
    };
  },
  methods: {
    addFolder() {
      if (this.newFolderName && this.newFolderLink) {
        const newFolder = {
          info: `${this.newFolderName} - ${this.newFolderLink}`,
          name: this.newFolderName,
          link: this.newFolderLink,
        };
        this.folders.push(newFolder);
        // 清空输入框
        this.newFolderName = '';
        this.newFolderLink = '';
      }
    },
  },
};
</script>

<style scoped>
.folder-list {
  max-width: 600px;
  margin: 20px auto;
  font-family: 'Arial', sans-serif;
}

h2 {
  text-align: center;
  color: #333;
}

.add-folder {
  display: flex;
  margin-bottom: 20px;
}

input {
  flex: 1;
  padding: 10px;
  margin-right: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  padding: 10px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

ul {
  list-style: none;
  padding: 0;
}

.folder-item {
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px 0;
  border-radius: 8px;
  transition: background-color 0.3s ease;
}

.folder-item:hover {
  background-color: #f5f5f5;
}

.folder-info {
  font-size: 16px;
  color: #333;
}

a {
  text-decoration: none;
  color: inherit;
}
</style>
