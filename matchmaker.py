import os
import json

DB_FILE     = "katanya_users_db.json"
K_FACTOR    = 32
DEFAULT_MMR = 1000

PLAYER_DB: dict = {}

def load_db():
    global PLAYER_DB
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                PLAYER_DB = json.load(f)
        except Exception:
            PLAYER_DB = {}
    else:
        PLAYER_DB = {}

def save_db():
    try:
        with open(DB_FILE, "w") as f:
            json.dump(PLAYER_DB, f, indent=4)
    except Exception: pass

# Muat database saat file di-import
load_db()

def get_or_create_player(username: str) -> dict:
    if username not in PLAYER_DB:
        PLAYER_DB[username] = {"password": "", "mmr": DEFAULT_MMR, "wins": 0, "losses": 0, "draws": 0, "total": 0}
    if "mmr" not in PLAYER_DB[username]:
        PLAYER_DB[username]["mmr"] = PLAYER_DB[username].pop("elo", DEFAULT_MMR)
        PLAYER_DB[username]["total"] = PLAYER_DB[username].get("wins", 0) + PLAYER_DB[username].get("losses", 0) + PLAYER_DB[username].get("draws", 0)
    return PLAYER_DB[username]

def expected_score(mmr_a: float, mmr_b: float) -> float:
    return 1.0 / (1.0 + 10 ** ((mmr_b - mmr_a) / 400))

def update_mmr(winner: str, loser: str, is_draw: bool = False) -> tuple[int, int]:
    wp = get_or_create_player(winner)
    lp = get_or_create_player(loser)

    exp_w = expected_score(wp["mmr"], lp["mmr"])
    exp_l = expected_score(lp["mmr"], wp["mmr"])

    score_w, score_l = (0.5, 0.5) if is_draw else (1.0, 0.0)

    delta_w = round(K_FACTOR * (score_w - exp_w))
    delta_l = round(K_FACTOR * (score_l - exp_l))

    wp["mmr"] = max(0, wp["mmr"] + delta_w)
    lp["mmr"] = max(0, lp["mmr"] + delta_l)

    if is_draw:
        wp["draws"] = wp.get("draws", 0) + 1
        lp["draws"] = lp.get("draws", 0) + 1
    else:
        wp["wins"] = wp.get("wins", 0) + 1
        lp["losses"] = lp.get("losses", 0) + 1

    wp["total"] = wp.get("total", 0) + 1
    lp["total"] = lp.get("total", 0) + 1

    save_db()
    return delta_w, delta_l

def get_leaderboard_data(top: int = 10) -> list:
    players = sorted(PLAYER_DB.items(), key=lambda x: x[1].get("mmr", DEFAULT_MMR), reverse=True)
    result  = []
    for i, (uname, data) in enumerate(players[:top]):
        result.append({
            "rank": i + 1, "username": uname, "mmr": data.get("mmr", DEFAULT_MMR),
            "wins": data.get("wins", 0), "losses": data.get("losses", 0), "draws": data.get("draws", 0), "total": data.get("total", 0),
        })
    return result