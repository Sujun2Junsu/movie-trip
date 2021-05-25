<template>
  <div>
    <h1>Review</h1>
    <button @click="created">리뷰 작성</button>
    


    <!-- <button>리뷰 작성</button> -->
    <!-- <ul>
      <li v-for="(review, idx) in reviews" :key="idx">
        <span @click="updateReviewsStatus(review)" :class="{ completed: review.completed }">{{ review.title }}</span>
        <button @click="deleteReviews(review)" class="review-btn">X</button>
      </li>
    </ul> -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Review',
  data: function () {
    return {
      title: '',
      content: '',
      myMovieRate: 0,
    }
  }, 
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
      // config???

    },
    getReviews: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/',
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.reviews = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReviews: function (review) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/${review.id}/`,
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.getReviews()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateReviewsStatus: function (review) {
      const reviewItem = {
        ...review,
        completed: !review.completed
      }

      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/${review.id}/`,
        data: reviewItem,
        headers: this.setToken(),
      })
        .then((res) => {
          console.log(res)
          review.completed = !review.completed
        })
      },
    },
  // createReviews: function () {
  //     axios({
  //       method: 'post',
  //       url: 'http://127.0.0.1:8000/community/create/',
  //       headers: this.setToken()
  //     })
  //       .then((res) => {
  //         console.log(res)
  //         this.reviews = res.data
  //       })
  //       .catch((err) => {
  //         console.log(err)
  //       })
  //     // this.getReviews()
  //   }
    createReview: function () {
      const reviewItem = {
        title: this.title,
      }

      if (reviewItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/community/create/',
          data: reviewItem,
          headers: this.setToken()
        })
          .then((res) => {
            console.log(res)
            // this.$router.push({ name: 'TodoList' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },

    created: function () {
    this.createReview()
  }
}

</script>

<style>

</style>