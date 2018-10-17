<template id="info">
  <div class="info" style="">
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card shadow="hover">
          <el-row>
            <el-col :span="24" >
              <el-tag>姓名：</el-tag> <el-tag type="success">{{ textUser.userInfo.name }}</el-tag>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="24">
              <el-tag>邮箱：</el-tag> <el-tag type="success">{{ textUser.userInfo.email }}</el-tag>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="24">
              <el-tag>电话：</el-tag> <el-tag type="success">{{ textUser.userInfo.phone }}</el-tag>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover">
          鼠标悬浮时显示
        </el-card>
      </el-col>
    </el-row>
    
    
  </div>
</template>

<script>
export default {
  '/info': 'Info',
  data(){
    return {
      textUser : this.$store.state,
      userInfo: {
        name : "",
        phone : "",
        email:"",
      }
    }
  },
  mounted(){
    //组件开始挂载时获取用户信息
    this.getUserInfo();

  },

  methods: {
    getUserInfo:function(){
      this.userInfo.name = this.$route.params.name;
      this.userInfo.phone = this.$route.params.phone;
      this.userInfo.email = this.$route.params.email;
    }
  },
  watch: {
  // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
    '$route': 'getUserInfo'
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-col{
  padding-top: 10px;
}
</style>

