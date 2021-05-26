<template>
  <div id="app">
    <div id="nav">
      <span v-if="isLogin">
        <ul class="nav justify-content-end">
          <li class="nav-item">
            <router-link @click.native="logout" to="#">Logout</router-link>
          </li>
        </ul>       
        <ul class="nav justify-content-center">
          <li class="nav-item">
            <router-link :to="{ name: 'Home'}"><img src="@/assets/logo.png" style="width:300px"></router-link>
          </li>
        </ul>
      </span>
      <span v-else>
        <ul class="nav justify-content-end">
          <li class="nav-item">
            <button @click="handleClickButton">Login</button>
            <app-my-modal
              :visible.sync="visible">
            </app-my-modal>
          </li>
          <!-- <li class="nav-item">
            <button @click="handleClickButton">Signup</button>
            <signup-modal
              :visible.sync="visible">
            </signup-modal>
            <router-link :to="{ name: 'Signup' }">Signup</router-link> -->
          <!-- </li> -->
        </ul>  
        <ul class="nav justify-content-center">
          <li class="nav-item">
            <router-link :to="{ name: 'Home'}"><img src="@/assets/logo.png" style="width:300px"></router-link>
          </li>
        </ul>
      </span>
    </div>
    <router-view @login="isLogin = true"/>

    <!-- 아래는 하단 고정형 -->
    <footer id="sticky-footer" class="py-4 bg-dark text-white-50">
      <div class="container text-center">
        <small>Copyright &copy; 서울 4반 석정준 서민수</small>
      </div>
    </footer>
  </div>
</template>

<script>
import myModal from '@/views/accounts/Login'
// import myModal from '@/views/accounts/Signup'
// import signupModal from '@/views/accounts/Signup'

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      visible: false
    }
  },
  components: {
    appMyModal: myModal,
    // signupModal: signupModal
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login'})
    },
    // moveToLogin: function () {
    //   this.$router.push({name: 'Login'})
    // },
    handleClickButton(){
      this.visible = !this.visible
    }
    // signupClickButton(){
    //   this.visible = !this.visible
    // } 
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
