<template id="logout">
  <div class="logout" style="width: 510px;margin-left: 269px;margin-top: 20px;">
    <el-radio-group v-model="labelPosition" size="small">
        <el-radio-button label="left">左对齐</el-radio-button>
        <el-radio-button label="right">右对齐</el-radio-button>
        <el-radio-button label="top">顶部对齐</el-radio-button>
    </el-radio-group>
    <div style="margin: 20px;"></div>
    <el-form :label-position="labelPosition" label-width="80px" :model="loginFrom" :rules="rules" :ref="loginFrom">
        <el-form-item label="邮箱"  prop="user_email">
            <el-input  v-model="loginFrom.user_email" ref="user_email"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="user_pwd">
            <el-input v-model="loginFrom.user_pwd" ref="user_pwd"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit(loginFrom)">切换用户</el-button>
        </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  '/logout': 'Logout',
  data() {
      return {
        labelPosition: 'right',
        loginFrom: [{
          model: '',
          pk: '',
          fields:{
            user_name: '',
            password: '',
            user_email: '',
            user_phone: ''
          }
        }],
        dataList:[],
        rules:{
            user_email: [
            { required: true, message: '请输入你的邮箱', trigger: 'blur' },
            { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
            ],
            user_pwd: [
                { required: true, message: '请输入你的密码', trigger: 'blur' },
                { min: 0, max: 20, message: '长度在 0 到 20 个字符', trigger: 'blur' }
            ]
        }
      };
    },
    methods: {
      onSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            var data = this.$refs[formName];
            this.$http.get('http://127.0.0.1:8000/web/check_user',{params: {"user_email":this.loginFrom.user_email, "user_pwd":this.loginFrom.user_pwd} })
            .then((response) => {
                var res = JSON.parse(response.bodyText)
                if (res.error_num == 0) {
                    this.loginFrom = res['list']
                    console.log("aaaaaaaaaaaaa",this.loginFrom)
                    this.dataList = res['list']
                    console.log("sssssssssssss",this.dataList)
                    this.$message.success('登录成功: ' + res['msg'])
                } else {
                    this.$message.error('登录失败:' + res['msg'])
                    console.log(res['msg'])
                }
            })
          } else {
            return false;
          }
        });
      }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

