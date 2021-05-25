<template>
  <div id="app">
    <div id="nav">
      <span v-if="isLogin">
        <ul class="nav justify-content-end">
          <li class="nav-item">
            <router-link @click.native="logout" to="#">Logout</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'Review' }">Review</router-link>
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
            <router-link :to="{ name: 'Login' }">Login</router-link> |
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'Signup' }">Signup</router-link>
          </li>
        </ul>  
        <ul class="nav justify-content-center">
          <li class="nav-item">
            <router-link :to="{ name: 'Home'}"><img src="@/assets/logo.png" style="width:300px"></router-link>
          </li>
        </ul>
      </span>
    </div>
    <router-view @login="isLogin = true"/>
    <!-- <footer> -->
      <!-- Copyright -->
      <!-- <div class="text-center p-3" style="background-color: gray-dark;"> -->
      <!-- 아래는 반응형 footer/ 위에는 고정형  -->
      <!-- <div class="fixed-bottom d-flex justify-content-center pt-5">© 2021 Copyright: 수준이 준수(석정준, 서민수)</div> -->
      <!-- Copyright -->
    <!-- </footer> -->
    <!-- 아래는 하단 고정형 -->
    <footer id="sticky-footer" class="py-4 bg-dark text-white-50">
      <div class="container text-center">
        <small>Copyright &copy; Your Website</small>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login'})
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

</style>
