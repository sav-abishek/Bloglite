<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container mt8">
    <button class="btn btn-basic" >
    <p class="navbar-brand footer"> Made with :3 by Abishek Vinodh</p>
    </button>
    <ul class="navbar-nav ms-auto">
        <li class="nav-item">
            <button class="btn btn-danger">
            <a class="anchor" href="">Check out my Source Code</a>
            </button>
        </li>
        <li>
        </li>
        <li class="nav-item">
            <button class="btn btn-primary">
            <a class="anchor" href="">Let's connect on LinkedIN</a>
            </button>
        </li>
      </ul>

    <!-- <span class="navbar-toggler-icon"></span>
    <div class="collapse navbar-collapse" id="navbarNav"> -->
      <!-- <ul class="navbar-nav ms-auto">
        <li class="nav-item">
            <router-link class="btn btn-success container " to="/">Home</router-link> 
        </li>
        <li class="nav-item">
          <router-link class="btn btn-primary container" to="/create">Create</router-link>
        </li>
      </ul> -->
    <!-- </div> -->
  </div>
</nav>
</template>

<script>
export default {

}
</script>

<style scoped>
  .footer {
      font-size: 18px !important;
      font-family: fantasy !important;
      color: rgb(0, 0, 0) !important;
      text-align:right;
  }

  .anchor {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-weight: bolder;
    color: white;
    text-decoration: none;
  }
  .anchor:hover {
    color: grey;
    text-decoration: none;
  }
</style>