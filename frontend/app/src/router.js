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
            path: '/logout',
            name: 'logout',
            component: () => import(/* webpackChunkName: "login" */ './components/Logout.vue')
        },
        {
            path: '/blog',
            name: 'blog',
            component: () => import(/* webpackChunkName: "blog" */ './views/Blog.vue')
        },
        {
            path: '/authors',
            name: 'Authors',
            component: () => import(/* webpackChunkName: "blog" */ './components/Authors/List.vue')
        },
        {
            path: '/authors/:id',
            name: 'Author',
            component: () => import(/* webpackChunkName: "blog" */ './components/Authors/Single.vue')
        },

    ]
});

