// vue.config.js
module.exports = {
    chainWebpack: (config) => {
    const svgRule = config.module.rule('svg');

    svgRule.uses.clear();

    svgRule
      .use('vue-svg-loader')
      .loader('vue-svg-loader');
  },
    publicPath: process.env.NODE_ENV === 'production'
        ? '/production-sub-path/'
        : '/',

    devServer: {
        proxy: {
            '/api': {
                target: 'http://172.18.0.1:8080',
                ws: true,
                changeOrigin: true
            }
        }
    }
}
