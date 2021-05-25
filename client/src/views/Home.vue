<template>
  <div class="home container">
    <NowPlayingMovies/>
    <router-link :to="{ name: 'Movies' }">[전체영화 보기]</router-link>
    <PopularMovies/>
    <TopRatedMovies/>
  </div>
</template>

<script>
import NowPlayingMovies from '@/components/movies/NowPlayingMovies'
import PopularMovies from '@/components/movies/PopularMovies'
import TopRatedMovies from '@/components/movies/TopRatedMovies'

export default {
  name: 'Home',
  components: {
    NowPlayingMovies,
    PopularMovies,
    TopRatedMovies,
  }
}
</script>
