<template>
  <div class="container">
    <div class="h4 text-light">
      # 나만 빼고 다 본 영화!
    </div>
    <br>
    <splide :options="options">
      <splide-slide>
        <div v-if="popularMovie1">
          <img @click="goMovieDetail1" :src="`https://image.tmdb.org/t/p/w200${popularMovie1.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="popularMovie2">
          <img @click="goMovieDetail2" :src="`https://image.tmdb.org/t/p/w200${popularMovie2.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="popularMovie3">
          <img @click="goMovieDetail3" :src="`https://image.tmdb.org/t/p/w200${popularMovie3.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="popularMovie4">
          <img @click="goMovieDetail4" :src="`https://image.tmdb.org/t/p/w200${popularMovie4.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="popularMovie5">
          <img @click="goMovieDetail5" :src="`https://image.tmdb.org/t/p/w200${popularMovie5.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="popularMovie6">
          <img @click="goMovieDetail6" :src="`https://image.tmdb.org/t/p/w200${popularMovie6.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="popularMovie7">
          <img @click="goMovieDetail7" :src="`https://image.tmdb.org/t/p/w200${popularMovie7.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="popularMovie8">
          <img @click="goMovieDetail8" :src="`https://image.tmdb.org/t/p/w200${popularMovie8.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="popularMovie9">
          <img @click="goMovieDetail9" :src="`https://image.tmdb.org/t/p/w200${popularMovie9.poster_path}`">
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
      const API_KEY = process.env.VUE_APP_TMDB_API_KEY

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}&language=ko-KR`
      })
        .then(res => {
          this.popularMovie1 = res.data.results[0]
          this.popularMovie2 = res.data.results[1]
          this.popularMovie3 = res.data.results[2]
          this.popularMovie4 = res.data.results[3]
          this.popularMovie5 = res.data.results[4]
          this.popularMovie6 = res.data.results[5]
          this.popularMovie7 = res.data.results[6]
          this.popularMovie8 = res.data.results[7]
          this.popularMovie9 = res.data.results[8]
        })
        .catch(err => {
          console.log(err)
        })
    },
    goMovieDetail1: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.popularMovie1.title }})
    },
    goMovieDetail2: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.popularMovie2.title }})
    },
    goMovieDetail3: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.popularMovie3.title }})
    },
    goMovieDetail4: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.popularMovie4.title }})
    },
    goMovieDetail5: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.popularMovie5.title }})
    },
    goMovieDetail6: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.popularMovie6.title }})
    },
    goMovieDetail7: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.popularMovie7.title }})
    },
    goMovieDetail8: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.popularMovie8.title }})
    },
    goMovieDetail9: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.popularMovie9.title }})
    },
  },
  created: function () {
    this.getPopularMovies()
  }
}
</script>

<style>

</style>