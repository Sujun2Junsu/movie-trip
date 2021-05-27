<template>
  <span class="carousel-item">
    <span class="row justify-content-center align-items-center mouse-over" @click="goMovieDetail">
      <span class="col-4"><img :src="posterPath" class="m-0" style="height: 550px; padding-bottom: 25px;" alt="이미지를 불러올 수 없습니다."></span>
      <span class="col-4">
        <p class="text-white h4">{{ movie.title }}</p>
        <hr>
        <p class="text-white">{{ movie.overview }}</p>
      </span>
    </span>
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
  },
  methods: {
    goMovieDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: { movieTitle: this.movie.title }})
    },
  }
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