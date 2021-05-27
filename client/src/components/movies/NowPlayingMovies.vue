<template>
  <div class="container">
    <!-- 캐루젤 -->
    <p class="h2 text-light">Now Playing</p>
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
      <!-- <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="5" aria-label="Slide 6"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="6" aria-label="Slide 7"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="7" aria-label="Slide 8"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="8" aria-label="Slide 9"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="9" aria-label="Slide 10"></button>
      </div> -->
      <div class="carousel-inner mh-100" style="width: 100%; height: 600px; background-color: #070B19;">
        
        <br>
        <span v-if="firstNowPlayingMovie" class="carousel-item active">
          <span class="row justify-content-center align-items-center mouse-over" @click="goMovieDetail">
            <span class="col-4"><img :src="firstNowPlayingMoviePic" class="m-0" style="height: 550px; padding-bottom: 25px;" alt="이미지를 불러올 수 없습니다."></span>
            <span class="col-4">
              <p class="text-white h4">{{ firstNowPlayingMovie.title }}</p>
              <hr>
              <p class="text-white">{{ firstNowPlayingMovie.overview }}</p>
            </span>
          </span>
        </span>
        <NowPlayingMoviesItem
          v-for="(movie, idx) in nowPlayingMovies"
          :key="idx"
          :movie="movie"
        />
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import NowPlayingMoviesItem from'@/components/movies/NowPlayingMoviesItem'

export default {
  name: 'NowPlayingMovies',
  data: function () {
    return {
      firstNowPlayingMovie: null,
      firstNowPlayingMoviePic: null,
      nowPlayingMovies: null,
    }
  },
  components: {
    NowPlayingMoviesItem
  },
  methods: {
    getNowPlayingMovies: function () {

      const API_KEY = process.env.VUE_APP_TMDB_API_KEY

      axios({
        method: 'get',// movie_list
        url: `https://api.themoviedb.org/3/movie/now_playing?api_key=${API_KEY}&language=ko-KR&page=1`
      })
        .then(res => {
          const allNowPlayingMovies = res.data.results
          this.nowPlayingMovies = allNowPlayingMovies.slice(1,10)
          // carousel의 첫번째 아이템의 class에만 active를 붙이기 위해 따로 떼어냄
          this.firstNowPlayingMovie = allNowPlayingMovies[0]
          console.log(this.firstNowPlayingMovie)
          this.firstNowPlayingMoviePic = `https://image.tmdb.org/t/p/w500/${allNowPlayingMovies[0].poster_path}`
        })
        .catch(err => {
          console.log(err)
        })
    },
    goMovieDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.firstNowPlayingMovie.title }})
    },
  },
  created: function () {
    this.getNowPlayingMovies()
  },
}
</script>

<style>
.mouse-over {
    -webkit-transform:scale(1);
    -moz-transform:scale(1);
    -ms-transform:scale(1); 
    -o-transform:scale(1);  
    transform:scale(1);
    -webkit-transition:.3s;
    -moz-transition:.3s;
    -ms-transition:.3s;
    -o-transition:.3s;
    transition:.3s;
    overflow: hidden;
}
.mouse-over:hover {
    -webkit-transform:scale(1.2);
    -moz-transform:scale(1.2);
    -ms-transform:scale(1.2);   
    -o-transform:scale(1.2);
    transform:scale(1.2);
    overflow: hidden;
    background-color:rgba(0, 0, 0, 0.308);
}
</style>