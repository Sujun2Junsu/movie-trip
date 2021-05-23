import Vue from 'vue'
import VueRouter from 'vue-router'
import Movies from '@/views/movies/Movies'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Home from '@/views/Home.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
