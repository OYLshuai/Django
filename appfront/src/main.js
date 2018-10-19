// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from './axios';//通过import引入
import ElementUI from 'element-ui'
import '../theme/index.css'
import VueResource from 'vue-resource'
import store from './store/store.js'
import formatDate from './assets/js/data.js'

Vue.config.productionTip = false

/* eslint-disable no-new */

Vue.use(ElementUI);
Vue.use(VueResource);
 
new Vue({
  el: '#app',
  store,
  router,
  formatDate,
  axios,//通过import引入，然后在这里调用
  components: { App },
  template: '<App/>'
})

