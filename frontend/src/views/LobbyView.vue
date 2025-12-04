<template>
  <section class="card">
    <h2>Lobby temps réel</h2>
    <p class="subtitle">
      Crée un lobby, ouvre cette page sur deux appareils, rejoins la même room et envoie des messages.
    </p>

    <div class="row">
      <button class="btn" @click="createRoom" :disabled="creating">
        {{ creating ? 'Création...' : 'Créer un lobby' }}
      </button>
      <input
        v-model="roomId"
        placeholder="ID lobby (ex: ABC123)"
        class="input"
      />
      <button class="btn secondary" @click="connect" :disabled="connected || !roomId">
        {{ connected ? 'Connecté' : 'Rejoindre' }}
      </button>
    </div>

    <div v-if="connected" class="chat">
      <div class="chat-messages">
        <div v-for="(m, idx) in messages" :key="idx" class="msg" :data-type="m.type">
          <span class="from">{{ m.from || m.type }}</span>
          <span class="text">{{ m.message }}</span>
        </div>
      </div>
      <div class="chat-input">
        <input
          v-model="pseudo"
          placeholder="Pseudo"
          class="input small"
        />
        <input
          v-model="text"
          placeholder="Message"
          class="input"
          @keyup.enter="send"
        />
        <button class="btn small" @click="send">Envoyer</button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const api = axios.create({
  baseURL: window.location.origin
})

const roomId = ref('')
const creating = ref(false)
const connected = ref(false)
const ws = ref(null)
const messages = ref([])
const pseudo = ref('player')
const text = ref('')

async function createRoom () {
  creating.value = true
  try {
    const { data } = await api.post('/api/lobbies/create')
    roomId.value = data.room_id
  } finally {
    creating.value = false
  }
}

function connect () {
  if (!roomId.value || connected.value) return
  const protocol = window.location.protocol === 'https:' ? 'wss' : 'ws'
  const url = `${protocol}://${window.location.host}/ws/lobby/${roomId.value}`
  const socket = new WebSocket(url)
  socket.onmessage = (event) => {
    try {
      const payload = JSON.parse(event.data)
      messages.value.push(payload)
    } catch {
      // ignore
    }
  }
  socket.onopen = () => {
    connected.value = True
  }
  socket.onclose = () => {
    connected.value = false
  }
  ws.value = socket
}

function send () {
  if (!ws.value || ws.value.readyState !== WebSocket.OPEN || !text.value) return
  ws.value.send(JSON.stringify({
    from: pseudo.value || 'player',
    message: text.value
  }))
  text.value = ''
}
</script>

<style scoped>
.card {
  background: radial-gradient(circle at top left, rgba(8,47,73,0.4), rgba(15,23,42,0.97));
  border-radius: 1.4rem;
  padding: 1.2rem 1.3rem;
  border: 1px solid rgba(56,189,248,0.6);
  box-shadow: 0 18px 45px rgba(15,23,42,0.96);
}

.subtitle {
  margin-top: 0.25rem;
  margin-bottom: 0.9rem;
  font-size: 0.9rem;
}

.row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.btn {
  border: none;
  border-radius: 999px;
  padding: 0.4rem 0.9rem;
  font-size: 0.85rem;
  cursor: pointer;
  background: linear-gradient(90deg, #22c55e, #22d3ee);
  color: white;
  white-space: nowrap;
}

.btn.secondary {
  background: linear-gradient(90deg, #6366f1, #a855f7);
}

.btn.small {
  padding: 0.3rem 0.7rem;
  font-size: 0.8rem;
}

.input {
  flex: 1;
  min-width: 140px;
  background: rgba(15,23,42,0.9);
  border-radius: 999px;
  border: 1px solid rgba(148,163,184,0.7);
  padding: 0.4rem 0.8rem;
  color: #e5e7eb;
  font-size: 0.85rem;
}

.input.small {
  max-width: 140px;
}

.chat {
  border-top: 1px solid rgba(148,163,184,0.7);
  padding-top: 0.9rem;
  margin-top: 0.2rem;
}

.chat-messages {
  max-height: 220px;
  overflow: auto;
  padding: 0.5rem;
  background: rgba(15,23,42,0.96);
  border-radius: 0.9rem;
  margin-bottom: 0.7rem;
}

.msg {
  display: flex;
  gap: 0.4rem;
  margin-bottom: 0.25rem;
  font-size: 0.82rem;
}

.msg[data-type="system"] .from {
  color: #22d3ee;
}

.from {
  font-weight: 600;
}

.chat-input {
  display: flex;
  gap: 0.4rem;
  align-items: center;
  flex-wrap: wrap;
}
</style>
