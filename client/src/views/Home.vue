<template>
  <div class="home">
    <NowPlayingMovies/>
    <router-link :to="{ name: 'Movies' }">[전체영화 보기]</router-link>
    <PopularMovies/>
    <HighRatingMovies/>
  </div>
</template>

<script>
import NowPlayingMovies from '@/components/NowPlayingMovies'
import PopularMovies from '@/components/PopularMovies'
import HighRatingMovies from '@/components/HighRatingMovies'

export default {
  name: 'Home',
  components: {
    NowPlayingMovies,
    PopularMovies,
    HighRatingMovies,
  }
}
</script>
