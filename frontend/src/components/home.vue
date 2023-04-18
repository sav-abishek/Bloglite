<template>
<div>
    <navBar/>
  <div class="container mt-5">
    <h1>Dashboard</h1>
    <div class="row">
    <div class="card mx-3 my-3" v-for="post in posts">
    <div class="card-img"></div>
    <div class="card-info">
        <p class="text-title"> {{ post.title }} </p>
        <p class="text-body"> {{ post.description }}</p>
    </div>
    <div class="card-footer">
    <!-- <span class="text-title">Count</span> -->
    <button v-if="isliked(post.id)" @click="like_post(post.id)" class="card-button">
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-hand-thumbs-up" viewBox="0 0 16 16">
        <path d="M8.864.046C7.908-.193 7.02.53 6.956 1.466c-.072 1.051-.23 2.016-.428 2.59-.125.36-.479 1.013-1.04 1.639-.557.623-1.282 1.178-2.131 1.41C2.685 7.288 2 7.87 2 8.72v4.001c0 .845.682 1.464 1.448 1.545 1.07.114 1.564.415 2.068.723l.048.03c.272.165.578.348.97.484.397.136.861.217 1.466.217h3.5c.937 0 1.599-.477 1.934-1.064a1.86 1.86 0 0 0 .254-.912c0-.152-.023-.312-.077-.464.201-.263.38-.578.488-.901.11-.33.172-.762.004-1.149.069-.13.12-.269.159-.403.077-.27.113-.568.113-.857 0-.288-.036-.585-.113-.856a2.144 2.144 0 0 0-.138-.362 1.9 1.9 0 0 0 .234-1.734c-.206-.592-.682-1.1-1.2-1.272-.847-.282-1.803-.276-2.516-.211a9.84 9.84 0 0 0-.443.05 9.365 9.365 0 0 0-.062-4.509A1.38 1.38 0 0 0 9.125.111L8.864.046zM11.5 14.721H8c-.51 0-.863-.069-1.14-.164-.281-.097-.506-.228-.776-.393l-.04-.024c-.555-.339-1.198-.731-2.49-.868-.333-.036-.554-.29-.554-.55V8.72c0-.254.226-.543.62-.65 1.095-.3 1.977-.996 2.614-1.708.635-.71 1.064-1.475 1.238-1.978.243-.7.407-1.768.482-2.85.025-.362.36-.594.667-.518l.262.066c.16.04.258.143.288.255a8.34 8.34 0 0 1-.145 4.725.5.5 0 0 0 .595.644l.003-.001.014-.003.058-.014a8.908 8.908 0 0 1 1.036-.157c.663-.06 1.457-.054 2.11.164.175.058.45.3.57.65.107.308.087.67-.266 1.022l-.353.353.353.354c.043.043.105.141.154.315.048.167.075.37.075.581 0 .212-.027.414-.075.582-.05.174-.111.272-.154.315l-.353.353.353.354c.047.047.109.177.005.488a2.224 2.224 0 0 1-.505.805l-.353.353.353.354c.006.005.041.05.041.17a.866.866 0 0 1-.121.416c-.165.288-.503.56-1.066.56z"/>
        </svg>
    </button>
    <button v-else @click="like_post(post.id)" class="card-button">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-hand-thumbs-up-fill" viewBox="0 0 16 16">
        <path d="M6.956 1.745C7.021.81 7.908.087 8.864.325l.261.066c.463.116.874.456 1.012.965.22.816.533 2.511.062 4.51a9.84 9.84 0 0 1 .443-.051c.713-.065 1.669-.072 2.516.21.518.173.994.681 1.2 1.273.184.532.16 1.162-.234 1.733.058.119.103.242.138.363.077.27.113.567.113.856 0 .289-.036.586-.113.856-.039.135-.09.273-.16.404.169.387.107.819-.003 1.148a3.163 3.163 0 0 1-.488.901c.054.152.076.312.076.465 0 .305-.089.625-.253.912C13.1 15.522 12.437 16 11.5 16H8c-.605 0-1.07-.081-1.466-.218a4.82 4.82 0 0 1-.97-.484l-.048-.03c-.504-.307-.999-.609-2.068-.722C2.682 14.464 2 13.846 2 13V9c0-.85.685-1.432 1.357-1.615.849-.232 1.574-.787 2.132-1.41.56-.627.914-1.28 1.039-1.639.199-.575.356-1.539.428-2.59z"/>
        </svg>
    </button>
    </div></div>
</div>
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
        return{
            posts:[],
        }
    },

    methods: {

        getArticles() {
            fetch('http://127.0.0.1:5000/dashboard_posts',{
                method: 'GET',
                headers: {
                    "Content-type": "application/json",
                    "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .then(response => this.posts.push(...response))
            .catch(error => {
                console.log(error)
                // this.error = error[error]
            })
        },

        like_post(id) {
            fetch(`http://127.0.0.1:5000/like/${id}`, {
                method: 'GET',
                headers: {
                    "Content-type": "application/json",
                    "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .catch(error => {
                console.log(error)
                // this.error = error[error]
            })
        },

        unlike_post(id) {
            fetch(`http://127.0.0.1:5000/unlike/${id}`, {
                method: 'GET',
                headers: {
                    "Content-type": "application/json",
                    "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .catch(error => {
                console.log(error)
            })
        },

        isliked(id) {
            fetch(`http://127.0.0.1:5000/is_liked/${id}`, {
                method: 'GET',
                headers: {
                    "Content-type": "application/json",
                    "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .then(resp => {
                console.log(resp.message)
                return resp.message
            })
        }   

    },

    created() {
        this.getArticles()
    }

}
</script>

<style scoped>
.card {
 width: 300px;
 height: 400px;
 padding: .8em;
 background: #f5f5f5;
 position:-ms-;
 overflow: visible;
 box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}

.card-img {
 background-color: #ffcaa6;
 height: 40%;
 width: 100%;
 border-radius: .5rem;
 transition: .3s ease;
}

.card-info {
 padding-top: 10%;
}

svg {
 width: 20px;
 height: 20px;
}

.card-footer {
 width: 100%;
 display: flex;
 justify-content: space-between;
 align-items: center;
 padding-top: 10px;
 border-top: 1px solid #ddd;
}

/*Text*/
.text-title {
 font-weight: 900;
 font-size: 1.2em;
 line-height: 1.5;
}

.text-body {
 font-size: .9em;
 padding-bottom: 10px;
}

/*Button*/
.card-button {
 border: 1px solid #252525;
 display: flex;
 padding: .3em;
 cursor: pointer;
 border-radius: 50px;
 transition: .3s ease-in-out;
}

/*Hover*/
.card-img:hover {
 transform: translateY(-25%);
 box-shadow: rgba(226, 196, 63, 0.25) 0px 13px 47px -5px, rgba(180, 71, 71, 0.3) 0px 8px 16px -8px;
}

.card-button:hover {
 border: 1px solid #ffcaa6;
 background-color: #ffcaa6;
}



.link-style {
    font-weight: bolder;
    color: black;
    text-decoration: none;
}
.link-style:hover {
    color: grey;
    text-decoration: none;
}

</style>