<template>
  <section class="grid">
    <article class="card main">
      <div class="header">
        <h2>Alpha Lab – API & Data</h2>
        <button class="btn" @click="loadAll" :disabled="loading">
          {{ loading ? 'Chargement...' : 'Rafraîchir tout' }}
        </button>
      </div>
      <p class="subtitle">
        Laboratoire pour tester les endpoints et vérifier les decks/jeux/thèmes du conteneur.
      </p>
    </article>

    <article class="card">
      <h3>Decks</h3>
      <button class="btn small" @click="loadDecks" :disabled="loading">Charger les decks</button>
      <pre v-if="decks" class="pre">{{ decks }}</pre>
      <p v-else class="empty">Aucun deck chargé.</p>
    </article>

    <article class="card">
      <h3>Jeux</h3>
      <button class="btn small" @click="loadGames" :disabled="loading">Charger les jeux</button>
      <pre v-if="games" class="pre">{{ games }}</pre>
      <p v-else class="empty">Aucun jeu chargé.</p>
    </article>

    <article class="card">
      <h3>Thèmes</h3>
      <button class="btn small" @click="loadThemes" :disabled="loading">Charger les thèmes</button>
      <pre v-if="themes" class="pre">{{ themes }}</pre>
      <p v-else class="empty">Aucun thème chargé.</p>
    </article>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const decks = ref(null)
const games = ref(null)
const themes = ref(null)
const loading = ref(false)

const api = axios.create({
  baseURL: window.location.origin
})

async function loadDecks () {
  const { data } = await api.get('/api/decks')
  decks.value = data
}

async function loadGames () {
  const { data } = await api.get('/api/games')
  games.value = data
}

async function loadThemes () {
  const { data } = await api.get('/api/themes')
  themes.value = data
}

async function loadAll () {
  loading.value = true
  try {
    await Promise.all([loadDecks(), loadGames(), loadThemes()])
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.grid {
  display: grid;
  gap: 1.1rem;
}

@media (min-width: 900px) {
  .grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
  .card.main {
    grid-column: 1 / -1;
  }
}

.card {
  background: radial-gradient(circle at top left, rgba(37,99,235,0.18), rgba(15,23,42,0.98));
  border-radius: 1.4rem;
  padding: 1rem 1.1rem;
  border: 1px solid rgba(129,140,248,0.6);
  box-shadow: 0 16px 40px rgba(15,23,42,0.96);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.btn {
  border: none;
  border-radius: 999px;
  padding: 0.4rem 1rem;
  font-size: 0.85rem;
  cursor: pointer;
  background: linear-gradient(90deg, #22d3ee, #6366f1);
  color: white;
  box-shadow: 0 12px 30px rgba(37,99,235,0.7);
}

.btn.small {
  padding: 0.3rem 0.8rem;
  font-size: 0.8rem;
  box-shadow: none;
}

.pre {
  margin-top: 0.6rem;
  background: rgba(15,23,42,0.96);
  padding: 0.55rem;
  border-radius: 0.7rem;
  font-size: 0.78rem;
  max-height: 220px;
  overflow: auto;
}

.empty {
  margin-top: 0.6rem;
  font-size: 0.85rem;
  opacity: 0.75;
}
</style>
