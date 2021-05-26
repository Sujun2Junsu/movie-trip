<template>
  <div class="row justify-content-start">
    <span v-if="userName" class="col-2 offset-1  text-secondary">
      - {{ userName }} :
    </span>
    <span class="col-2 text-secondary">
      {{ comment.content }}
    </span>
    <span class="col-3 offset-2">
      {{ createdTime }}
    </span>
    <span class="col-1">
      <button @click="deleteComment">삭제</button>
    </span>
  </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  name: 'CommentListItem',
  data: function () {
    return {
      userName: null,
      isCreateUser: null,
    }
  },
  props: {
    comment: {
      type: Object,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getUserName: function () {
      axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/user-detail/${this.comment.user}/`
      })
        .then(res => {
          this.userName = res.data.username
          
        })
    },
    deleteComment: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/review_comment/${this.comment.id}/`,
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          // location.reload()
          this.$emit('delete_comment')
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.getUserName()
  },
  computed: {
    createdTime: function () {
      return moment(this.comment.created_at).format('LLL')
    },
  }
}
</script>

<style>

</style>