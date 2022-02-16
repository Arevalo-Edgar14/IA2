import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Perceptron from '@/views/Perceptron.vue';
import About from '@/views/About.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: Perceptron,
  },
  {
    path: '/perceptron',
    name: 'Perceptron',
    component: Perceptron,
  },
  {
    path: '/about',
    name: 'about',
    component: About,
  },
  {
    path: '/technologies',
    name: 'Technologies',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Technologies.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
