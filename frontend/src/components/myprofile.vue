<template>
<div>
    
    <navBar/>
  <div class="container mt-5">
    <div class="row container ">
        <h1>
            My Profile
        </h1>
        <hr>
        <div class="profile-card mx-5 my-4">
        <div class="profile-info">
            <!-- <p class="profile-body"> Email ID</p> -->
            <p class="profile-title"> {{ profile.username }} <br>
             {{ profile.email }} </p>
        </div>
        </div>

        <div class="profile-card mx-3 my-4">
        <div class="profile-info">
            <!-- <p class="profile-body"> Email ID</p> -->
            <p class="profile-title"> Posts <br>
                 {{ profile.posts }} </p>
        </div>
        </div>

        <div class="profile-card mx-3 my-4">
        <div class="profile-info">
            <!-- <p class="profile-body"> Email ID</p> -->
            <p class="profile-title"> Followers <br>
                 {{ profile.followers }} </p>
        </div>
        </div>

        <div class="profile-card mx-3 my-4">
        <div class="profile-info">
            <!-- <p class="profile-body"> Email ID</p> -->
            <p class="profile-title"> Following <br>
                 {{ profile.following }} </p>
        </div>
        </div>
        
    </div>
    
    <div class="row container">
        <div class="container mt-5">
        <h3 >
            
  
        <button @click="export_profile()" class="export-button ms-auto">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-download" viewBox="0 0 16 16">
            <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/>
            <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/>
            </svg>
            
        </button>
        <button @click="send_mail()" class="export-button ms-auto">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-envelope-paper-heart-fill" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="m3 7.5 3.5 2L8 8.75l1.5.75 3.5-2v-6A1.5 1.5 0 0 0 11.5 0h-7A1.5 1.5 0 0 0 3 1.5v6ZM2 3.133l-.941.502A2 2 0 0 0 0 5.4v.313l2 1.173V3.133Zm12 3.753 2-1.173V5.4a2 2 0 0 0-1.059-1.765L14 3.133v3.753Zm-3.693 3.324L16 6.873v6.5l-5.693-3.163Zm5.634 4.274L8 10.072.059 14.484A2 2 0 0 0 2 16h12a2 2 0 0 0 1.941-1.516ZM5.693 10.21 0 13.372v-6.5l5.693 3.338ZM8 1.982C9.664.309 13.825 3.236 8 7 2.175 3.236 6.336.31 8 1.982Z"/>
            </svg>
            
        </button>
        My recent posts
    </h3>
    </div>
        <hr>
        <div v-if="error" class="alert alert-warning alert-dismissible fade show mt-1" role="alert">
            <strong>{{this.error}}</strong>
            <!-- <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button> -->
        </div>
        <div class="card mx-3 my-3" v-for="post in posts">
        <div class="card-img"></div>
        <div class="card-info">
            <p class="text-title"> {{ post.title }} </p>
            <p class="text-body"> {{ post.description }}</p>
        </div>
            <div class="card-footer">
                
            <!-- Button trigger modal for EDIT-->
            <button @click="triggerBinding(post.title, post.description, post.id)" type="button" class="card-button" data-bs-toggle="modal" data-bs-target="#staticBackdropedit">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                </svg>
            Edit
            </button>

            <!-- Modal for EDITING -->
            <div class="modal fade" id="staticBackdropedit" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Edit your blog</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <input class="form-control"  v-model="title">
                    <textarea class="form-control my-3" rows="5" v-model="description"></textarea>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button @click="editArticle(post.id)" type="button" data-bs-dismiss="modal" class="btn btn-primary">Submit</button>
                </div>
                </div>
            </div>
            </div>
            
            <!-- Button trigger modal for DELETE -->
            <button type="button" @click="triggerBinding(post.title, post.description, post.id)" class="card-button-delete" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>
                </svg>
            Delete
            </button>

            <!-- Modal -->
            <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Confirm delete?</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body" >
                    <p class="text-title"> {{ this.title }} </p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button @click="deleteArticle(post.id)" type="button" class="btn btn-danger" data-bs-dismiss="modal">Submit</button>
                </div>
                </div>
            </div>
            </div>
            </div>
        </div>
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
        return {
            profile: {},
            posts: [],
            error: null,
            title: "Title",
            description: "Description",
            post_id: null
        }
    },

    methods : {
        getArticles() {
            fetch('http://127.0.0.1:5000/myposts',{
                method: 'GET',
                headers: {
                    "Content-type": "application/json",
                    "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .then(response => {
                this.posts = [];
                this.posts.push(...response)
            })
            .catch(error => {
                console.log(error)
                // this.error = error[error]
            })
        },

        getProfile() {
            fetch('http://127.0.0.1:5000/myprofile',{
                method: 'GET',
                headers: {
                    "Content-type": "application/json",
                    "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .then(response => {
                // this.profile.push(...response)
                this.profile = response
            })
            .catch(error => {
                console.log(error)
                // this.error = error[error]
            })
        },

        triggerBinding(title, desc, id) {
            this.title = title;
            this.description = desc, 
            this.post_id = id
        },

        editArticle() {
            fetch(`http://127.0.0.1:5000/edit/${this.post_id}`,{
                method: 'POST',
                headers: {
                    "Content-type": "application/json",
                    "token": localStorage.getItem("token")
                }, body: JSON.stringify({
                    title: this.title, 
                    description: this.description
                })
            })
            .then(response => response.json())
            .then(response => {
                // this.profile.push(...response)
                this.getArticles()
                // this.error = response.message
            })
            .catch(error => {
                console.log(error)
                this.error = error.error
            })
        },

        deleteArticle() {
            fetch(`http://127.0.0.1:5000/delete/${this.post_id}`,{
                method: 'GET',
                headers: {
                    "Content-type": "application/json",
                    "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .then(response => {
                this.getArticles()
                this.error = response.message
            })
            .catch(error => {
                console.log(error)
                this.error = error.error
            })
        },

        export_profile() {
            fetch('http://127.0.0.1:5000/export_csv',{
                method: "GET",
                headers: {
                "Content-type": "application/json",
                "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .then(response => {
                console.log("celery task details:", response);
                setTimeout(() => {
                    window.location.href = "http://127.0.0.1:5000/download_file";
                }, 6000)
            })     
        },

        send_mail() {
            fetch('http://127.0.0.1:5000/monthly_report',{
                method: "GET",
                headers: {
                "Content-type": "application/json",
                "token": localStorage.getItem("token")
                }
            })
            .then(response => response.json())
            .then(response => response.json())
        }
    },

    mounted() {
        this.getProfile();
        this.getArticles()
    }
}
</script>

<style scoped>
.export-button{
  background: #bd6415;
  color: white;
  padding: 5px;
  margin: 2px;
  border-radius: 10px;
  border: none;
  width: 50px;
  text-decoration: none;
}
.export-button:hover{
  background: #cc762b;
  color: rgb(90, 87, 87);
  padding: 5px;
  margin: 2px;
  border-radius: 10px;
  border: none;
  width: 50px;
  text-decoration: none;
}
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

/* CSS STYLING FOR PROFILE INFO */
.profile-card {
 width: 250px;
 height: 100px;
 padding: 0.8em;
 border: 0cm;
 background: none;
 position:-ms-;
 overflow: visible;
 text-align: center;

}

.profile-info {
 background-color: #ffcaa6;
 height: 100%;
 width: 100%;
 border-radius: .5rem;
 transition: .3s ease;
}
.profile-info:hover {
 transform: translateY(-15%);
 box-shadow: rgba(226, 196, 63, 0.25) 0px 13px 47px -5px, rgba(180, 71, 71, 0.3) 0px 8px 16px -8px;
}
.profile-title {
    font-weight: 900;
    font-size: 1.2em;
}

/* CSS STYLING FOR USER POSTS */
.card {
 width: 400px;
 height: 450px;
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
 padding: .5em;
 cursor: pointer;
 border-radius: 10px;
 transition: .2s ease-in-out;
}
.card-button-delete {
 border: 1px solid #252525;
 display: flex;
 padding: .5em;
 cursor: pointer;
 border-radius: 10px;
 transition: .2s ease-in-out;
}
.card-button-delete:hover {
    color: #f5f5f5;
 border: 1px solid #ffcaa6;
 background-color: #c4480a;
}
.card-button:hover {
    color: #f5f5f5;
 border: 1px solid #ffcaa6;
 background-color: #08644d;
}
/*Hover*/
.card-img:hover {
 transform: translateY(-25%);
 box-shadow: rgba(226, 196, 63, 0.25) 0px 13px 47px -5px, rgba(180, 71, 71, 0.3) 0px 8px 16px -8px;
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