<template>
  <section>
    <h2>Explorateur de decks</h2>
    <p>Liste des decks détectés côté serveur.</p>

    <div v-if="loading">Chargement...</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <ul v-else>
      <li
        v-for="deck in decks"
        :key="deck.id"
        @click="openDeck(deck.id)"
        class="deck-item"
      >
        <strong>{{ deck.name }}</strong>
        <span v-if="deck.description"> — {{ deck.description }}</span>
      </li>
      <li v-if="!decks.length">Aucun deck trouvé.</li>
    </ul>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const decks = ref([])
const loading = ref(true)
const error = ref('')
const router = useRouter()

async function loadDecks () {
  loading.value = true
  error.value = ''
  try {
    const res = await fetch('/api/decks')
    if (!res.ok) throw new Error('Erreur ' + res.status)
    const data = await res.json()
    decks.value = data.decks || []
  } catch (e) {
    error.value = e.message || 'Erreur de chargement'
  } finally {
    loading.value = false
  }
}

function openDeck (id) {
  router.push({ name: 'deck-detail', params: { deckId: id } })
}

onMounted(loadDecks)
</script>

<style scoped>
.deck-item {
  cursor: pointer;
  margin-bottom: 0.4rem;
}
.error {
  color: #ff8a9a;
}
</style>
