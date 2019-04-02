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
                target: 'http://172.20.0.4:8000',
                ws: true,
                changeOrigin: true
            }
        },
        watchOptions: {
            ignored: /node_modules/,
            aggregateTimeout: 300,
            poll: 1000,
        },
    }
}
