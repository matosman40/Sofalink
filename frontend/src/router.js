import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './views/HomeView.vue'
import GamesView from './views/GamesView.vue'
import ProfilesView from './views/ProfilesView.vue'
import AlphaLabView from './views/AlphaLabView.vue'
import LobbyView from './views/LobbyView.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/games', name: 'games', component: GamesView },
  { path: '/profiles', name: 'profiles', component: ProfilesView },
  { path: '/alpha-lab', name: 'alpha-lab', component: AlphaLabView },
  { path: '/lobby', name: 'lobby', component: LobbyView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
