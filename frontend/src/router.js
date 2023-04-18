import {createRouter, createWebHistory} from 'vue-router'
import home from './components/home.vue'
import login from './components/login.vue'
import register from './components/register.vue'
import create from './components/create.vue'
import search from './components/search.vue'
import myprofile from './components/myprofile.vue'

const routes = [
    {
        path: '/home',
        name: 'home',
        component: home
    },
    {
        path: '/login',
        name: 'login',
        component: login
    },
    {
        path: '/register',
        name: 'register',
        component: register
    },
    {
        path: '/create',
        name: create,
        component: create
    },
    {
        path: '/search',
        name: search,
        component: search
    },
    {
        path: '/myprofile',
        name: myprofile,
        component: myprofile
    }


]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router;