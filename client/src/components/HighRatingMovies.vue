<template>
  <div class="container">
    High Rated
    <splide :options="options">
      <splide-slide>
        <div>
          <img :src="highRatingMovie1">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="highRatingMovie2">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="highRatingMovie3">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="highRatingMovie4">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="highRatingMovie5">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="highRatingMovie6">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="highRatingMovie7">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="highRatingMovie8">
        </div>
      </splide-slide>
      <splide-slide>
        <div>
          <img :src="highRatingMovie9">
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
  name: 'HightRatingMovies',
  data: function () {
    return {
      highRatingMovie1: null,
      highRatingMovie2: null,
      highRatingMovie3: null,
      highRatingMovie4: null,
      highRatingMovie5: null,
      highRatingMovie6: null,
      highRatingMovie7: null,
      highRatingMovie8: null,
      highRatingMovie9: null,
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
    getHightRatingMovies: function () {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-KR&page=1`
      })
        .then(res => {
          this.highRatingMovie1 = `https://image.tmdb.org/t/p/w200${res.data.results[0].poster_path}`
          this.highRatingMovie2 = `https://image.tmdb.org/t/p/w200${res.data.results[1].poster_path}`
          this.highRatingMovie3 = `https://image.tmdb.org/t/p/w200${res.data.results[2].poster_path}`
          this.highRatingMovie4 = `https://image.tmdb.org/t/p/w200${res.data.results[3].poster_path}`
          this.highRatingMovie5 = `https://image.tmdb.org/t/p/w200${res.data.results[4].poster_path}`
          this.highRatingMovie6 = `https://image.tmdb.org/t/p/w200${res.data.results[5].poster_path}`
          this.highRatingMovie7 = `https://image.tmdb.org/t/p/w200${res.data.results[6].poster_path}`
          this.highRatingMovie8 = `https://image.tmdb.org/t/p/w200${res.data.results[7].poster_path}`
          this.highRatingMovie9 = `https://image.tmdb.org/t/p/w200${res.data.results[8].poster_path}`
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.getHightRatingMovies()
  }
}
</script>

<style>

</style>