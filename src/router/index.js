import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Login from "../components/Login";
import Register from "../components/Register";
import Course from "../components/Course";
import Detail from "../components/Detail";
import Cart from "../components/Cart";

Vue.use(Router)

export default new Router({
  routes: [
    {path: "/", component: Home},
    {path: "/login", component: Login},
    {path: "/register", component: Register},
    {path: "/python", component: Course},
    {path: "/detail/:id", component: Detail},
    {path: "/cart", component: Cart},
  ]
})
