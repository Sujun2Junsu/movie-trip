<template>
  <div class="container" v-if="review">
    <br>
    <div class="row justify-content-around text-light">
      <!-- <div class="col text-light fas fa-arrow-left"></div> -->
      <!-- <router-link :to="{ name: 'ReviewList' }" class="text-light fas fa-arrow-left col-1"></router-link> -->
      <a @click="$router.go(-1)" class="text-light fas fa-arrow-left col-1"></a>
      <div class="col">작성자: {{ userName }}</div>
      <div class="col">등록: {{ createdTime }}</div>
      <div class="col">수정: {{ updatedTime }}</div>
      <hr>
    </div>
    <div class="row align-items-center">
      <h5 class="text-white col-7 m-0">&lt; {{ movieTitle }} &gt; : {{ review.title }}</h5>
      <h5 class="text-white col-3 m-0">{{ starRank }}</h5>
      <span class="col-2">
        <button @click="goUpdateReview()" class="btn btn-primary">수정</button>
        <button @click="deleteReview()" class="btn btn-danger">삭제</button>
      </span>
    </div>
    <hr>
    <div>      
      <p class="text-white" style="text-align: left; padding-left: 100px">{{ review.content }}</p>
    </div>
    <br>
    <div>
      <CommentList
        :movieId="parseInt(movieId)"
        :reviewId="parseInt(reviewId)"
      />
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import moment from 'moment'

import CommentList from '@/components/reviews/CommentList'

export default {
  name: 'ReviewDetail',
  data: function () {
    return { 
      reviewId: this.$route.params.reviewId,
      movieId: this.$route.params.movieId,
      review: null,
      userName: null,
      movieTitle: null,
      // is_same_user: null,
    }
  },
  components: {
    CommentList,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getReviewDetail: function (){
      // console.log(this.reviewId)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/review-detail/${this.reviewId}/`
      })
        .then(res => {
          this.review = res.data
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/user-detail/${this.review.user}/`
          })
            .then(res => {
              this.userName = res.data.username
              axios({
                method: 'get',
                url: `http://127.0.0.1:8000/movies/movie-detail/${this.movieId}/`
              })
                .then(res => {
                  this.movieTitle = res.data.title
                })
            })
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteReview: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/review/${this.reviewId}/`,
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'MovieDetailById', params: { movieId: this.movieId }})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goUpdateReview: function () {
      this.$router.push({ name: 'ReviewUpdateForm', params: { movieId: this.movieId, reviewId: this.reviewId }})
    },
    // isSameUser: function () {
    //   axios({
    //     method: 'get',
    //     url: `http://127.0.0.1:8000/movies/review-same-user/${this.reviewId}/`
    //   })
    //   .then(res => {
    //     console.log('유저')
    //     console.log(res)
    //   })
    // }
  },
  computed: {
    createdTime: function () {
      return moment(this.review.created_at).format('LLL')
    },
    updatedTime: function () {
      return moment(this.review.updated_at).format('LLL')
    },
    starRank: function () {
      let stars = ''
      for (let i = 0; i < this.review.rank; i++) {
        stars = stars + '★'
      }
      return stars
    }
  },
  created: function () {
    this.getReviewDetail()
    // this.isSameUser()
  }
}
</script>
  
<style>

</style>