<template>
  <div class="container text-white">
    <h4 v-if="movieTitle">&lt;{{ movieTitle }}&gt; 리뷰 작성</h4>
    <hr>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label row justify-content-start"> 리뷰 제목</label>
      <input type="input" class="form-control" id="exampleFormControlInput1" v-model="reviewTitle">
    </div>
    <div class="mb-3">
      <label for="rating" class="form-label row"> 평점: {{ rank }}점</label>
      <div class="star-rating" id="rating">
        <input type="radio" id="5-stars" name="rating" value="5" v-model="rank"/>
        <label for="5-stars" class="star">&#9733;</label>
        <input type="radio" id="4-stars" name="rating" value="4" v-model="rank"/>
        <label for="4-stars" class="star">&#9733;</label>
        <input type="radio" id="3-stars" name="rating" value="3" v-model="rank"/>
        <label for="3-stars" class="star">&#9733;</label>
        <input type="radio" id="2-stars" name="rating" value="2" v-model="rank"/>
        <label for="2-stars" class="star">&#9733;</label>
        <input type="radio" id="1-star" name="rating" value="1" v-model="rank"/>
        <label for="1-star" class="star">&#9733;</label>
      </div>
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label row justify-content-start"> 리뷰 내용</label>
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="5" v-model="reviewContent"></textarea>
    </div>
    <button @click="createReview" class="btn btn-outline-light">등록</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewForm',
  data: function (){
    return {
      movieId: this.$route.params.movieId,
      reviewTitle: null,
      reviewContent: null,
      rank: 0,
      movieTitle: null,
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
    getMovieTitle: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/movie-detail/${this.movieId}/`
      })
        .then(res => {
          this.movieTitle = res.data.title
        })
        .catch(err => {
          console.log(err)
        })
    },
    createReview: function () {
      const reviewItem = {
        title: this.reviewTitle,
        content: this.reviewContent,
        movie: this.movieId,
        rank: this.rank
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
  },
  created: function () {
    this.getMovieTitle()
  }
}
</script>

<style>
.star-rating {
  border:0;
  /* border:solid 1px #ccc; */
  display:flex;
  flex-direction: row-reverse;
  font-size:1.5em;
  justify-content:space-around;
  padding:0 .2em;
  text-align:center;
  width:5em;
}

.star-rating input {
  display:none;
}

.star-rating label {
  color:#ccc;
  cursor:pointer;
}

.star-rating :checked ~ label {
  color:#f90;
}

.star-rating label:hover,
.star-rating label:hover ~ label {
  color:#fc0;
}

article {
  background-color:#ffe;
  box-shadow:0 0 1em 1px rgba(0,0,0,.25);
  color:#006;
  font-family:cursive;
  font-style:italic;
  margin:4em;
  max-width:30em;
  padding:2em;
}
</style>