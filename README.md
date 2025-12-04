# SofaLink Engine – v4.0.0-alpha

SofaLink v4 est une **console de jeux multi‑supports** :
- Backend **FastAPI** avec lobby temps réel (WebSocket)
- Frontend **Vue 3 / Vite** moderne
- Données d'exemple (deck, jeu, thème)
- Dockerfile multi‑stage + `docker-compose.yml`

## Fonctionnalités v4.0.0-alpha

- UI servie directement sur `/`
- API:
  - `GET /api/health`
  - `GET /api/decks`
  - `GET /api/games`
  - `GET /api/themes`
  - `POST /api/decks/upload`
  - `GET /api/lobbies`
  - `POST /api/lobbies/create`
- WebSocket:
  - `ws://HOST/ws/lobby/{room_id}` (chat temps réel de test)

## Lancer en local (Docker)

```bash
docker compose up -d --build
```

Puis ouvrir :

```text
http://IP_DU_SERVEUR:8282/
```
