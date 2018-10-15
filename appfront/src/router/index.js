import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/menu/Home'
import Index from '@/components/menu/Index'
import Mark from '@/components/query/Mark'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/index',
      name: 'Index',
      component: Index
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/mark',
      name: 'Mark',
      component: Mark
    },
  ]
})
