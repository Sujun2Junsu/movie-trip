import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Movies from '@/views/movies/Movies'
import MovieDetail from '@/views/movies/MovieDetail'
import Home from '@/views/Home.vue'
import Review from '@/views/review/Review'
import ReviewDetail from '@/views/review/ReviewDetail'



Vue.use(VueRouter)

const routes = [
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
  },
  {
    path: '/movies',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/movies/:movieTitle',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/review/:movieId',
    name: 'Review',
    component: Review
  },
  {
    path: '/review-detail/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
