// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios";
Vue.prototype.$axios = axios;
import Element from "element-ui"
import "element-ui/lib/theme-chalk/index.css"
Vue.use(Element)
import "../static/css/global.css"
import settings from "./settings";
Vue.prototype.$settings = settings;
// 配置视频播放相关
require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');
import VideoPlayer from 'vue-video-player'

Vue.use(VideoPlayer);

Vue.config.productionTip = false
// 配置极验js
import "../static/js/gt"
/* eslint-disable no-new */
import store from './store/index'
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  store
})
