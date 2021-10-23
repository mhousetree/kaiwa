import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Category from "../views/Category.vue";
import Expression from "../views/Expression.vue";
import Playlist from "../views/Playlist.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/playlist",
    component: Playlist,
  },
  {
    path: "/:category",
    component: Category,
  },
  {
    path: "/from/:from_language/to/:to_language/:expression_slug",
    component: Expression,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
