<template>
  <div class="app-root">
    <header class="app-header">
      <div class="title">
        <div>
          <h1>SofaLink Engine</h1>
          <p class="subtitle">Console de jeux multi‑supports – v4.0.0-alpha</p>
        </div>
        <span class="pill">ALPHA 4</span>
      </div>
      <nav class="nav">
        <router-link to="/" class="nav-item" active-class="nav-item-active">Accueil</router-link>
        <router-link to="/games" class="nav-item" active-class="nav-item-active">Jeux</router-link>
        <router-link to="/profiles" class="nav-item" active-class="nav-item-active">Profils</router-link>
        <router-link to="/lobby" class="nav-item" active-class="nav-item-active">Lobby</router-link>
        <router-link to="/alpha-lab" class="nav-item" active-class="nav-item-active">Alpha Lab</router-link>
      </nav>
    </header>
    <main class="app-main">
      <router-view />
    </main>
  </div>
</template>

<script setup>
</script>

<style>
:root {
  color-scheme: dark;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
}

body {
  margin: 0;
  background:
    radial-gradient(circle at top, #1d2440 0, #020617 45%, #000 100%);
  color: #e5e7eb;
}

.app-root {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  padding: 1rem 1.6rem 0.9rem;
  background:
    radial-gradient(circle at top left, rgba(168,85,247,0.6), rgba(15,23,42,0.96));
  border-bottom: 1px solid rgba(148,163,184,0.4);
  box-shadow: 0 18px 40px rgba(15,23,42,0.95);
  position: sticky;
  top: 0;
  z-index: 20;
}

.title {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 1rem;
  margin-bottom: 0.8rem;
}

.title h1 {
  margin: 0;
  font-size: 1.25rem;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.subtitle {
  margin: 0.1rem 0 0;
  font-size: 0.82rem;
  opacity: 0.82;
}

.pill {
  align-self: flex-start;
  padding: 0.2rem 0.7rem;
  border-radius: 999px;
  border: 1px solid rgba(248,250,252,0.75);
  font-size: 0.78rem;
  background: linear-gradient(120deg, rgba(8,47,73,0.9), rgba(59,130,246,0.9));
  box-shadow: 0 10px 30px rgba(37,99,235,0.8);
}

.nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}

.nav-item {
  padding: 0.35rem 0.9rem;
  border-radius: 999px;
  border: 1px solid rgba(148,163,184,0.5);
  text-decoration: none;
  color: #e5e7eb;
  font-size: 0.85rem;
  background: radial-gradient(circle at top, rgba(15,23,42,0.9), rgba(15,23,42,0.6));
  transition: all .17s ease-out;
}

.nav-item:hover {
  border-color: #22d3ee;
  box-shadow: 0 0 0 1px rgba(34,211,238,0.5);
}

.nav-item-active {
  background: radial-gradient(circle at top left, #22d3ee, #6366f1);
  border-color: rgba(248,250,252,0.95);
  color: #0b1120;
  box-shadow: 0 14px 42px rgba(37,99,235,0.7);
}

.app-main {
  flex: 1;
  padding: 1.4rem 1.6rem 1.8rem;
}
</style>
