import AboutPage from '@/views/AboutPage.vue'
import HomePage from '@/views/HomePage.vue'
import UserPage from '@/views/UserPage.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: HomePage },
    { path: '/about', component: AboutPage },
    { path: '/users', component: UserPage },
  ],
})

export default router
