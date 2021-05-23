<template>
  <div class="container">
    Popular
    <splide :options="options">
      <splide-slide>
        <div>
          <img :src="popularMovie1">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="popularMovie2">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="popularMovie3">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="popularMovie4">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="popularMovie5">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="popularMovie6">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="popularMovie7">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="popularMovie8">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="popularMovie9">
        </div>
      </splide-slide>
    </splide>
  </div>

</template>

<script>
import axios from 'axios'
// splide
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import '@splidejs/splide/dist/css/themes/splide-default.min.css';

export default {
  name: 'PopularMovies',
  data: function () {
    return {
      popularMovie1: null,
      popularMovie2: null,
      popularMovie3: null,
      popularMovie4: null,
      popularMovie5: null,
      popularMovie6: null,
      popularMovie7: null,
      popularMovie8: null,
      popularMovie9: null,
      options: {
          type : 'loop',
          perPage: 3,
        },
    }
  },
  components: {
    Splide,
    SplideSlide,
  },
  methods: {
    getPopularMovies: function () {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/popular?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR'
      })
        .then(res => {
          this.popularMovie1 = `https://image.tmdb.org/t/p/w200${res.data.results[0].poster_path}`
          this.popularMovie2 = `https://image.tmdb.org/t/p/w200${res.data.results[1].poster_path}`
          this.popularMovie3 = `https://image.tmdb.org/t/p/w200${res.data.results[2].poster_path}`
          this.popularMovie4 = `https://image.tmdb.org/t/p/w200${res.data.results[3].poster_path}`
          this.popularMovie5 = `https://image.tmdb.org/t/p/w200${res.data.results[4].poster_path}`
          this.popularMovie6 = `https://image.tmdb.org/t/p/w200${res.data.results[5].poster_path}`
          this.popularMovie7 = `https://image.tmdb.org/t/p/w200${res.data.results[6].poster_path}`
          this.popularMovie8 = `https://image.tmdb.org/t/p/w200${res.data.results[7].poster_path}`
          this.popularMovie9 = `https://image.tmdb.org/t/p/w200${res.data.results[8].poster_path}`
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.getPopularMovies()
  }
}
</script>

<style>

</style>