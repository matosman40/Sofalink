<template>
  <section class="layout">
    <article class="card hero">
      <h2>Console SofaLink v4</h2>
      <p class="lead">
        Hub multi‑jeux pour soirées, salons, familles et potes. Un écran principal,
        plusieurs téléphones, des cartes, des plateaux… tout passe par SofaLink.
      </p>
      <ul class="bullets">
        <li>🎮 Moteur de jeux générique (v4 – squelette)</li>
        <li>🧑‍🤝‍🧑 Lobby temps réel &amp; rooms via WebSocket</li>
        <li>🃏 Support jeux de cartes &amp; jeux de plateau (à venir)</li>
      </ul>
    </article>

    <article class="card">
      <h3>API rapide</h3>
      <p>Endpoints principaux :</p>
      <ul class="bullets">
        <li><code>GET /api/health</code></li>
        <li><code>GET /api/decks</code></li>
        <li><code>GET /api/games</code></li>
        <li><code>GET /api/themes</code></li>
        <li><code>GET /api/lobbies</code></li>
        <li><code>POST /api/lobbies/create</code></li>
      </ul>
    </article>

    <article class="card">
      <h3>Alpha Lab</h3>
      <p>
        Va dans <strong>Alpha Lab</strong> pour appeler directement les API
        et vérifier que les données du conteneur sont bien lues.
      </p>
    </article>

    <article class="card">
      <h3>Lobby</h3>
      <p>
        L'onglet <strong>Lobby</strong> te permet de créer/join une room et
        de tester les messages temps réel entre plusieurs périphériques.
      </p>
    </article>
  </section>
</template>

<script setup>
</script>

<style scoped>
.layout {
  display: grid;
  gap: 1.2rem;
}

@media (min-width: 900px) {
  .layout {
    grid-template-columns: minmax(0, 2.1fr) minmax(0, 1fr);
  }
  .hero {
    grid-row: span 2;
  }
}

.card {
  background: radial-gradient(circle at top left, rgba(15,23,42,0.96), rgba(15,23,42,0.98));
  border-radius: 1.4rem;
  padding: 1.2rem 1.3rem;
  border: 1px solid rgba(148,163,184,0.5);
  box-shadow: 0 16px 45px rgba(15,23,42,0.95);
}

.hero {
  background:
    radial-gradient(circle at top left, rgba(34,211,238,0.18), rgba(15,23,42,0.98));
}

.lead {
  margin-top: 0.4rem;
  margin-bottom: 0.8rem;
}

.bullets {
  margin: 0;
  padding-left: 1.1rem;
}

code {
  background: rgba(15,23,42,0.9);
  padding: 0.1rem 0.35rem;
  border-radius: 0.3rem;
  font-size: 0.78rem;
}
</style>
