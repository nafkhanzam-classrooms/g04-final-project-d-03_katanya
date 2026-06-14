import asyncio
import json
import re
import websockets
import random

from database import PLAYER_DB, save_db, get_or_create_player, get_leaderboard_data, DEFAULT_MMR
from words import KBBI_WORDS, evaluate_guess, get_daily_secret, KBBI_LIST
from matchmaker import MatchmakingManager

manager = MatchmakingManager()

async def handler(websocket):
    username = None
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
            except json.JSONDecodeError:
                continue
            
            action = data.get("action")
            if not isinstance(action, str):
                continue
            
            #Autentikasi
            if action in ["login", "register"]:
                user = data.get("username", "").strip()
                pwd = data.get("password", "")
                
                if not re.match(r"^[A-Za-z0-9_]{3,15}$", user):
                    await websocket.send(json.dumps({"status": "auth_error", "message": "Username 3-15 karakter (huruf/angka/underscore)"}))
                    continue
                if len(pwd) < 6:
                    await websocket.send(json.dumps({"status": "auth_error", "message": "Password minimal 6 karakter"}))
                    continue
                    
                p = get_or_create_player(user)
                if action == "register":
                    if p["password"] != "":
                        await websocket.send(json.dumps({"status": "auth_error", "message": "Username sudah terdaftar!"}))
                        continue
                    p["password"] = pwd
                    save_db()
                else:
                    if p["password"] == "" or p["password"] != pwd:
                        await websocket.send(json.dumps({"status": "auth_error", "message": "Username atau Password salah!"}))
                        continue
                        
                username = user
                await manager.connect(websocket, username)
                await websocket.send(json.dumps({
                    "status": "auth_success", "username": user, "mmr": p.get("mmr", DEFAULT_MMR),
                    "wins": p.get("wins", 0), "losses": p.get("losses", 0), "draws": p.get("draws", 0),
                    "total": p.get("total", 0)
                }))

            #Ping/Latency
            elif action == "ping":
                await websocket.send(json.dumps({"status": "pong", "ts": data.get("ts")}))

            elif not username:
                await websocket.send(json.dumps({"status": "auth_error", "message": "Silakan login terlebih dahulu."}))
                continue

            #Single Player
            elif action == "get_practice_secret":
                secret = random.choice(KBBI_LIST) if KBBI_LIST else "UTAMA"
                await websocket.send(json.dumps({"status": "practice_secret", "secret_word": secret}))

            elif action == "check_guess":
                g, s = data.get("guess", "").upper(), data.get("secret_word", "").upper()
                if len(g) != 5 or g not in KBBI_WORDS:
                    await websocket.send(json.dumps({"status": "guess_error_single", "message": "Kata tidak valid di KBBI!", "mode": "prac"}))
                else:
                    await websocket.send(json.dumps({"status": "guess_res_single", "mode": "prac", "guess": g, "result": evaluate_guess(g, s), "is_win": g == s}))

            elif action == "check_daily_guess":
                g, s = data.get("guess", "").upper(), get_daily_secret()
                if len(g) != 5 or g not in KBBI_WORDS:
                    await websocket.send(json.dumps({"status": "guess_error_single", "message": "Kata tidak valid di KBBI!", "mode": "daily"}))
                else:
                    await websocket.send(json.dumps({"status": "guess_res_single", "mode": "daily", "guess": g, "result": evaluate_guess(g, s), "is_win": g == s}))

            #Multiplayer
            elif action == "find_match":
                await manager.join_queue(username)
            elif action == "submit_arena_guess":
                await manager.process_guess(username, data.get("room_id"), data.get("guess"))
            elif action == "get_leaderboard":
                await websocket.send(json.dumps({"status": "leaderboard_data", "leaderboard": get_leaderboard_data()}))
            elif action == "send_chat":
                await manager.send_chat(username, data.get("room_id"), data.get("text"))
            elif action == "get_live_matches":
                await websocket.send(json.dumps({"status": "live_matches_data", "matches": manager.get_live_matches_data()}))
            elif action == "spectate_room":
                await manager.spectate_room(username, data.get("room_id"), websocket)

    except websockets.exceptions.ConnectionClosed:
        pass
    except Exception as e:
        print(f"❌ Error dari koneksi {username}: {e}")
    finally:
        if username:
            if manager.connections.get(username) == websocket:
                manager.connections.pop(username, None)
                if username in manager.queue: manager.queue.remove(username)
                room = manager._find_active_room(username)
                if room and not room.get("game_over"):
                    await manager.handle_disconnect_gracefully(username, room["room_id"])

async def run_server():
    async with websockets.serve(handler, "0.0.0.0", 8000):
        print("🚀 Server berjalan di ws://localhost:8000")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(run_server())
