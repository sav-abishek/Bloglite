<template>
<div>
<div class="container">
    <navBar/>
    <div v-if="error" class="alert alert-warning alert-dismissible fade show mt-5" role="alert">
        <strong>{{this.error}}</strong>
    </div>
</div>
    <div class="container mt-5" >
        <h1>
            Create a new article
            <br>
        </h1>
        <form @submit.prevent="insertArticles">
        <input class="form-control" placeholder="Type a suitable title for your article" v-model="title">
        <!-- <input type="file" ref="fileInput"  @change="handleFileUpload"> -->
        <textarea class="form-control my-3" rows="5" placeholder="Express your article here..." v-model="description"></textarea>
        
        <button class="center" type="submit">Submit your article</button>
        <!-- <button type="submit">Publish your article</button> -->
        </form>
    </div>
</div>
</template>

<script>
import navBar from './navBar.vue';

export default {
    components: {
        navBar
    },

    data() {
        return {
            title: null,
            description: null,
            // file: null,
            error:null
        }
    },
    methods: {
        // handleFileUpload(event) {
        //     this.file = event.target.files[0];
        // },

        insertArticles() {
            if (!this.title || !this.description) {
                this.error = "Please enter all the fields"
            } else { 
                fetch('http://127.0.0.1:5000/addpost',{
                method: 'POST',
                headers: {
                    'Content-Type': "application/json",
                    // 'Content-Disposition': `attachment; filename=${this.file.name}`,
                    "token": localStorage.getItem("token")
                },
                body: JSON.stringify({
                    'title': this.title,
                    'description': this.description
                })

            })
            .then(resp => resp.json())
            .then(() => {
                this.$router.push({
                    name: 'home'
                })
            })
            .catch(error => {
                this.error = error
            })

            }
            }
        }
}
</script>

<style scoped>
input{
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: #a1aaa4;
  border-bottom: 1px solid #ddd;
  border-block-start-style: dotted;
  color: #834646;
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

</style>