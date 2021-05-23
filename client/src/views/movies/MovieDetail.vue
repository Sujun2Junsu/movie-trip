<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <div>
          <p>{{ movie.title }}</p>
          <img :src="movie.poster_path" alt="포스터" style="width: 100%">
        </div>
      </div>
      <div class="col-md-4">
        <div>
          <p>줄거리</p>
          {{ movie.overview }}
        </div>
      </div>
      <div class="col-md-4">
        <div>
          <p>트레일러</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "MovieDetail",
  data: function () {
    return {
      movieTitle: this.$route.params.movieTitle,
      movie: null,
    }
  },
  methods: {
    getMovieDetail: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/movie-list/',
      })
        .then(res => {
          const movieList = res.data
          // console.log(movieList)
          for(var i in movieList) {
            console.log(movieList[i])
            if(movieList[i].title === this.movieTitle) {
              this.movie = movieList[i];
            }
          }
          // console.log(this.movie)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.getMovieDetail()
  }
}
</script>

<style>

</style>