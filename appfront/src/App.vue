<template>
  <div id="app">
    <el-container style="height: 640px;">
      <el-header style="text-align: left; font-size: 12px">
        <span>璐哥真帅</span>
        <el-dropdown>
          <i class="el-icon-setting" style="margin-left: 15px"></i>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>查看</el-dropdown-item>
            <el-dropdown-item>新增</el-dropdown-item>
            <el-dropdown-item>删除</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-header>
      
      <el-container :span="20" style="height: 580px;">
        <el-aside  style="background-color: rgb(238, 241, 246)">
          <el-menu :default-active="1" class="el-menu-vertical-demo" style="text-align: left">
            <el-submenu index="1">
              <template slot="title"><i class="el-icon-star-on"></i>导航一</template>
              <el-menu-item-group>
                <router-link to="/index"><el-menu-item index="1-1"><i class="el-icon-star-off"></i>Index</el-menu-item></router-link>
                <router-link to="/home"><el-menu-item index="1-2"><i class="el-icon-star-off"></i>Home</el-menu-item></router-link>
                <el-menu-item index="1-3"><i class="el-icon-star-off"></i>选项3</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
              <template slot="title"><i class="el-icon-star-on"></i>导航二</template>
              <el-menu-item-group>
                <router-link to="/mark"><el-menu-item index="2-1"><i class="el-icon-star-off"></i>Mark</el-menu-item></router-link>
                <el-menu-item index="2-2"><i class="el-icon-star-off"></i>选项2</el-menu-item>
                <el-menu-item index="2-3"><i class="el-icon-star-off"></i>选项3</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="3">
              <template slot="title"><i class="el-icon-star-on"></i>导航三</template>
              <el-menu-item-group>
                <el-menu-item index="3-1"><i class="el-icon-star-off"></i>选项1</el-menu-item>
                <el-menu-item index="3-2"><i class="el-icon-star-off"></i>选项2</el-menu-item>
                <el-menu-item index="3-3"><i class="el-icon-star-off"></i>选项3</el-menu-item>
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
