
<template id="mark">
  <div class="mark">
    <el-card shadow="hover">
      <el-row>
        <el-col :span="24" >
          <el-tag type="success">商品管理</el-tag>
          <el-button type="primary" icon="el-icon-refresh" circle  style="float: right;" size="small" @click="refreshGoods()"></el-button>
        </el-col>
      </el-row>
    </el-card>
    <el-card shadow="hover" >
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="goods_number" label="商品号" sortable width="180" > 
          <template slot-scope="scope"> {{ scope.row.pk }} </template>
        </el-table-column>
        <el-table-column prop="goods_name" label="商品名" width="180"> 
          <template slot-scope="scope"> {{ scope.row.fields.goods_name }} </template>
        </el-table-column>
        <el-table-column  prop="goods_value" label="市价" width="180"> 
          <template slot-scope="scope"> {{ scope.row.fields.goods_value }} </template>
        </el-table-column> 
        <el-table-column  prop="goods_integration" label="积分价值" width="180"> 
          <template slot-scope="scope"> {{ scope.row.fields.goods_integration }} </template>
        </el-table-column>
        <el-table-column  prop="goods_repertory" label="商品库存" width="180"> 
          <template slot-scope="scope"> {{ scope.row.fields.goods_repertory }} </template>
        </el-table-column>
        <el-table-column  prop="day_conversion_max" label="每日兑换上限" width="180"> 
          <template slot-scope="scope"> {{ scope.row.fields.day_conversion_max }} </template>
        </el-table-column>
        <el-table-column  prop="goods_img" label="商品图片" width="180"> 
           <template slot-scope="scope">
          <!-- <template slot-scope="scope"> {{ scope.row.fields.goods_img }} </template> -->
           <img :src="scope.row.fields.goods_img">
          </template>
        </el-table-column>
        <el-table-column  prop="goods_describe" label="商品描述" width="180"> 
          <template slot-scope="scope"> {{ scope.row.fields.goods_describe }} </template>
        </el-table-column>
        <el-table-column  prop="goods_end_date" label="商品结束兑换日期" width="180"> 
          <template slot-scope="scope"> {{farmtDateTime(scope.row.fields.goods_end_date)}} </template>
        </el-table-column>
        <el-table-column prop="operate" label="操作" min-width="60" fixed="right">
          <template slot-scope="scope">
            <el-button @click = "show(scope.$index, scope.row)" style="margin-left: 10px;" type="text" size="small"> 
              查看 
            </el-button>
            <el-button @click = "deal(scope.$index, scope.row)" type="text" size="small"> 
              修改
            </el-button>
            <el-button @click = "del(scope.$index, scope.row)" type="text" size="small"> 
              删除 
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog title="商品详情" :visible.sync="showGoodsFrom" width="40%"> 
      <el-form label-width="150px" :model="goodsFrom" :ref="goodsFrom" size="mini" :disabled="true" >
        <el-form-item label="商品号"  prop="goods_number">
            <el-input v-model="goodsFrom.goods_number" ref="goods_number"></el-input>
        </el-form-item>
        <el-form-item label="商品名" prop="goods_name">
            <el-input v-model="goodsFrom.goods_name" ref="goods_name"></el-input>
        </el-form-item>
        <el-form-item label="市价" prop="goods_value">
            <el-input v-model="goodsFrom.goods_value" ref="goods_value"></el-input>
        </el-form-item>
        <el-form-item label="积分价值" prop="goods_integration">
            <el-input v-model="goodsFrom.goods_integration" ref="goods_integration"></el-input>
        </el-form-item>
        <el-form-item label="商品库存" prop="goods_repertory">
            <el-input v-model="goodsFrom.goods_repertory" ref="goods_repertory"></el-input>
        </el-form-item>
        <el-form-item label="每日兑换上限" prop="day_conversion_max">
            <el-input  v-model="goodsFrom.day_conversion_max" ref="day_conversion_max"></el-input>
        </el-form-item>
        <el-form-item label="商品图片" prop="goods_img">
            <el-input  v-model="goodsFrom.goods_img" ref="goods_img"></el-input>
            <!-- <img :v-model="goodsFrom.goods_img" ref="goods_img" src={{ MEDIA_URL }}{{ goods_img }}> -->
        </el-form-item>
        <el-form-item label="商品描述" prop="goods_describe">
            <el-input  v-model="goodsFrom.goods_describe" ref="goods_describe"></el-input>
        </el-form-item>
        <el-form-item label="商品结束兑换日期" prop="goods_end_date">
            <el-input  v-model="goodsFrom.goods_end_date" ref="goods_end_date"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="showGoodsFrom = false">确 定</el-button>
      </span>
    </el-dialog>


    <el-dialog title="商品修改" :visible.sync="dealGoodsFrom" width="40%"> 
      <el-form label-width="150px" :model="goodsFrom" :ref="goodsFrom" size="mini">
        <el-form-item label="商品号"  prop="goods_number">
            <el-input v-model="goodsFrom.goods_number" ref="goods_number"></el-input>
        </el-form-item>
        <el-form-item label="商品名" prop="goods_name">
            <el-input v-model="goodsFrom.goods_name" ref="goods_name"></el-input>
        </el-form-item>
        <el-form-item label="市价" prop="goods_value">
            <el-input v-model="goodsFrom.goods_value" ref="goods_value"></el-input>
        </el-form-item>
        <el-form-item label="积分价值" prop="goods_integration">
            <el-input v-model="goodsFrom.goods_integration" ref="goods_integration"></el-input>
        </el-form-item>
        <el-form-item label="商品库存" prop="goods_repertory">
            <el-input v-model="goodsFrom.goods_repertory" ref="goods_repertory"></el-input>
        </el-form-item>
        <el-form-item label="每日兑换上限" prop="day_conversion_max">
            <el-input  v-model="goodsFrom.day_conversion_max" ref="day_conversion_max"></el-input>
        </el-form-item>
        <el-form-item label="商品图片" prop="goods_img">
            <el-upload
              class="upload-demo"
              :action= "uploadUrl"
              :on-preview="handlePreview"
              :on-remove="handleRemove"
              :before-remove="beforeRemove"
              :limit="1"
              :on-exceed="handleExceed"
              :file-list="fileList">
              <el-button size="small" type="primary">点击上传</el-button>
            </el-upload>
        </el-form-item>
        <el-form-item label="商品描述" prop="goods_describe">
            <el-input  v-model="goodsFrom.goods_describe" ref="goods_describe"></el-input>
        </el-form-item>
        <el-form-item label="商品结束兑换日期" prop="goods_end_date">
            <el-input  v-model="goodsFrom.goods_end_date" ref="goods_end_date"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dealGoodsFrom = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit(goodsFrom)">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
import formatDate from '../../assets/js/data.js'

export default {
  '/mark': 'Mark',
  data(){
    return {
      textGoods : this.$store.state.goodsCount,
      showGoodsFrom: false,
      dealGoodsFrom: false,
      uploadUrl: "http://127.0.0.1:8000/web/mod_goods",
      tableData: [],
      fileList: [],
      goodsFrom: {
        goods_number:'',
        goods_value:'',
        goods_integration: '',
        goods_name: '',
        goods_repertory: '',
        day_conversion_max: '',
        goods_describe: '',
        goods_img: '',
        goods_end_date:''
      },
    }
  },
  mounted(){
    //组件开始挂载时获取用户信息
    this.refreshGoods();
  },

  methods: {
    farmtDateTime(date){
      if(typeof(date) != 'object' && date !=''){  //date 为空的话它的数据类型为object
        var Data = date.replace('T',' ');  
        Data = Data.substr(0, 19);
        return Data
      } else {
        return ' ';
      } 
    },
    show(index, row){
      this.goodsFrom = row.fields
      this.goodsFrom.goods_number = row.pk
      this.showGoodsFrom = true;
    },
    deal(index, row){
      this.uploadUrl = "http://127.0.0.1:8000/web/mod_goods?goods_number=" + row.pk
      this.goodsFrom = row.fields
      this.goodsFrom.goods_number = row.pk
      this.dealGoodsFrom = true;
    },
    del(index, row){
      this.goodsFrom = row.fields
      this.goodsFrom.goods_number = row.pk
      this.dealGoodsFrom = true;
    },
    onSubmit(formName) {
      var that = this;
      console.log("sssss",this.goodsFrom.goods_number);
      console.log("sssss",this.goodsFrom.goods_value);
      console.log("sssss",this.goodsFrom.goods_integration);
      console.log("sssss",this.goodsFrom.goods_name);
      console.log("sssss",this.goodsFrom.goods_repertory);
      console.log("sssss",this.goodsFrom.day_conversion_max);
      console.log("sssss",this.goodsFrom.goods_describe);
      console.log("sssss",this.goodsFrom.goods_img);
      console.log("sssss",this.goodsFrom.goods_end_date);
    },
    refreshGoods(){
      var that = this;
      this.$axios({ 
          url:"web/show_goods",
          headers:{'Content-Type': "application/x-www-form-urlencoded"}, 
          method:'post'
      }).then(function(response){
          if (response.data.error_num == 0) {
            that.tableData = response.data.list
            console.log("zhaotu",response.data.list[0].fields.goods_img.url);
            that.$store.dispatch('commitGoodsCount',response.data);
            that.$message.success('刷新成功:共 ' + that.textGoods.count + ' 件商品')
          } else {
            that.$message.error('刷新失败，请稍后再试')
          }
      }) .catch(function(err){
          console.log("错误信息：",err); 
      })
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleExceed(files, fileList) {
      this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`确定移除 ${ file.name }？`);
    }
  },
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
