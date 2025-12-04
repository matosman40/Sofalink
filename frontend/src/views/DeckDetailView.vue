<template>
  <section>
    <h2>Détail du deck</h2>
    <div v-if="loading">Chargement du deck...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else-if="deck">
      <h3>{{ deck.name }}</h3>
      <p v-if="deck.description">{{ deck.description }}</p>
      <h4>Cartes ({{ deck.cards.length }})</h4>
      <ul>
        <li v-for="card in deck.cards" :key="card.code">
          {{ card.code }} – {{ card.label || (card.rank + ' ' + card.suit) }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Aucun deck trouvé.</p>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const deck = ref(null)
const loading = ref(true)
const error = ref('')

async function loadDeck () {
  loading.value = true
  error.value = ''
  try {
    const id = route.params.deckId
    const res = await fetch(`/api/decks/${id}`)
    if (!res.ok) throw new Error('Erreur ' + res.status)
    const data = await res.json()
    deck.value = data.deck || null
  } catch (e) {
    error.value = e.message || 'Erreur de chargement'
  } finally {
    loading.value = false
  }
}

onMounted(loadDeck)
</script>

<style scoped>
.error {
  color: #ff8a9a;
}
</style>
