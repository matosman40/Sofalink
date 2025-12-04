<template>
  <section>
    <h2>Explorateur de jeux</h2>
    <div v-if="loading">Chargement...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <ul v-else>
      <li
        v-for="game in games"
        :key="game.id"
        @click="openGame(game.id)"
        class="game-item"
      >
        <strong>{{ game.name }}</strong>
        <span v-if="game.description"> — {{ game.description }}</span>
      </li>
      <li v-if="!games.length">Aucun jeu trouvé.</li>
    </ul>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const games = ref([])
const loading = ref(true)
const error = ref('')
const router = useRouter()

async function loadGames () {
  loading.value = true
  error.value = ''
  try {
    const res = await fetch('/api/games')
    if (!res.ok) throw new Error('Erreur ' + res.status)
    const data = await res.json()
    games.value = data.games || []
  } catch (e) {
    error.value = e.message || 'Erreur de chargement'
  } finally {
    loading.value = false
  }
}

function openGame (id) {
  router.push({ name: 'game-detail', params: { gameId: id } })
}

onMounted(loadGames)
</script>

<style scoped>
.game-item {
  cursor: pointer;
  margin-bottom: 0.4rem;
}
.error {
  color: #ff8a9a;
}
</style>
