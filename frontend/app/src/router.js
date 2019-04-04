import Vue from 'vue'
import Router from 'vue-router'
import axiosAuth from '@/api/axios-auth'

Vue.use(Router);

const routes = [
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
        component: () => import(/* webpackChunkName: "login" */ './views/Logout.vue')
    },
    {
        path: '/blog',
        name: 'blog',
        component: () => import(/* webpackChunkName: "blog" */ './views/Blog.vue')
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        meta: {requiresAuth: true},
        component: () => import(/* webpackChunkName: "blog" */ './views/templates/admin/Dashboard.vue'),
    },
];

const router = new Router({
    routes: routes,
});

router.beforeEach((to, from, next) => {
    let token = localStorage.getItem('token');
    let requireAuth = to.matched.some(record => record.meta.requiresAuth);

    if (!requireAuth) {
        next();
    }

    if (requireAuth && !token) {
        next('/login');
    }

    if (to.path === '/login') {
        if (token) {
            axiosAuth.post('/decode_token').then(() => {
                next('/dashboard');
            }).catch(() => {
                next();
            });
        } else {
            next();
        }
    }

    if (requireAuth && token) {
        axiosAuth.post('/decode_token').then(() => {
            next();
        }).catch(() => {
            next('/login');
        })
    }
});

export default router;
