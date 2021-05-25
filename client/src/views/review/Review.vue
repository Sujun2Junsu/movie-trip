<template>
  <div v-if="movie">
    <h1>{{ movie.title }} 리뷰 목록</h1>
    <hr>
    <button>리뷰 작성</button>
    <ReviewListItem
      v-for="(review, idx) in reviewList"
      :key="idx"
      :review="review"
    />
  </div>
</template>

<script>
import axios from 'axios'

import ReviewListItem from '@/components/reviews/ReviewListItem'

export default {
  name: 'Review',
  data: function () {
    return {
      movieId: this.$route.params.movieId,
      movie: null,
      reviewList: null,
    }
  }, 
  components: {
    ReviewListItem
  },
  methods: {
    getMovieDetail: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/movie-detail/${this.movieId}/`
      })
        .then(res => {
          this.movie = res.data
        })
    },
    getReviewList: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/movie-detail/${this.movieId}/review-list/`
      })
      .then(res => {
        console.log(res)
        this.reviewList = res.data
      })
    }
  //   setToken: function () {
  //     const token = localStorage.getItem('jwt')
  //     const config = {
  //       Authorization: `JWT ${token}`
  //     }
  //     return config
  //     // config???

  //   },
  //   getReviews: function () {
  //     axios({
  //       method: 'get',
  //       url: 'http://127.0.0.1:8000/',
  //       headers: this.setToken()
  //     })
  //       .then((res) => {
  //         console.log(res)
  //         this.reviews = res.data
  //       })
  //       .catch((err) => {
  //         console.log(err)
  //       })
  //   },
  //   deleteReviews: function (review) {
  //     axios({
  //       method: 'delete',
  //       url: `http://127.0.0.1:8000/${review.id}/`,
  //       headers: this.setToken()
  //     })
  //       .then((res) => {
  //         console.log(res)
  //         this.getReviews()
  //       })
  //       .catch((err) => {
  //         console.log(err)
  //       })
  //   },
  //   updateReviewsStatus: function (review) {
  //     const reviewItem = {
  //       ...review,
  //       completed: !review.completed
  //     }

  //     axios({
  //       method: 'put',
  //       url: `http://127.0.0.1:8000/${review.id}/`,
  //       data: reviewItem,
  //       headers: this.setToken(),
  //     })
  //       .then((res) => {
  //         console.log(res)
  //         review.completed = !review.completed
  //       })
  //     },
  //   },
  // // createReviews: function () {
  // //     axios({
  // //       method: 'post',
  // //       url: 'http://127.0.0.1:8000/community/create/',
  // //       headers: this.setToken()
  // //     })
  // //       .then((res) => {
  // //         console.log(res)
  // //         this.reviews = res.data
  // //       })
  // //       .catch((err) => {
  // //         console.log(err)
  // //       })
  // //     // this.getReviews()
  // //   }
  //   createReview: function () {
  //     const reviewItem = {
  //       title: this.title,
  //     }

  //     if (reviewItem.title) {
  //       axios({
  //         method: 'post',
  //         url: 'http://127.0.0.1:8000/create/',
  //         data: reviewItem,
  //         headers: this.setToken()
  //       })
  //         .then((res) => {
  //           console.log(res)
  //           // this.$router.push({ name: 'TodoList' })
  //         })
  //         .catch((err) => {
  //           console.log(err)
  //         })
  //       }
  //   },
  },
  created: function () {
    this.getMovieDetail()
    this.getReviewList()
  }
}

</script>

<style>

</style>