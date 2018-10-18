import Vue from 'vue'
import Vuex from 'Vuex'
Vue.use(Vuex);

//Vuex配置
const store = new Vuex.Store({
    state: {
      domain:'http://127.0.0.1:8000/web/', //保存后台请求的地址，修改时方便（比方说从测试服改成正式服域名）
      userInfo: { //保存用户信息
        name: '请登陆查看信息',
        email: 'null',
        phone: 'null'
      },
      userMessage:{
        allMessage: [],
        messageed: [],
        messageing: [],
        count: " "
      },
      msg:"",
    },
    mutations: {
      //更新用户信息
      updateUserInfo(state, newUserInfo) {
        state.userInfo = newUserInfo;
      },
      
      //更新用户处理信息
      updateUserMessage(state, newMessage) {
        state.userMessage.allMessage = newMessage.allmsg;
        state.userMessage.messageed = newMessage.msged;
        state.userMessage.messageing = newMessage.msging;
        state.userMessage.count = newMessage.count;
      },
      
      //测试
      updateMsg(state, data) {
        state.msg = data;
      }
    },
    actions: {
      commitUserList:({commit},userInfo) => commit('updateUserInfo',userInfo),
      commitMsg:({commit},data) => commit('updateMsg',data),
      commitMessage:({commit},newMessage) => commit('updateUserMessage',newMessage)

    }
  })

  export default store
  
  //设置cookie,增加到vue实例方便全局调用
  //vue全局调用的理由是，有些组件所用到的接口可能需要session验证，session从cookie获取
  //当然，如果session保存到vuex的话除外
  Vue.prototype.setCookie = (c_name, value, expiredays) => {
    var exdate = new Date();　　　　
    exdate.setDate(exdate.getDate() + expiredays);　　　　
    document.cookie = c_name + "=" + escape(value) + ((expiredays == null) ? "" : ";expires=" + exdate.toGMTString());
  }
  
  //获取cookie、
  function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
      return (arr[2]);
    else
      return null;
  }
  Vue.prototype.getCookie = getCookie;
  
  //删除cookie
  Vue.prototype.delCookie =(name) => {
      var exp = new Date();
      exp.setTime(exp.getTime() - 1);
      var cval = getCookie(name);
      if (cval != null)
        document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
    }
  
  