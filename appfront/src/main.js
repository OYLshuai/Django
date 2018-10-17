// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import '../theme/index.css'
import VueResource from 'vue-resource'
import store from './store/store.js'

Vue.config.productionTip = false

/* eslint-disable no-new */

Vue.use(ElementUI);
Vue.use(VueResource);
 
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})

