import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/index'
import './registerServiceWorker'

import CKEditor from '@ckeditor/ckeditor5-vue';

Vue.config.productionTip = false

Vue.use(CKEditor)


new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
