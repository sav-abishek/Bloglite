import SignUp from './components/SignUp.vue';
import Login from './components/Login.vue';
import Profile from './components/Profile.vue';
import feed from './components/feed.vue';
import follower from './components/follower.vue'


import{createRouter,createWebHistory} from 'vue-router'

const routes = [
    {
        name:'SignUp',
        component:SignUp,
        path:'/'
    },
    {
        name:'Login',
        component:Login,
        path:'/login'
    },
    {
        nmae:'Profile',
        component:Profile,
        path:'/profile'
    },
    {
        name:'feed',
        component:feed,
        path:'/feed'
    },
    {
        name:'follower',
        component:follower,
        path:'/follower'
    },

]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;

