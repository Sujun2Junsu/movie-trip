<template>
  <div>
    <hr>
    <span>{{ review.title }}</span>
    <span>{{ review.created_at }}</span>
  </div>
</template>

<script>
export default {
  name: 'ReviewListItem',
  props: {
    review: {
      type: Object,
    }
  }
}
</script>

<style>

</style>