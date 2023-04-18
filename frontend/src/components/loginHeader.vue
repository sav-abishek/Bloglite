<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container mt5">
        <p class="navbar-brand text-style">Welcome to Blog: Get socially appetized</p>

        <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
            <li class="nav-item">
            <router-link class="btn btn-warning container anchor" to="/register">New user? Signup here!</router-link>
            </li>
        </ul>
        </div>
    </div>
    </nav>
</template>

<script>
export default {

}
</script>

<style scoped>
  .text-style {
      font-size: 30px !important;
      font-family: fantasy !important;
      color: rgb(100, 1, 1) !important;
  }
  .anchor {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-weight: bolder;
    color: rgb(0, 0, 0);
    text-decoration: none;
  }
  .anchor:hover {
    color: grey;
    text-decoration: none;
  }
</style>