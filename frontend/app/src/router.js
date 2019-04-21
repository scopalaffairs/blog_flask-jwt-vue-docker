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
        path: '/admin',
        name: 'login',
        component: () => import(/* webpackChunkName: "login" */ './views/Login.vue')
    },
    {
        path: '/logout',
        name: 'logout',
        component: () => import(/* webpackChunkName: "logout" */ './views/Logout.vue')
    },
    {
        path: '/blog',
        name: 'blog',
        component: () => import(/* webpackChunkName: "blog" */ './views/Blog.vue')
    },
    {
        path: '/blog/:postId',
        name: 'blogContent',
        component: () => import(/* webpackChunkName: "blogContent" */ './views/templates/blog/blog-post.vue')
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        meta: {requiresAuth: true},
        component: () => import(/* webpackChunkName: "dashboard" */ './views/templates/admin/Dashboard.vue'),
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

    // specific protection handling
    if (to.path === '/dashboard') {
        if (token) {
            axiosAuth.post('/users/login', token).then(() => {
                next('/dashboard');
            }).catch(() => {
                next();
            });
        } else {
            next();
        }
    }

    // generic protection handling
    if (requireAuth && token) {
        console.log("generic auth route", token);

        axiosAuth.post('/users/login', token).then(() => {
            next();
        }).catch(() => {
            next();
        })
    }
});

export default router;
