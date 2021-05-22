<template>
  <div class="home">
    <NowPlayingMovies/>
    <TrendingMovies/>
    <HighRatingMovies/>
  </div>
</template>

<script>
import NowPlayingMovies from '@/components/NowPlayingMovies'
import TrendingMovies from '@/components/TrendingMovies'
import HighRatingMovies from '@/components/HighRatingMovies'

export default {
  name: 'Home',
  components: {
    NowPlayingMovies,
    TrendingMovies,
    HighRatingMovies,
  }
}
</script>
