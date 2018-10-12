<template>
  <div class="home">
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
        <el-aside width="250px" style="background-color: rgb(238, 241, 246)">
          <el-menu :default-openeds="['1']" default-active="1" class="el-menu-vertical-demo" style="text-align: left">
            <el-submenu index="1">
              <template slot="title"><i class="el-icon-star-on"></i>导航一</template>
              <el-menu-item-group>
                <el-menu-item index="1-1"><i class="el-icon-star-off"></i>选项1</el-menu-item>
                <el-menu-item index="1-2"><i class="el-icon-star-off"></i>选项2</el-menu-item>
                <el-menu-item index="1-3"><i class="el-icon-star-off"></i>选项3</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
              <template slot="title"><i class="el-icon-star-on"></i>导航二</template>
              <el-menu-item-group>
                <el-menu-item index="2-1"><i class="el-icon-star-off"></i>选项1</el-menu-item>
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
          <el-row display="margin-top:10px">
          <el-input v-model="input" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
          <el-button type="primary" @click="addBook()" style="float:left; margin: 2px;">新增</el-button>
          </el-row>
          <el-row>
              <el-table :data="bookList" height="510" style="width: 100%" border>
                <el-table-column prop="id" label="编号" min-width="100">
                  <template scope="scope"> {{ scope.row.pk }} </template>
                </el-table-column>
                <el-table-column prop="book_name" label="书名" min-width="100">
                  <template scope="scope"> {{ scope.row.fields.book_name }} </template>
                </el-table-column>
                <el-table-column prop="add_time" label="添加时间" min-width="100">
                  <template scope="scope"> {{ scope.row.fields.add_time }} </template>
                </el-table-column>
                <el-table-column prop="operate" label="操作" min-width="100">
                  <template slot-scope="scope">
                    <el-button @click = "delBook(scope.$index, scope.row)" type="text" size="small">
                      移除
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      input: '',
      bookList: []
    }
  },
  mounted: function() {
    this.showBooks()
  },
  methods: {
    addBook(){
      this.$http.get('http://127.0.0.1:8000/web/add_book?book_name=' + this.input)
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
              this.showBooks()
              this.$message.success('新增书籍成功')
            } else {
              this.$message.error('新增书籍失败，请重试')
              console.log(res['msg'])
            }
        })
    },
    delBook(index, row){
      this.$http.get('http://127.0.0.1:8000/web/del_book?book_name=' + row.fields.book_name + '&&id=' + row.pk)
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num == 0) {
              this.showBooks()
              this.$message.success('删除书籍成功')
            } else {
              this.$message.error('删除书籍失败，请重试')
              console.log(res['msg'],row.fields.book_name)
            }
        })
    },
    showBooks(){
      this.$http.get('http://127.0.0.1:8000/web/show_books')
        .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num == 0) {
              this.bookList = res['list']
              console.log(res['list']);
            } else {
              this.$message.error('查询书籍失败')
              console.log(res['msg'])
            }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  
  .el-aside {
    color: #333;
  }
</style>
