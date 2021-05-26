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
              <th scope="col">평점</th>
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
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
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
        url: `http://127.0.0.1:8000/movies/movie-detail/${this.movieId}/review-list/`,
        headers: this.setToken()
      })
      .then(res => {
        this.reviewList = res.data
      })
    },
    goReviewForm: function () {
      this.$router.push({ name: 'ReviewForm', params: { movieId: this.movieId }})
    }
  },
  created: function () {
    this.getMovieDetail()
    this.getReviewList()
  }
}

</script>

<style>

</style>