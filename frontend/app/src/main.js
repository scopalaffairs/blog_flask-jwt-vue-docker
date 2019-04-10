import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/index'
import './registerServiceWorker'
import * as svgicon from 'vue-svgicon';

Vue.use(svgicon, {
  classPrefix: 'AppIcon-',
});


Vue.config.productionTip = false;


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
