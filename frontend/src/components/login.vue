<template>
    
    <div class="body container">
      <loginHeader/>
      
    <div v-if="message" class="alert alert-warning alert-dismissible fade show mt-5" role="alert">
    <strong>{{this.message}}</strong>
    </div>

      <div class="box">
       <form >
            <br>
            <input type="text" v-model="username" name="username" placeholder="Username" >
            <br>
            <input type="password" v-model="password" name="password" placeholder="Password" >
            <br><br>
            <button @click.prevent="logmein" class="center" type="submit">Log in</button>
        </form>
      </div>    
  </div>
  <!-- <loginFooter/> -->
</template>

<script>
import loginFooter from './loginFooter.vue';
import loginHeader from './loginHeader.vue';
import home from './home.vue';
// import {router} from '../router';
import router from '../router.js';

export default {


  components: { 
    loginFooter,
    loginHeader, 
    home
     },

  data() {
    return {
      username: '',
      password: '',
      message: null
    }
  },

  methods: {
    logmein() {
      if (!this.username || !this.password) {
                this.message = "Please enter all the fields"
                
            } else { fetch('http://127.0.0.1:5000/login',{
                method: 'POST',
                headers: {
                    "Content-type": "application/json"
                },
                body: JSON.stringify({
                  username: this.username,
                  password: this.password
                })
            }).then(function(response) { return response.json() } )
            .then(function(data) {
              if (data.error == "invalid credentials") {
                this.message = data.error
              } else {
				        localStorage.setItem("token", data.token)
                router.push({path: '/home'})
                console.log("passed thse router")
              }
			      })
            .catch(error => this.message = "Invalid credentials")
            
            
            }
    }
  }
}
</script>

<style scoped>
body{
  --primaryGreen: #1a472a;
  --secondaryGreen: #2a623d;
  --primaryGrey: #5d5d5d;
  --secondaryGrey: #dddddd;
  --black: 	#000000;
}
.box{
  max-width: 420px;
  margin: 30px auto;
  background-color: white;
  text-align: left;
  padding: 40px;
  border-radius: 10px;
}
label{
  letter-spacing: 1px;
  color: #aaa;
  margin: 25px 0 15px;
  text-transform: uppercase;
  font-weight: bold;
  display: inline-block;
}
input{
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
}
button{
  background: #2a623d;
  color: white;
  padding: 10px;
  margin: 20px;
  border-radius: 20px;
  border: none;
  min-width: 200px;
}
.center {
  margin: 0;
  position:fixed;
  /* top: 50%; */
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>