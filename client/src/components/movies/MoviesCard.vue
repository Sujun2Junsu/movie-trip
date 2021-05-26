<template>
  <div class="col" @click="goMovieDetail">
    <div class="card">
      <img :src="movie.poster_path" class="card-img-top" :alt="movie.title">
      <div class="card-body">
        <h5 class="card-title text-white">{{ movie.title }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MoviesCard',
  props: {
    movie: {
      type: Object
    }
  },
  methods: {
    goMovieDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.movie.title }})
    },
  }
}
</script>

<style>
.card-body {
  background-color: #070B19;
}
</style>