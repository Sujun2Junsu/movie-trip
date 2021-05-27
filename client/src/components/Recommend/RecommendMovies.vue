<template>
  <div v-if="recommendMovie" class="container">
    <hr>
    <div><h4>{{ recommendMovie.movieNm }}({{ recommendMovie.movieNmOg }})</h4></div>
    <div style="text-align: start;">- 개봉일: {{ recommendMovie.openDt }}</div>
    <div style="text-align: start;">- 장르: {{ recommendMovie.genreAlt }}</div>
    <div style="text-align: start;">- 상영시간: {{ recommendMovie.showTm }}분</div>
    <div style="text-align: start;">- 감독: {{ recommendMovie.directors[0].peopleNm }}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RecommendMovies',
  data: function () {
    return {
      recommendMovie: null,
    }
  },
  props: {
    countryCode: {
      type: Number,
    }
  },
  methods: {
    getRecommendMovie: function () {
      axios({
        method: 'get',
        url: `http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&repNationCd=${this.countryCode}`
      })
        .then(res => {
          // console.log(res)
          var idx = Math.floor(Math.random() * 10)
          // console.log(idx)
          var MovieCode = res.data.movieListResult.movieList[idx].movieCd
          axios({
            method: 'get',
            url: `http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=25082f603f83818090a9a2a338bc11da&movieCd=${MovieCode}`
          })
            .then(res => {
              this.recommendMovie = res.data.movieInfoResult.movieInfo
            })
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  watch: {
    countryCode: function () {
      this.getRecommendMovie()
    },
  }
}
</script>

<style>

</style>