<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-md navbar-dark bg-#2c3e50" style="height: 80px;">
        <div class="container-fluid">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <li class="nav-item">
            <router-link :to="{ name: 'Home'}">
              <img src="@/assets/logo.png" style="width:300px">
            </router-link>
          </li>
          <div class="collapse navbar-collapse container d-flex flex-row-reverse fs-5" id="navbarNav">
            <span v-if="isLogin">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <router-link @click.native="logout" to="#" class="text-light nav-link active" text-decoration: none>Logout</router-link>
                </li>
              </ul>
            </span>
            <span v-else>
              <ul class="navbar-nav gap-3">
                <li class="nav-item">
                  <a @click="handleClickButton" class="text-light nav-link">Login</a>
                  <app-my-modal
                    :visible.sync="visible">
                  </app-my-modal>
                </li>
                <li class="nav-item me-3">
                  <a @click="signupClickButton" class="text-light nav-link">Signup</a>
                  <signup-modal
                    :seen.sync="seen">
                  </signup-modal>
                </li>
              </ul>
            </span>
          </div>
        </div>
      </nav>
    </div>
    <router-view @login="isLogin = true"/>

    <!-- 아래는 하단 고정형 완성 -->
    <footer class="fixed-bottom d-flex justify-content-center align-items-center text-white-50 bg-dark py-2">
      <p class="m-0">Copyright &copy; 서울 4반 석정준 서민수</p>
    </footer>
  </div>
</template>


<script>
import myModal from '@/views/accounts/Login'
import signupModal from '@/views/accounts/Signup'

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      visible: false,
      seen: false
    }
  },
  components: {
    appMyModal: myModal,
    signupModal: signupModal
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Home'})
    },
    handleClickButton(){
      this.visible = !this.visible
    },
    signupClickButton(){
      this.seen = !this.seen
    } 
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

.body {
  background-color: black;
  text-align: center;
  z-index: 100;
}

.navbarNav {
  z-index: 991;
}

a { text-decoration:none }
</style>
