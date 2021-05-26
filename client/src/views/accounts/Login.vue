
<template>
  <div>
    <div class="Login"
    v-if="visible" @click.self="handleWrapperClick">
    <div class="my-modal__dialog">
      <div class="modal-content">
      <header class="my-modal__header">
        <span>Login</span>
        <!-- <button @click="$emit('update:visible', !visible)">Close</button> -->
        <!-- <button @click="$emit('update:visible', !visible)" type="button" class="btn-close justify-content-end" aria-label="Close"></button> -->
      </header>
      <div class="my-modal__body">
        <div>
          <label for="username1" class="form-label">사용자 이름</label>
          <input type="text" class="form-control" id="username" v-model="credentials1.username" placeholder="Username">
        </div>
          <br>
        <div>
          <label for="password1" class="form-label">비밀번호</label>
          <input type="password" class="form-control" id="password" v-model="credentials1.password" placeholder="Password">
        </div>
        </div>
        <div class="modal-footer">
            <!-- <button @click="login" type="button" class="btn btn-primary" data-bs-dismiss="modal">Login</button> -->
            <button @click="login" type="button" class="btn btn-primary" >Login</button>
            <button @click="$emit('update:visible', !visible)" type="button" class="btn btn-secondary">Close</button>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'my-modal',
  props: {
    visible: {
      type: Boolean,
      require: true,
      default: false
    },
    title: {
      type: String,
      require: false,
    },
  },
  data: function () {
    return {
      credentials1: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials1,        
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('my-modal')
          // this.$router.push({ name: 'Home'})
          // login 후 modal close 안되는 것 위해 새로고침    
          location.reload()
        })
        .catch(err => {
          console.log(err)
        })
    },
    handleWrapperClick(){
      this.$emit('update:visible', false)
      // this.$router.push({ name: '/Home'})   
    },
  }
}

</script>

<style lang="scss">
$module: 'my-modal';
.#{$module} {
  // This is modal bg
  background-color: rgba(0,0,0,.7);
  top: 0; right: 0; bottom: 0; left: 0;
  position: fixed;
  overflow: auto;
  margin: 0;

  //This is modal layer
  &__dialog{
    z-index: 999;
    width: 600px;
    background: #fff;
    margin-bottom: 50px;
    // modal 가운데 등장하게 크기 상관없이
    position: fixed;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    -moz-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    -o-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
  }

  &__header {
    font-size: 28px;
    font-weight: bold;
    line-height: 1.29;
    padding: 16px 16px 0 25px;
    position: relative;
  }
  &__body {
    padding: 25px;
    min-height: 150px;
    max-height: 412px;
    overflow-y: scroll;
  }
}
</style>