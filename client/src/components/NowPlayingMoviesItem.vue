<template>
  <span class="carousel-item">
    <div style="width: 100%; height: 600px; background-color: black;">
      <img :src="this.posterPath" class="m-0" style="height: 550px; padding-bottom: 25px;" alt="이미지를 불러올 수 없습니다.">
    </div>
  </span>
</template>

<script>
export default {
  name: 'NowPlayingMoviesItem',
  props: {
    movie: {
      type: Object,
    }
  },
  computed: {
    posterPath: function () { 
      const url = this.movie.poster_path
      return `https://image.tmdb.org/t/p/w500${url}`
    },
  }
}
</script>

<style>

</style>