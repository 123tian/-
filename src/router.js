import Vue from 'vue'
import VueRouter from 'vue-router'
import pageA from './pages/a'
import pageB from './pages/b'
import pageC from './pages/c'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component:pageA
  },
  {
  path: './pageb',
  component:pageB
  },

  {
    path: './pagec/:id',
    component: pageC
  }
]


const router = new VueRouter({
  routes
})

export default router
