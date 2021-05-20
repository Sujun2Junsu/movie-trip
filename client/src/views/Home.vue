<template>
  <div class="home">
    <NowPlayingMovies/>
  </div>
</template>

<script>
import NowPlayingMovies from '@/components/NowPlayingMovies'

export default {
  name: 'Home',
  components: {
    NowPlayingMovies
  }
}
</script>
