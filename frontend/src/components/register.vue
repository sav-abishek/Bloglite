<template>
    <div class="body container">
      <registerHeader/>
      
    <div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5" role="alert">
    <strong>{{this.error}}</strong>
    </div>

      <div class="box">
       <form @submit.prevent="registerMe">
            <br>
            <input type="text" v-model="name" name="name" placeholder="Name" required>
            <br>
            <input type="email" v-model="email" name="email" placeholder="Email" required>
            <br>
            <input type="text" v-model="username" name="username" placeholder="Username" required>
            <br>
            <input type="password" v-model="password" name="password" placeholder="Password" required>
            <br><br>
            <button class="center" type="submit">Register</button>

        </form>
      </div>    
  </div>
</template>
  
<script>
import registerHeader from './registerHeader.vue';
import loginFooter from './loginFooter.vue';
import login from './login.vue';

  export default {
    components: {
      registerHeader,
      loginFooter
    },

    data() {
      return {
        name: null,
        email: null,
        username: null,
        password: null,
        error: 'Please register yourself'
      }
    },
  
    methods: {
      registerMe() {
        if (!this.username || !this.password) {
                  this.error = "Please enter all the fields"
                  
              } else { fetch('http://127.0.0.1:5000/register',{
                  method: 'POST',
                  headers: {
                      "Content-type": "application/json"
                  },
                  body: JSON.stringify({
                    email: this.email,
                    username: this.username,
                    password: this.password
                  })
              })
              .then(resp => resp.json())
              .then(() => {
                  this.$router.push('/login')
              })
              .catch(error => {
                  this.error = error["error"]
                  // console.log(error)
              })
  
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
  .form-signin {
    width: 100%;
    max-width: 330px;
    padding: 15px;
    margin: 0 auto;
  }
  .form-signin .checkbox {
    font-weight: 400;
  }
  .form-signin .form-control {
    position: relative;
    box-sizing: border-box;
    height: auto;
    padding: 10px;
    font-size: 16px;
  }
  .form-signin .form-control:focus {
    z-index: 2;
  }
  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
</style>