import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import(/* webpackChunkName: "home" */ './views/Home.vue')
        },
        {
            path: '/login',
            name: 'login',
            component: () => import(/* webpackChunkName: "login" */ './views/Login.vue')
        },
        {
            path: '/blog',
            name: 'blog',
            component: () => import(/* webpackChunkName: "blog" */ './views/Blog.vue')
        },
        {
            path: '/books',
            name: 'books',
            component: () => import(/* webpackChunkName: "blog" */ './views/Books.vue')
        }
    ]
});
