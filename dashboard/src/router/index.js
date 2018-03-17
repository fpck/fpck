import Vue from 'vue'
import Router from 'vue-router'
import * as pages from '@/pages';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: pages.Home
    },
    {
      path: '/about',
      name: 'About',
      component: pages.About
    }
  ]
})
