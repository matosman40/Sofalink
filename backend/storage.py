import json
from pathlib import Path
from typing import Any, Dict, List

DATA_ROOT = Path(__file__).resolve().parent.parent / "data"
DB_ROOT = DATA_ROOT / "db"

DB_ROOT.mkdir(parents=True, exist_ok=True)

def _db_path(name: str) -> Path:
    return DB_ROOT / f"{name}.json"

def load_list(name: str) -> List[Dict[str, Any]]:
    path = _db_path(name)
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_list(name: str, data: List[Dict[str, Any]]) -> None:
    path = _db_path(name)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
