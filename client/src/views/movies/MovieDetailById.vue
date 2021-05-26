<template>
  <div class="container">
    <div class="row" v-if="movie">
      <!-- <span class="col-3 align-self-start"><router-link :to="{ name: 'Movies' }" class="text-light">All Movies</router-link></span> -->
      <div class="movie-title row align-items-center justify-content-around">
        <span class="col"><h4 class="text-white mb-0">{{ movie.title }}</h4></span>
        <!-- <span class="col"><button>찜</button></span> -->
      </div>
      <br>
      <div class="col-lg-4">
        <div>
          <img :src="movie.poster_path" alt="포스터" style="width: 100%">
        </div>
      </div>
      <div class="col-lg-7 offset-lg-1">
        <div>
          <div class="video-wrap" v-if="relatedVideoUrl">
            <iframe :src="relatedVideoUrl" frameborder="1"></iframe>
          </div>
          <div>
            <p class="text-white-50 text-start">{{ movie.overview }}</p>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <div v-if="movie">
      <ReviewList
        :movieId="movie.id"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ReviewList from '@/views/review/ReviewList'

export default {
  name: "MovieDetail",
  data: function () {
    return {
      movieId: this.$route.params.movieId,
      movie: null,
      relatedVideoUrl: null,
    }
  },
  components: {
    ReviewList,
  },
  methods: {
    getMovieDetail: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/movie-detail/${this.movieId}/`,
      })
        .then(res => {
          console.log(res)
          this.movie = res.data
        })
        .then(movie => {
          const API_KEY = process.env.VUE_APP_TMDB_API_KEY
          axios({
            method: 'get',
            url: `https://api.themoviedb.org/3/movie/${movie.movie_id}/videos?api_key=${API_KEY}&language=en-US`
          })
          .then(res => {
            // console.log(res)
            // console.log(res.data.results[0])
            if (res.data.results[0]) {
              this.relatedVideoUrl = 'https://www.youtube.com/embed/' + res.data.results[0].key
            }
          })
        })
        .catch(err => {
          console.log(err)
        }) 
    },
  },
  created: function () {
    this.getMovieDetail()
  },
}
</script>

<style>
  .movie-title {
    border: 0;
    /* border: 0.1px solid gray; */
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
  }

  /* 트레일러 영상 반응형으로 만드는 css코드 */
  .video-wrap {
    position:relative; 
    padding-bottom:56.25%; 
    padding-top:30px; 
    height:0; 
    overflow:hidden;
    }

  .video-wrap iframe,
  .video-wrap object,
  .video-wrap embed {
    position:absolute; 
    top:0; 
    left:0; 
    width:100%; 
    height:100%;
    }
</style>