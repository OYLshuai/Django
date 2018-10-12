<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  margin:0px;
  position:absolute;
  top:0px;
  left:0px;
  width:100%;
  height:100%;
  border:hidden;
}
</style>
