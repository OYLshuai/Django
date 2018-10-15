<template>
  <div id="app">
    <el-container style="height: 640px;">
      <el-header style="text-align: left; font-size: 12px">
        <span style="padding-left: 5px;" >璐哥真帅</span>
        <el-dropdown>
          <i class="el-icon-setting" style="margin-left: 15px"></i>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>个人信息  <i class="el-icon-view"></i></el-dropdown-item>
            <el-dropdown-item>未读消息  <i class="el-icon-phone-outline"></i></el-dropdown-item>
            <el-dropdown-item>退出登录  <i class="el-icon-circle-close"></i></el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <img src="./assets/image/logo.png" style="width: 120px;padding-left: 1100px;float: right;padding-top: 4px;">
      </el-header>
      
      <el-container :span="20" style="height: 580px;">
        <el-aside  style="background-color: rgb(238, 241, 246)">
          <el-menu class="el-menu-vertical-demo" style="text-align: left">
            <el-submenu index="1">
              <template slot="title"><i class="el-icon-menu"></i>菜单</template>
              <el-menu-item-group>
                <router-link to="/index"><el-menu-item index="1-1">首页</el-menu-item></router-link>
                <router-link to="/home"><el-menu-item index="1-2">书籍管理</el-menu-item></router-link>
                <el-menu-item index="1-3">待定</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
              <template slot="title"><i class="el-icon-news"></i>查询</template>
              <el-menu-item-group>
                <router-link to="/mark"><el-menu-item index="2-1">Mark</el-menu-item></router-link>
                <el-menu-item index="2-2">待定</el-menu-item>
                <el-menu-item index="2-3">待定</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="3">
              <template slot="title"><i class="el-icon-setting"></i>设置</template>
              <el-menu-item-group>
                <el-menu-item index="3-1">待定</el-menu-item>
                <el-menu-item index="3-2">待定</el-menu-item>
                <el-menu-item index="3-3">待定</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-main>
          <!--用于渲染匹配的组件-->
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      imgUrl:'./assets/image/logo.jpg'
    }
  }
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

a {
  text-decoration: none;
}

.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
  }
  
 .el-aside {
  color: #333;
 }

 .el-menu {
   border-right-width: 0px;
 }
</style>
