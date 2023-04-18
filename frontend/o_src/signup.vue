<script>
export default{
  name:'SignUp',
  data(){
    return {
      email_id:"",
      fullname:"",
      user_name:"",
      password:""
    }
  },
  methods:{
    SignUp(){
      console.log("yes",this.email_id)
    }
  }
}
</script>

<template>
  <div class="hello">
      <span id="root">
      <section class="section-all">
  
        <!-- 1-Role Main -->
        <main class="main">
          <div class="wrapper">
            <article class="article">
              <div class="content">
                <div class="login-box">
                  <div class="header">
                     <p style="font-family: Apple Chancery, cursive; font-size: 24px;">Bloglite</p> -->
                  </div><!-- Header end -->
                  <div class="form-wrap">
                    <form class="form">
  
                      <div class="input-box">
                        <input type="text" placeholder="email" v-model="email_id" required> 
                      </div>  
                      <div class="input-box">
                        <input type="text" placeholder="fullname" v-model="fullname" required> 
                      </div> 
                      <div class="input-box">
                        <input type="text" placeholder="user_name" v-model="user_name" required> 
                      </div>
                      <div class="input-box">
                        <input type="password" placeholder="password" v-model="password" required> 
                      </div>  
  
                      <span class="button-box">
                        <button class="btn" v-on:click="Signup">Sign up</button> 
                      </span>  
  
                      
                    </form>
                  </div> <!-- Form-wrap end -->
                </div> <!-- Login-box end -->
  
                <div class="login-box">
                  <p class="text">Do have an account?<a href="#">Sign in</a></p>
                </div> <!-- Signup-box end -->
  
                
              </div> <!-- Content end -->
            </article>
        </div> <!-- Wrapper end -->
    </main>

    <!-- 2-Role Footer -->
      <div class="footer-container">
        <p class="glow">We hope you have a pleasant time with us</p> 

        <nav class="footer-nav" role="navigation">
        </nav>

      </div> <!-- Footer container end -->
    
    
  </section>
</span> <!-- Root -->
  </div>
  
</template>

<style scoped>
/* Universal Selectors */
#root, body, html {
  height:100%;
}

body {
  overflow-y: scroll;
}

a, abbr, acronym, address, applet, article, aside, audio, b, big, blockquote, body, canvas, caption, center, cite, code, dd, del, details, dfn, div, dl, dt, em, embed, fieldset, figcaption, figure, footer, form, h1, h2, h3, h4, h5, h6, header, hgroup, html, i, iframe, img, ins, kbd, label, legend, li, mark, menu, nav, object, ol, output, p, pre, q, ruby, s, samp, section, small, span, strike, strong, sub, summary, sup, table, tbody, td, tfoot, th, thead, time, tr, tt, u, ul, var, video {
  margin:0;
  padding:0;
  border:0;
  font:inherit;
  vertical-align: baseline;
} 

a, a:visited {
  text-decoration: none;
}
a:active, .btn:active {
  opacity:.5;
}

ol, ul {
  list-style: none;
}

body, button, input {
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:14px;
  line-height:18px;
}
#root, article, main, div, section, header, nav, footer {
    border: 0 solid #000000;
    box-sizing: border-box;
    align-items: stretch;
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    margin:0;
    padding:0;
    position: relative;
    -webkit-box-align: stretch;
      -moz-box-align: stretch;
    -webkit-box-orient: vertical;
      -moz-box-orient: vertical;
    -webkit-box-direction: normal;
      -moz-box-direction: normal;
  } /* <--Universal Selectors End */
  
  
  #root {
    z-index: 0;
  }
  
  .section-all {
    min-height:100%;
    overflow:hidden;
  }
  
  .main {
    background-image: url('../../static/j.png');
    background-size: cover;
    flex-grow: 1;
    -webkit-box-flex: 1;
    -moz-box-flex: 1;
    -moz-box-ordinal-group: 5;
    -webkit-box-ordinal-group: 5;
  }
  
  .wrapper {
    min-height:100%;
    overflow: hidden;
  }
  .wrapper, .article {
    flex-grow: 1;
    justify-content: center;
    -webkit-box-flex: 1;
      -moz-box-flex: 1;
    -webkit-box-pack: center;
      -moz-box-pack: center;
  }
  
  .article {
    flex-direction: row;
    margin:0 auto;
    max-width: 935px;
    width:100%;
    -webkit-box-orient: horizontal;
      -moz-box-orient: horizontal;
    -webkit-box-direction: normal;
      -moz-box-direction: normal;
  }
  
  .content {
    color:#3847d3;
    flex-grow:1;
    justify-content: center;
    max-width: 350px;
    margin-top:12px;
    -webkit-box-pack: justify;
      -moz-box-pack: justify;
    -webkit-box-flex: 1;
      -moz-box-flex: 1;  
  }
  .login-box {
    background:#bde4fe;
    border: 1px solid #e6e6e6;
    border-radius: 1px;
    margin:0 0 10px;
    padding: 10px 0;
    /* align-items: center; */
  }
  
  .header {
    margin: 14.45px auto 12px;
  }
  
  .logo {
    background: cover no-repeat;
    width:175px;
    height:auto;
  }
  
  .form {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
    -moz-box-direction: normal;
    -webkit-box-direction: normal;
  }
  
  .input-box {
    margin:auto 40px 6px;
  }
  
  input {
    height: 36px;
    border: 1px solid #efefef;
    border-radius: 3px;
    background-color: #fafafa;
    width:100%;
    font-size:12px;
    padding: 9px 0 7px 8px;
  outline: none;
  overflow: hidden;
  text-overflow: ellipsis;
  box-sizing: border-box;
}
input#name:focus, input#password:focus {
  border-color:#bbb;
}

.button-box {
  display: block;
  position: relative;
  margin: 8px 40px;
  background-color: #007C7A;
}
.btn {
  cursor: pointer;
  width: 100%;
  padding:0 8px; 
  background: #527ea2;
  border:1px solid #9bc9f4;
  color:#fff;
  border-radius:3px;
  font-weight:600;
  font-size: 14px;
  height: 28px;
  line-height: 26px;
  outline: none;
  white-space: nowrap;
}

.text {
    text-align:center;
    margin:15px;
    color:#394ae6;
    font-size:14px;
  }
  
  .text a, .text a:visited, .text a:hover, .text a:active {
    color:#08335a;
    margin-left:3px;
  }
  
  /* App Store */
  
  /* FOOTER */
  
  .footer-container {
    flex-direction: row;  
    background-color: rgb(248, 242, 248);
    
    padding: 38px 0;
    max-width:100%;
    font-size:12px;
    font-weight:600;
    margin:0 auto;
    text-transform:uppercase;
    width:100%;
  }

  
  
  
  .footer-nav ul li {
    display: inline-block;
    margin-right: 13px;
    margin-bottom:7px;
}

.glow {
  font-size: 30px;
  color: #fff;
  text-align: center;
  animation: glow 1s ease-in-out infinite alternate;
  padding-left: 30%;
}

@-webkit-keyframes glow {
  from {
    text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #60baf6, 0 0 40px #4ecde9, 0 0 50px #45c1d6, 0 0 60px #46f3f6, 0 0 70px #8af0f4;
  }
  
  to {
    text-shadow: 0 0 20px #fff, 0 0 30px #007C7A, 0 0 40px #007C7A, 0 0 50px #007C7A, 0 0 60px #007C7A, 0 0 70px #007C7A, 0 0 80px #007C7A;
  }
}







  
</style>

