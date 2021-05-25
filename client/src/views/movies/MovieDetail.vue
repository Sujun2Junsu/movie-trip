<template>
  <div class="container">
    <div class="row" v-if="movie">
      <router-link class="col align-self-start" :to="{ name: 'Movies' }">[전체영화 보기]</router-link>
      <hr class="movie-card">
      <br>
      <span class="h5 text-white">{{ movie.title }}</span>
      <br><br>
      <hr>
      <div class="col-lg-4">
        <div>
          <img :src="movie.poster_path" alt="포스터" style="width: 100%">
        </div>
      </div>
      <div class="col-lg-8">
        <div>
          <div>
            <div class="video-wrap" v-if="relatedVideoUrl">
              <iframe :src="relatedVideoUrl" frameborder="1"></iframe>
            </div>
          </div>
          <div>
            <p class="text-white-50 text-start">{{ movie.overview }}</p>
          </div>
        </div>
        <div>
        </div>
      </div>
    </div>
    <hr>
    <button>Review</button>
    <button>찜</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "MovieDetail",
  data: function () {
    return {
      movieTitle: this.$route.params.movieTitle,
      movie: null,
      relatedVideoUrl: null,
    }
  },
  methods: {
    getMovieDetail: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/movie-list/',
      })
        .then(res => {
          const movieList = res.data
          for(var i in movieList) {
            if(movieList[i].title === this.movieTitle) {
              this.movie = movieList[i]
              return movieList[i]
            }
          }
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
  /* 영화 카드 구분선 */
  .movie-card {
    border-style: inset;
    border-width:2px;
    border-radius: 10px;    
    padding: 3px;
    border-color:#a64d5d;
    background: white;
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