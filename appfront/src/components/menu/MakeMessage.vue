<template id="makeMessage">
  <div class="makeMessage"  style="width: 700px;margin-left: 169px;margin-top: 20px;">
    <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="接收人">
            <el-select v-model="form.user" placeholder="请选择接收人">
                <el-option
                    v-for="item in UsersInfo"
                    :key="item.user_email"
                    :label="item.user_name"
                    :value="item.user_email">
                    <span style="float: left">{{ item.user_name }}</span>
                    <span style="float: right; color: #8492a6; font-size: 13px">{{ item.user_email }}</span>
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="通知消息">
            <el-input type="textarea" v-model="form.message"></el-input>
        </el-form-item>
        <el-form-item label="备注">
            <el-input type="textarea" v-model="form.msg_remark"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
        </el-form-item>
    </el-form>
  </div>
</template>

<script>
import formatDate from './../../assets/js/data.js'
import Qs from 'qs'

export default {
  '/makeMessage': 'MakeMessage',
  data() {
      return {
        textUser : this.$store.state,
        UsersInfo:[],
        form: {
          user: '',
          message: '',
          msg_remark: ''
        },
        commitData: {
          user_email:'',
          message:'',
          msg_date:'',
          msg_remark:'',
          deal_remark:'',
          deal_flag:'',
          deal_date:''
        },
      }
    },
    mounted(){
        //组件开始挂载时获取用户信息
        //this.getUserInfo(); 
        this.optionInit(); 
    },
    methods: {
        optionInit(){
            if(this.textUser.userInfo.email != 'null'){
                this.$http.get('web/get_users',{})
                .then((response) => {
                    var res = JSON.parse(response.bodyText)
                    if (res.error_num == 0) {
                        this.UsersInfo = res.list_user;
                    }
                })

            }else{
                this.UsersInfo = [{user_name:'请左上角登陆'}];
            }
        },

        onSubmit() {
            var that = this;
            if(this.textUser.userInfo.email != 'null'){    
                var myDate = new Date();
                this.commitData.user_email = this.form.user
                this.commitData.message = this.form.message
                this.commitData.msg_remark = this.form.msg_remark
                this.commitData.msg_date = formatDate(myDate,'yyyy-MM-dd hh:mm:ss')
                this.commitData.deal_flag = '0'
                this.$axios({ 
                    url:"web/add_msg",
                    headers:{'Content-Type': "application/x-www-form-urlencoded"}, 
                    method:'post', 
                    data: Qs.stringify({
                        user_email: this.commitData.user_email,
                        message: this.commitData.message,
                        msg_remark: this.commitData.msg_remark,
                        msg_date: this.commitData.msg_date,
                        deal_flag: this.commitData.deal_flag,
                        deal_date: this.commitData.deal_date,
                        deal_remark: this.commitData.deal_remark
                    })
                }).then(function(response){
                    if (response.data.error_num == 0) {
                        that.$message.success('入库成功，已经通知那个傻逼了')
                    } else {
                        that.$message.error('入库失败，你这个傻逼再试试')
                    }
                }) .catch(function(err){
                    console.log(err); 
                })
            }else{
                this.$message.error('你还没有登陆')
            }
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

