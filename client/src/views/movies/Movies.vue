<template>
  <div>
    <router-link :to="{ name: 'Home' }">[홈으로]</router-link>
    <div class="row row-cols-2 row-cols-sm-3 row-cols-md-5 g-4">
      <MoviesCard
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import MoviesCard from '@/views/movies/MoviesCard'

export default {
  name: 'Movies',
  data: function () {
    return {
      movies: null,
    }
  },
  components: {
    MoviesCard,
  },
  methods: {
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/movie-list/'
      })
        .then(res =>{
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.getMovies()
  }
}
</script>

<style>

</style>