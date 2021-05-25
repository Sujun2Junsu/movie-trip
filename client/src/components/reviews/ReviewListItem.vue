<template>
  <div v-if="review">
    <hr>
    <div @click="goReviewDetail">
      <span>{{ review.title }}</span>
      <span>{{ review.created_at }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  props: {
    review: {
      type: Object,
    },
  },
  methods: {
    goReviewDetail: function () {
      this.$router.push({ name: 'ReviewDetail', params: { reviewId: this.review.id }})
    }
  }
}
</script>

<style>

</style>