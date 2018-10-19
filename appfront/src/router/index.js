import Vue from 'vue'
import Vuex from 'Vuex'
import Router from 'vue-router'
import Home from '@/components/menu/Home'
import Index from '@/components/menu/Index'
import MakeMessage from '@/components/menu/MakeMessage'
import Mark from '@/components/query/Mark'
import Info from '@/components/personalInfo'
import Message from '@/components/message'
import Logout from '@/components/logout'


//状态管理
Vue.use(Vuex)

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/index',   name: 'Index',   component: Index },
    { path: '/home',    name: 'Home',    component: Home },
    { path: '/mark',    name: 'Mark',    component: Mark },
    { path: '/info',    name: 'Info',    component: Info },
    { path: '/message', name: 'Message', component: Message },
    { path: '/logout',  name: 'Logout',  component: Logout },
    { path: '/makeMessage',  name: 'MakeMessage',  component: MakeMessage },
  ]
})

