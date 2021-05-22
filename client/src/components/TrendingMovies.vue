<template>
  <div class="container">
    Now Trending
    <splide :options="options">
      <splide-slide>
        <div>
          <img :src="trendingMovie1">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="trendingMovie2">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="trendingMovie3">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="trendingMovie4">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="trendingMovie5">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="trendingMovie6">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="trendingMovie7">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="trendingMovie8">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="trendingMovie9">
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

const API_KEY = '4dc86c92c350c5edac0c712116558e11'

export default {
  name: 'TrendingMovies',
  data: function () {
    return {
      trendingMovie1: null,
      trendingMovie2: null,
      trendingMovie3: null,
      trendingMovie4: null,
      trendingMovie5: null,
      trendingMovie6: null,
      trendingMovie7: null,
      trendingMovie8: null,
      trendingMovie9: null,
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
    getTrendingMovies: function () {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/trending/all/day?api_key=${API_KEY}&language=ko-KR&page=1`
      })
        .then(res => {
          this.trendingMovie1 = `https://image.tmdb.org/t/p/w200${res.data.results[0].poster_path}`
          this.trendingMovie2 = `https://image.tmdb.org/t/p/w200${res.data.results[1].poster_path}`
          this.trendingMovie3 = `https://image.tmdb.org/t/p/w200${res.data.results[2].poster_path}`
          this.trendingMovie4 = `https://image.tmdb.org/t/p/w200${res.data.results[3].poster_path}`
          this.trendingMovie5 = `https://image.tmdb.org/t/p/w200${res.data.results[4].poster_path}`
          this.trendingMovie6 = `https://image.tmdb.org/t/p/w200${res.data.results[5].poster_path}`
          this.trendingMovie7 = `https://image.tmdb.org/t/p/w200${res.data.results[6].poster_path}`
          this.trendingMovie8 = `https://image.tmdb.org/t/p/w200${res.data.results[7].poster_path}`
          this.trendingMovie9 = `https://image.tmdb.org/t/p/w200${res.data.results[8].poster_path}`
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.getTrendingMovies()
  }
}
</script>

<style>

</style>