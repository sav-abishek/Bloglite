<script>
export default{
    name:'follower'
}
</script>
<template>
    <p style="text-align: center;">Bloglite</p>
    <div class="f">
    <div class="container">
      <h1>Followers</h1>
      <p class="follower-count">1000</p>
      <h2>Followers List:</h2>
        <div class="follower-list"><img src ="../../static/a4.png"><p style="text-align:center">Vivek</p><button id="follow-button">Unfollow</button></div>
        <div class="follower-list"><img src ="../../static/a4.png"><p style="text-align:center">Devesh</p><button id="follow-button">Unfollow</button></div>
        <div class="follower-list"><img src ="../../static/a4.png"><p style="text-align:center">koi pagal</p><button id="follow-button">Unfollow</button></div>
    </div>
    <div class="container1">
        <h1>Following</h1>
        <p class="follower-count">1000</p>
        <h2>Following List:</h2>
        <div class="follower-list"><img src ="../../static/a4.png"><p style="text-align:center">Vivek</p><button id="follow-button">+ Follow</button></div>
        <div class="follower-list"><img src ="../../static/a4.png"><p style="text-align:center">Devesh</p><button id="follow-button">+ Follow</button></div>
        <div class="follower-list"><img src ="../../static/a4.png"><p style="text-align:center">koi pagal</p><button id="follow-button">+ Follow</button></div>
          
      </div>
    </div>
</template>

<style scoped>
  img{
  height: 50px;
  width: 50px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  margin-right: 15px;
}
#follow-button {
  color: #3399FF;
  font-family: "Helvetica";
  font-size: 10pt;
  background-color: #ffffff;
  border: 1px solid;
  border-color: #3399FF;
  border-radius: 3px;
  width: 85px;
  height: 20px; 
  top: 50px;
  left: 50px;	
  cursor: hand;		 
  text-align:center;  
  margin-left: 10%;
}
.container {
  display: flex;
  flex-direction: column;
  align-items: left;
  
}
.container1{
  display: flex;
  flex-direction: column;
  align-items: right;

}
.f{
    display: flex;
    flex-direction: row;
    align-items: right;
    justify-content: space-between;
    padding-left: 10%;
    padding-right: 5%;
}

.follower-count {
  font-size: 48px;
  font-weight: bold;
  margin-top: 5px;
}

.follower-list {
  width: 300px;
  height: 50px;
  box-shadow: rgba(64, 126, 157, 0.25) 0px 25px 50px -12px;
  margin-top: 10px;
  margin-bottom: 15px;
  font-size: 18px;
  list-style-type: none;
  color: rgb(1, 1, 10);
  padding-bottom: 2%;
  padding-top: 1%;
  display: flex;
  text-transform: uppercase;
  align-items: center;
}

</style>

