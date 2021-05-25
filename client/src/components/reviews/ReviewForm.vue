<template>
  <div class="container text-white">
    <h4>리뷰 작성</h4>
    <hr>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label row justify-content-start"> - 제목</label>
      <input type="input" class="form-control" id="exampleFormControlInput1">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label row justify-content-start"> -  내용</label>
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="5"></textarea>
    </div>
    <!--   
    model = Review
    fields = '__all__'
    read_only_fields = ('user', 'movie',) 
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_reviews")
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    content, title
    movie, user는 어디서 받아오기
    -->
  </div>
</template>

<script>
export default {
  name: 'ReviewForm',
}
</script>

<style>

</style>