<template>
  <div class="home">
    <NowPlayingMovies/>
    <router-link :to="{ name: 'Movies' }">[전체영화 보기]</router-link>
    <PopularMovies/>
    <HighRatingMovies/>
  </div>
</template>

<script>
import NowPlayingMovies from '@/components/movies/NowPlayingMovies'
import PopularMovies from '@/components/movies/PopularMovies'
import HighRatingMovies from '@/components/movies/HighRatingMovies'

export default {
  name: 'Home',
  components: {
    NowPlayingMovies,
    PopularMovies,
    HighRatingMovies,
  }
}
</script>
