<template>
  <div class="container text-white">
    <h4>리뷰 작성</h4>
    <hr>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label row justify-content-start"> - 제목</label>
      <input type="input" class="form-control" id="exampleFormControlInput1" v-model="reviewTitle">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label row justify-content-start"> -  내용</label>
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="5" v-model="reviewContent"></textarea>
    </div>
    <button @click="createReview">Add</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewForm',
  data: function (){
    return {
      reviewTitle: null,
      reviewContent: null,
      movieId: this.$route.params.movieId,
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
    createReview: function () {
      const reviewItem = {
        title: this.reviewTitle,
        content: this.reviewContent,
        movie: this.movieId
      }
      if (reviewItem.title && reviewItem.content && reviewItem.title.trim() && reviewItem.content.trim()) {
        console.log('성공')
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/movie-detail/${this.movieId}/review-list/`,
          data: reviewItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$router.push({ name: 'MovieDetailById', params: { movieId: this.movieId }})
          })
      } else {
        console.log('값이 없습니다.')
      }
      
    }
  }
}
</script>

<style>

</style>