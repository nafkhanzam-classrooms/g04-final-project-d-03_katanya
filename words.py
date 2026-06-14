import re
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --- IMPORT DARI MODULE KITA ---
from database import PLAYER_DB, save_db, get_or_create_player, get_leaderboard_data, DEFAULT_MMR
from words import KBBI_WORDS, evaluate_guess, get_daily_secret
from matchmaker import MatchmakingManager

app = FastAPI(title="KATANYA - Web Game Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AuthRequest(BaseModel):
    username: str
    password: str

class GuessRequest(BaseModel):
    guess:       str
    secret_word: str

class DailyRequest(BaseModel):
    guess: str

@app.post("/register")
def register(req: AuthRequest):
    user = req.username.strip()
    if not re.match(r"^[A-Za-z0-9_]{3,15}$", user): raise HTTPException(400, "Username 3-15 karakter")
    if user in PLAYER_DB: raise HTTPException(400, "Username sudah terdaftar!")
    if len(req.password) < 6: raise HTTPException(400, "Password minimal 6 karakter")
    PLAYER_DB[user] = {"password": req.password, "mmr": DEFAULT_MMR, "wins": 0, "losses": 0, "draws": 0, "total": 0}
    save_db()
    return {"message": "Registrasi berhasil!", "username": user, "mmr": DEFAULT_MMR}

@app.post("/login")
def login(req: AuthRequest):
    user = req.username.strip()
    p    = get_or_create_player(user)
    if p["password"] and p["password"] != req.password:
        raise HTTPException(400, "Username atau Password salah!")
    return {
        "message":  "Login berhasil!", "username": user, "mmr": p.get("mmr", DEFAULT_MMR),
        "wins": p.get("wins", 0), "losses": p.get("losses", 0), "draws": p.get("draws", 0), "total": p.get("total", 0),
    }

@app.get("/get-practice-secret")
def practice_secret():
    from words import KBBI_LIST
    import random
    secret = random.choice(KBBI_LIST) if KBBI_LIST else "UTAMA"
    return {"secret_word": secret}

@app.get("/get-leaderboard")
def leaderboard():
    return {"leaderboard": get_leaderboard_data()}

@app.post("/check-guess")
def check_guess(req: GuessRequest):
    g, s = req.guess.upper(), req.secret_word.upper()
    if len(g) != 5: return {"error": "Kata harus 5 huruf"}
    if g not in KBBI_WORDS: return {"error": "Kata tidak terdaftar di KBBI!"}
    return {"guess": g, "result": evaluate_guess(g, s), "is_win": g == s}

@app.post("/check-daily-guess")
def check_daily(req: DailyRequest):
    g, s = req.guess.upper(), get_daily_secret()
    if len(g) != 5: return {"error": "Kata harus 5 huruf"}
    if g not in KBBI_WORDS: return {"error": "Kata tidak terdaftar di KBBI!"}
    return {"guess": g, "result": evaluate_guess(g, s), "is_win": g == s}

manager = MatchmakingManager()

@app.websocket("/ws/{username}")
async def ws_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            try:
                data = await websocket.receive_json()
            except WebSocketDisconnect:
                break 
            except Exception:
                continue 

            if not isinstance(data, dict):
                continue
            
            action = data.get("action")
            if not isinstance(action, str):
                continue

            if action == "ping":
                await websocket.send_json({"status": "pong", "ts": data.get("ts")})
            elif action == "find_match":
                await manager.join_queue(username)
            elif action == "submit_arena_guess":
                r_id = data.get("room_id")
                guess = data.get("guess")
                if isinstance(r_id, str) and isinstance(guess, str):
                    await manager.process_guess(username, r_id, guess)
            elif action == "get_leaderboard":
                await websocket.send_json({"status": "leaderboard_data", "leaderboard": get_leaderboard_data()})
            elif action == "send_chat":
                r_id = data.get("room_id")
                text = data.get("text")
                if isinstance(r_id, str) and isinstance(text, str):
                    await manager.send_chat(username, r_id, text)
            elif action == "get_live_matches":
                matches = manager.get_live_matches_data()
                await websocket.send_json({"status": "live_matches_data", "matches": matches})
            elif action == "spectate_room":
                r_id = data.get("room_id")
                if isinstance(r_id, str):
                    await manager.spectate_room(username, r_id, websocket)

    except Exception:
        pass
    finally:
        if manager.connections.get(username) == websocket:
            manager.connections.pop(username, None)
            if username in manager.queue: manager.queue.remove(username)
            room = manager._find_active_room(username)
            if room and not room.get("game_over"):
                await manager.handle_disconnect_gracefully(username, room["room_id"])