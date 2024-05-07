module.exports = {
    configureWebpack: {
      resolve: {
        alias: {
          '@': require('path').resolve(__dirname, 'src'), // 设置 '@' 别名到 'src' 目录
        },
      },
    },
    publicPath: '/', // 设置静态资源的基础路径为根目录
    lintOnSave: false, // 关闭eslint校验
    outputDir: process.env.outputDir || 'dist', // 打包生成目录，默认为 'dist'
  };
  