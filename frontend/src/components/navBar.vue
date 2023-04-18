<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container mt5">
    <router-link class="navbar-brand text-style" to="/home">Welcome {{ user_profile.username }}</router-link>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
            <router-link class="button" to="/myprofile">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-lines-fill" viewBox="0 0 16 16">
              <path d="M6 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-5 6s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zM11 3.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5zm.5 2.5a.5.5 0 0 0 0 1h4a.5.5 0 0 0 0-1h-4zm2 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2zm0 3a.5.5 0 0 0 0 1h2a.5.5 0 0 0 0-1h-2z"/>
              </svg>
              Profile
            </router-link> 
        </li>
        <li class="nav-item">
            <router-link class="button" to="/create">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16">
              <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
              <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
              </svg>
              Create
            </router-link>  
        </li>
        <li class="nav-item">
            <router-link class="button" to="/search">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search-heart-fill" viewBox="0 0 16 16">
              <path d="M6.5 13a6.474 6.474 0 0 0 3.845-1.258h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.008 1.008 0 0 0-.115-.1A6.471 6.471 0 0 0 13 6.5 6.502 6.502 0 0 0 6.5 0a6.5 6.5 0 1 0 0 13Zm0-8.518c1.664-1.673 5.825 1.254 0 5.018-5.825-3.764-1.664-6.69 0-5.018Z"/>
              </svg>
              Search
            </router-link>  
        </li>
        <li class="nav-item">
            <router-link @click="logoutUser()" class="button-logout" to="/">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-box-arrow-in-right" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M6 3.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 0-1 0v2A1.5 1.5 0 0 0 6.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-8A1.5 1.5 0 0 0 5 3.5v2a.5.5 0 0 0 1 0v-2z"/>
              <path fill-rule="evenodd" d="M11.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H1.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
              </svg>
              Logout 
              
            </router-link>  
        </li>
      </ul>
    </div>
  </div>

</nav>
</template>

<script>
export default {
  data() {
    return  {
      user_profile: {"username": "sample"}
    }
  },
  methods: {
    getUser() {
      fetch('http://127.0.0.1:5000/myprofile',{
                method: 'GET',
                headers: {
                    "Content-type": "application/json",
                    "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .then(response => {
              this.user_profile = response
            })
            .catch(error => {
                console.log(error)
            })
    },

    logoutUser() {
      localStorage.removeItem("token"); 
      this.$router.push('/login')
    }
  },

  mounted() {
    this.getUser()
  } 
}
</script>

<style scoped>
  .text-style {
      font-size: 30px !important;
      font-family: fantasy !important;
      color: rgb(136, 135, 135) !important;
  }
  .button{
  background: #2a623d;
  color: white;
  padding: 10px;
  margin: 20px;
  border-radius: 10px;
  border: none;
  min-width: 200px;
  text-decoration: none;
}
.button-logout{
  background: #bb4506;
  color: white;
  padding: 10px;
  margin: 20px;
  border-radius: 10px;
  border: none;
  min-width: 200px;
  text-decoration: none;
}
.button-logout:hover{
  background: #bb4506;
  color: rgb(158, 155, 155);
  padding: 10px;
  margin: 20px;
  border-radius: 10px;
  border: none;
  min-width: 200px;
  text-decoration: none;
}
.button:hover{
  background: #2a623d;
  color: rgb(158, 155, 155);
  padding: 10px;
  margin: 20px;
  border-radius: 10px;
  border: none;
  min-width: 200px;
  text-decoration: none;
}
</style>