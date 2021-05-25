<template>
  <div class="container" v-if="review">
    <h5 class="text-white">&lt; {{ movieTitle }} &gt; : {{ review.title }}</h5>
    <div class="row justify-content-around">
      <div class="col">작성자: {{ userName }}</div>
      <div class="col">등록: {{ createdTime }}</div>
      <div class="col">수정: {{ updatedTime }}</div>
    </div>
    <hr>
    <p class="text-white">{{ review.content }}</p>
  </div>

</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  name: 'ReviewDetail',
  data: function () {
    return { 
      reviewId: this.$route.params.reviewId,
      movieId: this.$route.params.movieId,
      review: null,
      userName: null,
      movieTitle: null,
    }
  },
  methods: {
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
  },
  computed: {
    createdTime: function () {
      moment.locale('kr')
      return moment(this.review.created_at).format('LLL')
    },
    updatedTime: function () {
      return moment(this.review.updated_at).format('LLL')
    },
  },
  created: function () {
    this.getReviewDetail()
  }
}
</script>
  
<style>

</style>