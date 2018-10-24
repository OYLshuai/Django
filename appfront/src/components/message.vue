<template id="message">
  <div class="message">
    <el-card shadow="hover">
      <el-row>
        <el-col :span="24" >
          <el-tag type="info">姓名：</el-tag> <el-tag type="success">{{ textUser.userInfo.name }}</el-tag>
          <el-button type="primary" icon="el-icon-refresh" circle  style="float: right;" size="small" @click="refreshMessage()"></el-button>
        </el-col>
      </el-row>
    </el-card>
    <el-card shadow="hover"  @click="trunMessage()">
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="msg_date" label="日期" sortable width="180" > 
          <template slot-scope="scope"> {{ farmtDateTime(scope.row.fields.msg_date) }} </template>
        </el-table-column>
        <el-table-column prop="message" label="消息内容" width="180"> 
          <template slot-scope="scope"> {{ scope.row.fields.message }} </template>
        </el-table-column>
        <el-table-column  prop="msg_remark" label="消息备注" width="180"> 
          <template slot-scope="scope"> {{ scope.row.fields.msg_remark }} </template>
        </el-table-column> 
        <el-table-column  prop="deal_remark" label="处理备注" width="180"> 
          <template slot-scope="scope"> {{ scope.row.fields.deal_remark }} </template>
        </el-table-column>
        <el-table-column  prop="deal_date" label="处理日期" width="180"> 
          <template slot-scope="scope"> {{farmtDateTime(scope.row.fields.deal_date)}} </template>
        </el-table-column>
        <el-table-column prop="tag" label="处理状态" width="100" :filters="[{ text: '已读', value: '1' }, { text: '未读', value: '0' }]" :filter-method="filterTag" filter-placement="bottom-end">
          <template slot-scope="scope">
            <el-tag :type="scope.row.fields.deal_flag === '1' ? 'success' : 'danger'" disable-transitions>{{farmtTag(scope.row.fields.deal_flag)}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="operate" label="操作" min-width="100" fixed="right">
          <template slot-scope="scope">
            <el-button @click = "deal(scope.$index, scope.row)" type="text" size="small"> 
              处理 
            </el-button>
            <el-button @click = "show(scope.$index, scope.row)" type="text" size="small"> 
              查看 
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog title="消息详情" :visible.sync="showMsgFrom" width="30%"> 
      <el-form label-width="80px" :model="loginFrom" :ref="loginFrom" size="mini" :disabled="true">
        <el-form-item label="日期"  prop="msg_date">
            <el-input v-model="loginFrom.msg_date" ref="msg_date"></el-input>
        </el-form-item>
        <el-form-item label="消息内容" prop="message">
            <el-input v-model="loginFrom.message" ref="message"></el-input>
        </el-form-item>
        <el-form-item label="消息备注" prop="msg_remark">
            <el-input v-model="loginFrom.msg_remark" ref="msg_remark"></el-input>
        </el-form-item>
        <el-form-item label="处理备注" prop="deal_remark">
            <el-input v-model="loginFrom.deal_remark" ref="deal_remark"></el-input>
        </el-form-item>
        <el-form-item label="处理日期" prop="deal_date">
            <el-input v-model="loginFrom.deal_date" ref="deal_date"></el-input>
        </el-form-item>
        <el-form-item label="处理状态" prop="deal_flag">
            <el-input  v-model="loginFrom.deal_flag" ref="deal_flag"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="showMsgFrom = false">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog title="消息处理" :visible.sync="dealMsgFrom" width="30%" > 
      <el-form label-width="80px" :model="loginFrom" :ref="loginFrom" size="mini">
        <el-form-item label="日期"  prop="msg_date">
            <el-input v-model="loginFrom.msg_date" ref="msg_date"></el-input>
        </el-form-item>
        <el-form-item label="消息内容" prop="message">
            <el-input v-model="loginFrom.message" ref="message"></el-input>
        </el-form-item>
        <el-form-item label="消息备注" prop="msg_remark">
            <el-input v-model="loginFrom.msg_remark" ref="msg_remark"></el-input>
        </el-form-item>
        <el-form-item label="处理备注" prop="deal_remark">
            <el-input v-model="loginFrom.deal_remark" ref="deal_remark"></el-input>
        </el-form-item>
        <el-form-item label="处理日期" prop="deal_date">
            <el-input v-model="loginFrom.deal_date" ref="deal_date"></el-input>
        </el-form-item>
        <el-form-item label="处理状态" prop="deal_flag">
            <el-input v-model="loginFrom.deal_flag" ref="deal_flag"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dealMsgFrom = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit(loginFrom)">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>

import formatDate from '../assets/js/data.js'

export default {
  '/message': 'Message',
    data(){
    return {
      showMsgFrom: false,
      dealMsgFrom: false,
      textUser : this.$store.state,
      tableData: this.$store.state.userMessage.allMessage,
      userMessage : this.$store.state.userMessage,
      userInfo: {
        name : "",
        phone : "",
        email:"",
      },
      loginFrom: {
        id:'',
        user_email:'',
        msg_date: '',
        message: '',
        msg_remark: '',
        deal_remark: '',
        deal_date: '',
        deal_flag:''
      },
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
    },

    farmtTag(row) {
        if(row == '1'){
          return "已读";
        } else {
          return "未读";
        }
    },

    farmtDateTime(date){
      if(typeof(date) != 'object' && date !=''){  //date 为空的话它的数据类型为object
        var Data = date.replace('T',' ');  
        Data = Data.substr(0, 19);
        return Data
      } else {
        return ' ';
      } 
    },

    filterTag(value, row) {
      return row.fields.deal_flag === value;
    },
    show(index, row){
      this.loginFrom = row.fields
      this.loginFrom.id = row.pk
      this.showMsgFrom = true;
    },
    deal(index, row){
      this.loginFrom = row.fields
      this.loginFrom.id = row.pk
      this.dealMsgFrom = true;
    },
    onSubmit(formName) {
      this.$refs[formName].validate((valid) => {
          if (valid) {
            var myDate = new Date();
            this.loginFrom.user_email = this.textUser.userInfo.email;
            this.loginFrom.deal_flag = '1';
            this.loginFrom.deal_date = formatDate(myDate,'yyyy-MM-dd hh:mm:ss')
            var data = this.loginFrom;
            this.$http.get('http://127.0.0.1:8000/web/mod_msg',{params: {"loginFrom":this.loginFrom} })
            .then((response) => {
                var res = JSON.parse(response.bodyText)
                if (res.error_num == 0) {
                   this.dealMsgFrom = false
                   this.$message.success('处理成功: 处理时间为' + data.deal_date)
                } else {
                    this.$message.error('处理失败')
                    console.log(res['msg'])
                }
            })
          } else {
            return false;
          }
        });
    },
    refreshMessage(){
    if(this.textUser.userInfo.email != 'null'){
        this.$http.get('http://127.0.0.1:8000/web/show_message',{params: {"user_email":this.textUser.userInfo.email} })
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
                this.$store.dispatch('commitMessage',res);
                this.tableData = this.$store.state.userMessage.allMessage
                this.$message.success('获取消息成功:共 ' + this.userMessage.count + ' 条新信息')
            } else {
                this.$message.error('获取消息失败: ' + res['msg'])
                console.log(res['msg'])
            }
        })
      } else {
        this.$message.error('同步失败: 邮箱错误')
      }
    },
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

.el-card{
  margin-top: 10px;
}
</style>

