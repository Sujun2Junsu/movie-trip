<template>
  <div v-if="movie">
    <div class="container">
      <div class="row align-items-center">
        <span class="col-8 offset-2 align-self-center"><h5 class="text-white mb-0">영화리뷰</h5></span>
        <span class="col-2"><button @click="goReviewForm">글 작성</button></span>
      </div>
      <br>
      <div class="d-lg-block col-lg-12"> 
        <table class="table table-dark table-hover">
          <thead>
            <tr class="text-white">
              <th scope="col">리뷰 제목</th>
              <th scope="col">작성자</th>
              <th scope="col">작성 시간</th>
            </tr>
          </thead>
          <tbody>
            <ReviewListItem
              v-for="(review, idx) in reviewList"
              :key="idx"
              :review="review"
              :movieId="movieId"
            />
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ReviewListItem from '@/components/reviews/ReviewListItem'

export default {
  name: 'Review',
  data: function () {
    return {
      movie: null,
      reviewList: null,
    }
  },
  props: {
    movieId: {
      type: Number,
    },
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
        // console.log(res)
        this.reviewList = res.data
      })
    },
    goReviewForm: function () {
      this.$router.push({ name: 'ReviewForm' })
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