<template>
  <div class="home container">
    <br>
    <NowPlayingMovies/>
    <br>
    <!-- <router-link :to="{ name: 'Movies' }" class="text-light">전체영화 보기</router-link> -->
    <br>
    <PopularMovies/>
    <br>
    <br>
    <br>
    <TopRatedMovies/>
    <br>
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
