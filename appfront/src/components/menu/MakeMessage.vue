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

export default {
  '/makeMessage': 'MakeMessage',
  data() {
      return {
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
            this.$http.get('web/get_users',{})
            .then((response) => {
                var res = JSON.parse(response.bodyText)
                if (res.error_num == 0) {
                    this.UsersInfo = res.list_user;
                }
            })
        },

        onSubmit() {
            var myDate = new Date();
            this.commitData.user_email = this.form.user
            this.commitData.message = this.form.message
            this.commitData.msg_remark = this.form.msg_remark
            this.commitData.msg_date = formatDate(myDate,'yyyy-MM-dd hh:mm:ss')
            this.commitData.deal_flag = '0'
            console.log('submit!',this.commitData.user_email);
            console.log('submit!',this.commitData.message);
            console.log('submit!',this.commitData.msg_remark);
            console.log('submit!',this.commitData.msg_date);
            console.log('submit!',this.commitData.deal_flag);


            this.$axios({ 
                url:"web/add_msg", 
                method:'post', 
                data:{ 
                    Message:this.commitData
                } 
            }).then(function(response){ 
                // if (response.data.error_num == 0) {
                //      //this.$message.success('入库成功，等待处理')
                // } else {
                //     //this.$message.error('入库失败，请重试')
                // }
            }) .catch(function(err){
                 console.log(err); 
            })
            // this.$http.post('web/add_msg',{params: {"Message":this.commitData}})
            // .then((response) => {
            //     var res = JSON.parse(response.bodyText)
            //     if (res.error_num == 0) {
            //         this.$message.success('入库成功，等待处理')
            //     } else {
            //         this.$message.error('入库失败，请重试')
            //     console.log(res['msg'])
            //     }
            // })
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

