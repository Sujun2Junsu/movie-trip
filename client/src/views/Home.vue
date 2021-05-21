<template>
  <div class="home">
    <NowPlayingMovies/>
    <TrendingMovies/>
  </div>
</template>

<script>
import NowPlayingMovies from '@/components/NowPlayingMovies'
import TrendingMovies from '@/components/TrendingMovies'

export default {
  name: 'Home',
  components: {
    NowPlayingMovies,
    TrendingMovies,
  }
}
</script>
