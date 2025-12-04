<template>
  <section>
    <h2>Détail du jeu</h2>
    <div v-if="loading">Chargement du jeu...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else-if="game">
      <h3>{{ game.name }}</h3>
      <p v-if="game.description">{{ game.description }}</p>
      <p v-if="game.deck_id">Deck associé : {{ game.deck_id }}</p>
    </div>
    <div v-else>
      <p>Aucun jeu trouvé.</p>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const game = ref(null)
const loading = ref(true)
const error = ref('')

async function loadGame () {
  loading.value = true
  error.value = ''
  try {
    const id = route.params.gameId
    const res = await fetch(`/api/games/${id}`)
    if (!res.ok) throw new Error('Erreur ' + res.status)
    const data = await res.json()
    game.value = data.game || null
  } catch (e) {
    error.value = e.message || 'Erreur de chargement'
  } finally {
    loading.value = false
  }
}

onMounted(loadGame)
</script>

<style scoped>
.error {
  color: #ff8a9a;
}
</style>
