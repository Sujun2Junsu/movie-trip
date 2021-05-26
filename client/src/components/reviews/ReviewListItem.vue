<template>
  <tr v-if="review" @click="goReviewDetail" class="text-white">
    <th scope="row">{{ review.title }}</th>
    <td>{{ userName }}</td>
    <td>{{ starRank }}</td>
    <td>{{ createdTime }}</td>
  </tr>
</template>

<script>
import moment from 'moment'
import axios from 'axios'

export default {
  name: 'ReviewListItem',
  data: function () {
    return {
      userName: null,
    }
  },
  props: {
    review: {
      type: Object,
    },
    movieId: {
      type: Number,
    },
  },
  methods: {
    goReviewDetail: function () {
      this.$router.push({ name: 'ReviewDetail', params: { reviewId: this.review.id, movieId: this.movieId }})
    },
    getUserName: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/user-detail/${this.review.user}/`
      })
        .then(res => {
          this.userName = res.data.username
        })
    }
  },
  computed: {
    createdTime: function () {
      return moment(this.review.created_at).format('LLL')
    },
    starRank: function () {
      let stars = ''
      for (let i = 0; i < this.review.rank; i++) {
        stars = stars + '★'
      }
      return stars
    }
  },
  created: function () {
    this.getUserName()
  }
}
</script>

<style>

</style>