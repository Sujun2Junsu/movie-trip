<template>
  <div class="container">
    Top Rated
    <splide :options="options">
      <splide-slide>
        <div v-if="topRatedMovie1">
          <img @click="goMovieDetail1" :src="`https://image.tmdb.org/t/p/w200${topRatedMovie1.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="topRatedMovie2">
          <img @click="goMovieDetail2" :src="`https://image.tmdb.org/t/p/w200${topRatedMovie2.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="topRatedMovie3">
          <img @click="goMovieDetail3" :src="`https://image.tmdb.org/t/p/w200${topRatedMovie3.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="topRatedMovie4">
          <img @click="goMovieDetail4" :src="`https://image.tmdb.org/t/p/w200${topRatedMovie4.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="topRatedMovie5">
          <img @click="goMovieDetail5" :src="`https://image.tmdb.org/t/p/w200${topRatedMovie5.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="topRatedMovie6">
          <img @click="goMovieDetail6" :src="`https://image.tmdb.org/t/p/w200${topRatedMovie6.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="topRatedMovie7">
          <img @click="goMovieDetail7" :src="`https://image.tmdb.org/t/p/w200${topRatedMovie7.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="topRatedMovie8">
          <img @click="goMovieDetail8" :src="`https://image.tmdb.org/t/p/w200${topRatedMovie8.poster_path}`">
        </div>
      </splide-slide>
      <splide-slide>
        <div v-if="topRatedMovie9">
          <img @click="goMovieDetail9" :src="`https://image.tmdb.org/t/p/w200${topRatedMovie9.poster_path}`">
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
  name: 'topRatedMovies',
  data: function () {
    return {
      topRatedMovie1: null,
      topRatedMovie2: null,
      topRatedMovie3: null,
      topRatedMovie4: null,
      topRatedMovie5: null,
      topRatedMovie6: null,
      topRatedMovie7: null,
      topRatedMovie8: null,
      topRatedMovie9: null,
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
    gettopRatedMovies: function () {
      const API_KEY = process.env.VUE_APP_TMDB_API_KEY

      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-KR`
      })
        .then(res => {
          this.topRatedMovie1 = res.data.results[0]
          this.topRatedMovie2 = res.data.results[1]
          this.topRatedMovie3 = res.data.results[2]
          this.topRatedMovie4 = res.data.results[3]
          this.topRatedMovie5 = res.data.results[4]
          this.topRatedMovie6 = res.data.results[5]
          this.topRatedMovie7 = res.data.results[6]
          this.topRatedMovie8 = res.data.results[7]
          this.topRatedMovie9 = res.data.results[8]
        })
        .catch(err => {
          console.log(err)
        })
    },
    goMovieDetail1: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.topRatedMovie1.title }})
    },
    goMovieDetail2: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.topRatedMovie2.title }})
    },
    goMovieDetail3: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.topRatedMovie3.title }})
    },
    goMovieDetail4: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.topRatedMovie4.title }})
    },
    goMovieDetail5: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.topRatedMovie5.title }})
    },
    goMovieDetail6: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.topRatedMovie6.title }})
    },
    goMovieDetail7: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.topRatedMovie7.title }})
    },
    goMovieDetail8: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.topRatedMovie8.title }})
    },
    goMovieDetail9: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.topRatedMovie9.title }})
    },
  },
  created: function () {
    this.gettopRatedMovies()
  }
}
</script>

<style>

</style>