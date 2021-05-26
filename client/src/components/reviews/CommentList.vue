<template>
  <div class="row justify-content-start container">
    <br><hr><br>
    <span class="col-3 text-white">댓글 목록</span>
    <br>
    <div>
      <CommentListItem
        id="commentReload"
        v-for="(comment,idx) in commentList"
        :key="idx"
        :comment="comment"
        @delete_comment="getCommentList"
      />
    </div>
    <br><br><hr>
    <div class="row justify-content-around align-items-center">
      <span class="col-6 offset-3"><input type="text" class="form-control" v-model="commentContent" @keyup.enter="createComment"></span>
      <span class="col-3"><button @click="createComment" class="btn btn-outline-light">댓글 등록</button></span>
      <br><br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import $ from 'jquery'

import CommentListItem from '@/components/reviews/CommentListItem'

export default {
  name: 'CommentList',
  data: function () {
    return {
      commentList: null,
      commentContent: null,
    }
  },
  props: {
    movieId: {
      type: Number,
    },
    reviewId: {
      type: Number
    },
  },
  components: {
    CommentListItem
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getCommentList: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/review/${this.reviewId}/comment-list/`,
        headers: this.setToken()
      })
      .then(res => {
        this.commentList = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    createComment: function () {
      const commentItem = {
        content: this.commentContent,
        review: this.reviewId
      }
      if (commentItem.content && commentItem.content.trim()) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/review/${this.reviewId}/comment-list/`,
          data: commentItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.getCommentList() // 그냥 이렇게하면 되는거였어!
            // location.reload() // 얘는 전체 페이지 새로고침
            // $("#commentReload").load("#commentReload"); // 이것도 전체 새로고침 되는데?ㅠ
            this.commentContent = '' // 비워주기
          })
          .catch(err => {
            console.log(err)
          })
      }
    }
  },
  created: function () {
    this.getCommentList()
  }
}
</script>

<style>

</style>