<template>
    <div>
    <div class="container">
        <navBar/>
        
        
    </div>
        <div class="container mt-5" >
            <h1>
            Discover friends
            </h1>
            <div v-if="error" class="alert alert-info alert-dismissible fade show mt-5" role="alert">
            <strong>{{this.error}}</strong>
        </div>
            <form @submit.prevent="searchUser">
            <input class="form-control" placeholder="Username" v-model="query">          
            <button class="button" type="submit">Search for an user</button>
            </form>
        </div>
        <div class="container mt-2">
            <h1 v-if="search_query.length > 0">
                Search Results
                <br>    
            </h1>
            <div class="row">
            <div class="card mx-4 my-3" v-for="user in search_query">

                <div class="card">
                    <div class="infos">
                        <div class="image"></div>
                        <div class="info">
                            <div>
                                <p class="name">
                                    {{user.username}}
                                </p>
                                <p class="function">
                                    {{user.email}} 
                                </p>
                            </div>
                            <div class="stats">
                                    <p class="flex flex-col">
                                        Articles
                                        <span class="state-value">
                                            {{user.posts}}
                                        </span>
                                    </p>
                                    <p class="flex">
                                        Followers
                                        <span class="state-value">
                                            {{user.followers}}
                                        </span>
                                    </p>
                                    
                            </div>
                        </div>
                    </div>
                    <button  v-if="!isFollowing(user.username)" @click="followFunction(user.username)" class="request-follow">
                            Follow
                    </button>
                    <button v-else @click="unfollowFunction(user.username)" type="button" class="request">
                            Unfollow
                    </button>
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
                query: null,
                search_query: [],
                user_follow: [],
                error:"Begin by typing an username... ",
                following: []
            }
        },
        methods: {
            searchUser() {
                // this.is_following();
                fetch('http://127.0.0.1:5000/search',{
                    method: 'POST',
                    headers: {
                        "Content-type": "application/json",
                        "token": localStorage.getItem("token")
                    },
                    body: JSON.stringify({
                        query: this.query
                    })
                })
                .then(response => response.json())
                .then(response => {
                    this.search_query=[];
                    this.search_query.push(...response)
                })
                .catch(error => {
                    this.error = error
                })
                },

            followFunction(follow_username) {
                fetch(`http://127.0.0.1:5000/follow/${follow_username}`,{
                    method: 'POST',
                    headers: {
                        "Content-type": "application/json",
                        "token": localStorage.getItem("token")
                    }
                })
                .then(response => response.json())
                .then(response => {
                    fetch('http://127.0.0.1:5000/is_following',{
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                        "token": localStorage.getItem("token")
                    }
                }).then(resp => resp.json())
                .then(response => {
                this.following.push(...response)
                this.searchUser()
                this.error = `Succesfully followed ${follow_username}`  
                })

                })
                .catch(error => {
                    this.error = error
                })
            },

            unfollowFunction(unfollow_username) {
                fetch(`http://127.0.0.1:5000/unfollow/${unfollow_username}`,{
                    method: 'POST',
                    headers: {
                        "Content-type": "application/json",
                        "token": localStorage.getItem("token")
                    }
                })
                .then(response => response.json())
                .then(response => {
                    const index = this.following.findIndex(u => u.id === unfollow_username.id);
                    this.following.splice(index, 1);
                    this.error = `Succesfully unfollowed ${unfollow_username}`  
                    this.searchUser()              
                })
                .catch(error => {
                    this.error = error
                })
            },
        
            isFollowing(name) {
                return this.following.some(user => user.following === name);
                }
        },
        beforeMount() {
            fetch('http://127.0.0.1:5000/is_following',{
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                        "token": localStorage.getItem("token")
                    }
                }).then(resp => resp.json())
                .then(response => this.following.push(...response))

            }
    }
    
    </script>
    
    <style scoped>
    .card {
    max-width: 320px;
    border-radius: 1rem;
    background-color: rgba(31, 41, 55, 1);
    padding: 1rem;
    }

    .infos {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    grid-gap: 1rem;
    gap: 1rem;
    }

    .image {
    height: 7rem;
    width: 7rem;
    border-radius: 0.5rem;
    background-color: rgb(118, 36, 194);
    background: linear-gradient(to bottom right, rgb(118, 36, 194), rgb(185, 128, 240));
    }

    .info {
    height: 7rem;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    }

    .name {
    font-size: 1.25rem;
    line-height: 1.75rem;
    font-weight: 500;
    color: rgba(255, 255, 255, 1);
    }

    .function {
    font-size: 0.75rem;
    line-height: 1rem;
    color: rgba(156, 163, 175, 1);
    }

    .stats {
    width: 100%;
    border-radius: 0.5rem;
    background-color: rgba(255, 255, 255, 1);
    padding: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.75rem;
    line-height: 1rem;
    color: rgba(0, 0, 0, 1);
    }

    .flex {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 4px;
    }

    .state-value {
    font-weight: 700;
    color: rgb(118, 36, 194);
    }

    .request {
    margin-top: 1.5rem;
    width: 100%;
    border: 1px solid transparent;
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    line-height: 1.5rem;
    background-color: rgb(209, 179, 237);
    transition: all .3s ease;
    }

    .request:hover {
    background-color: rgb(104, 85, 121);
    color: #fff;
    }
    .request-follow {
    margin-top: 1.5rem;
    width: 100%;
    border: 1px solid transparent;
    background-color: rgb(219, 118, 183);
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    line-height: 1.5rem;
    transition: all .3s ease;
    }

    .request-follow:hover {
    background-color: rgb(160, 34, 116);
    color: #fff;
    }


    input{
      display: block;
      padding: 10px 6px;
      width: 35%;
      box-sizing: border-box;
      border: #a1aaa4;
      border-bottom: 1px solid #ddd;
      border-block-start-style: dotted;
      color: #834646;
    }
    .button{
      background: #2a623d;
      color: white;
      padding: 10px;
      margin: 20px;
      border-radius: 20px;
      border: none;
      min-width: 200px;
    }

    
    </style>