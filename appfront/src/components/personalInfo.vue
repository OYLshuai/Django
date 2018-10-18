<template id="info">
  <div class="info" style="">
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card shadow="hover">
          <el-row>
            <el-col :span="24" >
              <el-tag type="info">姓名：</el-tag> <el-tag type="success">{{ textUser.userInfo.name }}</el-tag>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="24">
              <el-tag type="info">邮箱：</el-tag> <el-tag type="success">{{ textUser.userInfo.email }}</el-tag>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="24">
              <el-tag type="info">电话：</el-tag> <el-tag type="success">{{ textUser.userInfo.phone }}</el-tag>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
      <el-col :span="16">
        <el-card shadow="hover"  @click="trunMessage()">
          <el-table :data="tableData" style="width: 100%">
            <el-table-column prop="msg_date" label="日期" sortable width="180" > 
              <template slot-scope="scope"> {{ farmtDateTime(scope.row.fields.msg_date) }} </template>
            </el-table-column>
            <el-table-column prop="message" label="消息内容" width="180"> 
              <template slot-scope="scope"> {{ scope.row.fields.message }} </template>
            </el-table-column>
            <el-table-column  prop="msg_remark" label="消息备注"> 
              <template slot-scope="scope"> {{ scope.row.fields.msg_remark }} </template>
            </el-table-column>
            <el-table-column prop="tag" label="处理状态" width="100" :filters="[{ text: '已读', value: '1' }, { text: '未读', value: '0' }]" :filter-method="filterTag" filter-placement="bottom-end">
              <template slot-scope="scope">
                <el-tag :type="scope.row.fields.deal_flag === '0' ? 'danger' : 'success'" disable-transitions>{{farmtTag(scope.row.fields.deal_flag)}}</el-tag>
              </template>
            </el-table-column>
          </el-table>
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
      tableData: this.$store.state.userMessage.allMessage,
      userInfo: {
        name : "",
        phone : "",
        email:"",
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
        if(row == '0'){
          return "未读";
        } else {
          return "已读";
        }
    },

    farmtDateTime(date){
        var Data = date.replace('T',' ');  
        Data = Data.substr(0, 19);
        return Data
    },

    filterTag(value, row) {
      return row.fields.deal_flag === value;
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
</style>

