import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)


export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import(/* webpackChunkName: "home" */ './views/Home.vue')
        },
        {
            path: '/',
            name: 'welcome',
            component: () => import(/* webpackChunkName: "welcome" */ './views/Welcome.vue')
        },
        {
            path: '/documentation',
            name: 'documentation',
            component: () => import(/* webpackChunkName: "documentation" */ './views/Documentation.vue')
        },
        {
            path: '/acknowledgements',
            name: 'acknowledgements',
            component: () => import(/* webpackChunkName: "acknowledgements" */ './views/Acknowledgements.vue')
        },
        {
            path: '/news',
            name: 'news',
            component: () => import(/* webpackChunkName: "newsroom" */ './views/NewsRoom.vue')
        },
        {
            path: '/search',
            name: 'search',
            component: () => import(/* webpackChunkName: "search" */ './views/Search.vue')
        }

    ]
})
