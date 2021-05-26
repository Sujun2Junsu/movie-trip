<template>
  <div>
    <div class="Signup"
    v-if="visible" @click.self="handleWrapperClick">
    <div class="signup-modal__dialog">
      <div class="modal-content">
      <header class="signup-modal__header">
        <span>Signup</span>
      </header>
      <div class="signup-modal__body">
        <div>
          <label for="username">사용자 이름 : </label>
          <input type="text" class="form-control" id="username" v-model="credentials.username" placeholder="Username">
        </div>
        <div>
          <label for="password">비밀번호 : </label>
          <input type="password" class="form-control" id="password" v-model="credentials.password" placeholder="Password">
        </div>
        <div>
          <label for="passwordConfirmation">비밀번호 확인: </label>
          <input type="password" class="form-control" id="passwordConfirmation" v-model="credentials.passwordConfirmation" placeholder="PasswordConfirmation">
        </div>
        <button @click="signup(credentials)">Signup</button>
        <!-- <button @click="$emit('update:visible', !visible)" type="button" class="btn btn-secondary">Close</button> -->
        <!-- <div class="modal-footer">
            <button @click="login" type="button" class="btn btn-primary" data-bs-dismiss="modal">Login</button>
            <button @click="$emit('update:visible', !visible)" type="button" class="btn btn-secondary">Close</button>
        </div> -->
      </div>
    </div>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  props: {
  visible: {
    type: Boolean,
    require: true,
    default: false
  },
  title: {
    type: String,
    require: false,
    }
  },
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,        
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Login'})           
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
$module: 'signup-modal';
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
    // left: 50%;
    // top: 75px;
    width: 600px;
    // position: absolute;
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