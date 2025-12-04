from fastapi import FastAPI, UploadFile, File, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json
import uuid

APP_VERSION = "4.0.0-alpha"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DECKS_DIR = DATA_DIR / "decks"
GAMES_DIR = DATA_DIR / "games"
THEMES_DIR = DATA_DIR / "themes"

app = FastAPI(
    title="SofaLink Engine v4",
    version=APP_VERSION,
    description="SofaLink v4 – moteur multi‑jeux avec lobby temps réel (squelette alpha)."
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Utils JSON ----

def load_json(path: Path):
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"Ressource introuvable: {path.name}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur de lecture JSON: {e}")

# ---- Basic API ----

@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "version": APP_VERSION,
        "engine": "v4.0.0-alpha",
        "features": ["lobby", "cards", "themes", "alpha-engine"]
    }

@app.get("/api/decks")
async def list_decks():
    decks = []
    for deck_dir in sorted(DECKS_DIR.glob("*")):
        manifest = deck_dir / "manifest.json"
        if manifest.exists():
            data = load_json(manifest)
            decks.append(data)
    return {"items": decks}

@app.get("/api/games")
async def list_games():
    games = []
    for game_file in sorted(GAMES_DIR.glob("*.json")):
        games.append(load_json(game_file))
    return {"items": games}

@app.get("/api/themes")
async def list_themes():
    themes = []
    for theme_dir in sorted(THEMES_DIR.glob("*")):
        manifest = theme_dir / "theme.json"
        if manifest.exists():
            data = load_json(manifest)
            themes.append(data)
    return {"items": themes}

@app.post("/api/decks/upload")
async def upload_deck(file: UploadFile = File(...)):
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="Fichier JSON attendu.")
    target = DECKS_DIR / file.filename
    content = await file.read()
    try:
        json.loads(content.decode("utf-8"))
    except Exception:
        raise HTTPException(status_code=400, detail="JSON invalide.")
    target.write_bytes(content)
    return {"status": "uploaded", "filename": file.filename}

# ---- Lobby temps réel (squelette v4) ----

class LobbyManager:
    def __init__(self):
        self.rooms: dict[str, list[WebSocket]] = {}

    async def connect(self, room_id: str, websocket: WebSocket):
        await websocket.accept()
        self.rooms.setdefault(room_id, []).append(websocket)
        await self.broadcast(room_id, {"type": "system", "message": f"Un joueur a rejoint {room_id}."})

    def disconnect(self, room_id: str, websocket: WebSocket):
        if room_id in self.rooms and websocket in self.rooms[room_id]:
            self.rooms[room_id].remove(websocket)

    async def broadcast(self, room_id: str, message: dict):
        for ws in list(self.rooms.get(room_id, [])):
            try:
                await ws.send_json(message)
            except WebSocketDisconnect:
                self.disconnect(room_id, ws)

lobby_manager = LobbyManager()

@app.get("/api/lobbies")
async def list_lobbies():
    return {
        "rooms": [
            {"id": rid, "players": len(sockets)}
            for rid, sockets in lobby_manager.rooms.items()
        ]
    }

@app.post("/api/lobbies/create")
async def create_lobby():
    room_id = uuid.uuid4().hex[:6].upper()
    return {"room_id": room_id}

@app.websocket("/ws/lobby/{room_id}")
async def lobby_ws(websocket: WebSocket, room_id: str):
    await lobby_manager.connect(room_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await lobby_manager.broadcast(room_id, {
                "type": "chat",
                "from": data.get("from", "inconnu"),
                "message": data.get("message", "")
            })
    except WebSocketDisconnect:
        lobby_manager.disconnect(room_id, websocket)

# ---- UI intégrée sur "/" ----

DIST_DIR = BASE_DIR / "dist"
if DIST_DIR.exists():
    app.mount("/", StaticFiles(directory=DIST_DIR, html=True), name="frontend")
