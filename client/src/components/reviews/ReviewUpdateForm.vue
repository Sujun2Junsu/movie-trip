<template>
  <div class="container text-white" v-if="review">
    <h4>리뷰 수정</h4>
    <hr>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label row justify-content-start"> - 제목</label>
      <input type="input" class="form-control" id="exampleFormControlInput1" v-model="reviewTitle" :placeholder="review.title">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label row justify-content-start"> -  내용</label>
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="5" v-model="reviewContent" :placeholder="review.content"></textarea>
    </div>
    <button @click="updateReview">수정완료</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewUpdateForm',
  data: function (){
    return {
      reviewTitle: null,
      reviewContent: null,
      reviewId: this.$route.params.reviewId,
      movieId: this.$route.params.movieId,
      review: null,
      user: null,
    }
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
              this.user = res.data
            })
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateReview: function () {
      const reviewItem = {
        title: this.reviewTitle,
        content: this.reviewContent,
        movie: this.movieId
      }
      if (reviewItem.title && reviewItem.content && reviewItem.title.trim() && reviewItem.content.trim()) {
        console.log('성공')
        axios({
          method: 'put',
          url: `http://127.0.0.1:8000/movies/review/${this.reviewId}/`,
          data: reviewItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$router.push({ name: 'MovieDetailById', params: { movieId: this.movieId }})
          })
      } else {
        console.log('수정사항이 없습니다.')
      }
      
    }
  },
  created: function () {
    this.getReviewDetail()
  }
}
</script>

<style>

</style>