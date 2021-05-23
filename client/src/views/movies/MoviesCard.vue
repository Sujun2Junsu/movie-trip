<template>
  <div class="col">
    <div class="card">
      <img :src="movie.poster_path" class="card-img-top" :alt="movie.title">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
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
  }
}
</script>

<style>

</style>