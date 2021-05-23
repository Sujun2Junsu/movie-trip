<template>
  <!-- 캐루젤 -->
  <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
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
    </div>
    <div class="carousel-inner mh-100" style="width: 100%; height: 600px; background-color: #070B19;">
      <p style="color: white;">Now Playing</p>
      <span class="carousel-item active">
          <img :src="this.firstNowPlayingMoviePic" class="m-0" style="height: 550px; padding-bottom: 25px;" alt="이미지를 불러올 수 없습니다.">
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
</template>

<script>
import axios from 'axios'

import NowPlayingMoviesItem from'@/components/movies/NowPlayingMoviesItem'

const API_KEY = '4dc86c92c350c5edac0c712116558e11'

export default {
  name: 'NowPlayingMovies',
  data: function () {
    return {
      firstNowPlayingMoviePic: null,
      nowPlayingMovies: null,
    }
  },
  components: {
    NowPlayingMoviesItem
  },
  methods: {
    getNowPlayingMovies: function () {
      axios({
        method: 'get',// movie_list
        url: `https://api.themoviedb.org/3/movie/now_playing?api_key=${API_KEY}&language=ko-KR&page=1`
      })
        .then(res => {
          const allNowPlayingMovies = res.data.results
          this.nowPlayingMovies = allNowPlayingMovies.slice(1,10)
          // carousel의 첫번째 아이템의 class에만 active를 붙이기 위해 따로 떼어냄
          this.firstNowPlayingMoviePic = `https://image.tmdb.org/t/p/w500${allNowPlayingMovies[0].poster_path}`
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.getNowPlayingMovies()
  },
}
</script>

<style>

</style>