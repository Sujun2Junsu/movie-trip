import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Movies from '@/views/movies/Movies'
import MovieDetail from '@/views/movies/MovieDetail'
import MovieDetailById from '@/views/movies/MovieDetailById'
import Home from '@/views/Home.vue'
import ReviewList from '@/views/review/ReviewList'
import ReviewDetail from '@/views/review/ReviewDetail'
import ReviewForm from '@/components/reviews/ReviewForm'
import ReviewUpdateForm from '@/components/reviews/ReviewUpdateForm'
import Recommend from '@/views/recommend/Recommend'


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
    path: '/accounts/login/',
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
    path: '/movies2/:movieId',
    name: 'MovieDetailById',
    component: MovieDetailById
  },
  {
    path: '/review-list/:movieId',
    name: 'ReviewList',
    component: ReviewList
  },
  {
    path: '/review-detail/:movieId/:reviewId',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/review-form',
    name: 'ReviewForm',
    component: ReviewForm
  },
  {
    path: '/review-update-form/:movieId/:reviewId',
    name: 'ReviewUpdateForm',
    component: ReviewUpdateForm
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
