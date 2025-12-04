from pydantic import BaseModel
from typing import List, Optional, Dict

class DeckCard(BaseModel):
    code: str
    label: Optional[str] = None
    suit: Optional[str] = None
    rank: Optional[str] = None

class Deck(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    cards: List[DeckCard] = []

class Game(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    deck_id: Optional[str] = None

class Theme(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

class Profile(BaseModel):
    id: str
    name: str
    avatar: Optional[str] = None
    preferences: Dict[str, str] = {}

class Lobby(BaseModel):
    id: str
    name: str
    game_id: Optional[str] = None
    host_profile_id: Optional[str] = None
    player_ids: List[str] = []
