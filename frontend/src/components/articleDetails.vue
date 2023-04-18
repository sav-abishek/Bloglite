<template>
  <div class="container mt-5">
        <h3><b>
            {{ article.title }}
        </b></h3>
        <br>
        <i>
            {{ article.body }}
        </i>
        <br> {{ article.date }}
        <br><button class="btn btn-danger mt-5" @click="deleteArticle">Delete article</button>
  </div>
</template>

<script>
export default {
    data() {
        return {
            article:{}
        }
    },
    props : {
        id: {
            type:[Number, String],
            required:true
        }
    },
    methods: {
        deleteArticle() {
            fetch(`http://127.0.0.1:5000/delete/${this.id}`,{
            method:['DELETE'],
            headers: {
                    "Content-type": "application/json"
                }
            }).then(response => response.json())
            .then(() => {
                this.$router.push({
                    name: 'home'
                })
            })
            .catch(err => console.log(err))
        },

        getArticleById() {
            fetch(`http://127.0.0.1:5000/get/${this.id}/`,{
            method:['GET'],
            headers: {
                    "Content-type": "application/json"
                }
            }).then(response => response.json())
            .then(data => {
                this.article = data
            })
            .catch(err => console.log(err))
        }
    },

    // created() {
    //     this.getArticleById()
    // }
}
</script>

<style>

</style>