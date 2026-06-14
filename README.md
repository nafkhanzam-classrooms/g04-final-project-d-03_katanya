
- `index.html` — struktur HTML aplikasi
- `script.js`  — logika JavaScript klien
- `style.css`  — gaya tampilan (CSS)

Catatan: angka di depan setiap baris merujuk ke baris relatif dalam file asal.

=== index.html ===

1 <!DOCTYPE html>
  — Deklarasi dokumen HTML5.
2 <html lang="id">
  — Elemen root, `lang="id"` menandakan bahasa Indonesia.
3 <head>
  — Mulai metadata dokumen.
4 <meta charset="UTF-8">
  — Menetapkan encoding karakter.
5 <meta name="viewport" content="width=device-width, initial-scale=1.0">
  — Memastikan tampilan responsif pada perangkat mobile.
6 <title>KATANYA - Tebak Kata Multiplayer</title>
  — Judul halaman.
7 <link rel="stylesheet" href="style.css">
  — Menghubungkan stylesheet eksternal.
8 </head>
  — Akhir head.
9 <body>
  — Konten utama dimulai.

10 <div id="ping-indicator">Ping: -- ms</div>
  — Menampilkan ping WebSocket (di-update oleh JS).
11 <div id="input-lock"></div>
  — Overlay untuk mencegah input saat terkunci.
12 <div id="toast-root"></div>
  — Root untuk menampung toast notifikasi.

13 <!-- AUTH SCREEN -->
14 <div id="auth-screen">
15   <div class="auth-box">
16     <h1>KATANYA</h1>
17     <p>Game Tebak Kata PvP Arena</p>
18     <input type="text" id="auth-user" placeholder="Username" autocomplete="off" maxlength="15">
      — Input username (JS baca `#auth-user`).
19     <input type="password" id="auth-pass" placeholder="Password" maxlength="20">
      — Input password (JS baca `#auth-pass`).
20     <button id="btn-login" class="btn full" onclick="doAuth('login')">Masuk (Login)</button>
      — Tombol login memanggil `doAuth('login')`.
21     <div class="auth-divider">── atau ──</div>
22     <button id="btn-reg" class="btn full ghost" onclick="doAuth('register')">Daftar Akun Baru</button>
      — Tombol register memanggil `doAuth('register')`.
23   </div>
24 </div>

25 <!-- SIDEBAR -->
26 <div class="sidebar">
27   <div class="logo">KATANYA</div>
28   <div class="logo-sub">PvP ARENA</div>
29   <div class="profile-badge">
30     👤 <span id="pf-name" style="font-weight:700;color:var(--green)">–</span><br>
      — Nama pengguna yang diisi oleh JS `updateProfile()`.
31     🏆 MMR: <span id="pf-mmr" style="font-weight:700;color:var(--gold)">–</span>
      — Rating MMR pengguna.
32     &nbsp;|&nbsp; W: <span id="pf-w" style="color:var(--green)">0</span>
33     L: <span id="pf-l" style="color:var(--red)">0</span>
34     D: <span id="pf-d" style="color:var(--muted)">0</span>
35   </div>
36   <button class="menu-btn active" onclick="nav('match')">🎮 Play Match</button>
37   <button class="menu-btn" onclick="nav('daily')">📅 Daily Quiz</button>
38   <button class="menu-btn" onclick="nav('practice')">🏋️ Practice</button>
39   <button class="menu-btn" onclick="nav('spectate')">👁️ Spectate</button>
40   <button class="menu-btn" onclick="nav('rank')">🏆 Leaderboard</button>
41   <button class="menu-btn danger" onclick="doLogout()">🚪 Logout</button>
      — Logout memanggil `doLogout()`.
42 </div>

43 <!-- MAIN -->
44 <div class="main">

45   <!-- MATCH -->
46   <div id="panel-match" class="panel active" style="margin-top:60px">
47     <div class="card">
48       <h2>⚔️ Live Matchmaking</h2>
49       <p style="color:var(--muted);margin-bottom:16px">Bertanding 1v1 real-time. Tebak kata yang sama lebih cepat dari lawan!</p>
50       <div style="font-size:1.1rem;margin-bottom:4px">Rating kamu: <strong id="dash-mmr" style="color:var(--gold);font-size:1.4rem">–</strong></div>
51       <button class="btn" id="btn-find" onclick="findMatch()">Cari Lawan</button>
52     </div>
53     <div class="card" style="border-left:3px solid var(--gold)">
54       <h2 style="color:var(--gold)">📅 Daily Quiz Hari Ini</h2>
55       <p id="daily-status-home" style="color:var(--muted);margin-bottom:14px">Satu kata khusus untuk semua pemain.</p>
56       <button class="btn gold sm" onclick="nav('daily')">Main Sekarang</button>
57     </div>
58   </div>

59   <!-- ARENA & SPECTATE UI -->
60   <div id="panel-arena" class="panel" style="max-width:940px;margin-top:20px">
61     <div style="display:flex;justify-content:space-between;align-items:center;width:100%;margin-bottom:16px;padding:0 4px">
62       <!-- P1 (Kamu) -->
63       <div class="arena-header-col" style="text-align:left;">
64         <div id="arena-my-tag" style="font-weight:700;color:var(--green);font-size:0.95rem">Kamu</div>
65         <div id="arena-my-status" style="color:var(--red); font-size:0.8rem; display:none; margin-top:4px; font-weight: bold;">Terputus (60s)</div>
66       </div>
67       <!-- Timer -->
68       <div class="timer-wrap">
69         <div id="timer-disp" class="timer-display">⏱ 05:00</div>
70         <div class="timer-bar"><div id="timer-fill" class="timer-fill" style="width:100%"></div></div>
71       </div>
72       <!-- P2 (Lawan) -->
73       <div class="arena-header-col" style="text-align:right;">
74         <div id="arena-opp-tag" style="font-weight:700;color:var(--gold);font-size:0.95rem">Lawan</div>
75         <div id="arena-opp-status" style="color:var(--red); font-size:0.8rem; display:none; margin-top:4px; font-weight: bold;">Terputus (60s)</div>
76       </div>
77     </div>

78     <div class="card" style="padding:20px; margin-bottom:10px;">
79       <div class="arena-wrap">
80         <div class="arena-col">
81           <div style="font-weight:700;color:var(--green);margin-bottom:6px" id="arena-my-label">Papan Kamu</div>
82           <div class="board" id="arena-board"></div>
83           <div class="keyboard" id="arena-kb"></div>
84         </div>
85         <div class="arena-col" style="opacity:0.72" id="opp-board-wrapper">
86           <div style="font-weight:700;color:var(--gold);margin-bottom:6px" id="arena-opp-label">Lawan</div>
87           <div class="board" id="arena-opp-board"></div>
88           <p id="arena-opp-info" style="font-size:0.75rem;color:var(--muted);margin-top:10px;text-align:center">Progres lawan (live)</p>
89         </div>
90       </div>
91     </div>

92     <!-- Live Chat -->
93     <div class="chat-wrap" id="arena-chat">
94         <div id="chat-box" class="chat-msgs"></div>
95         <div class="chat-input-row">
96             <input type="text" id="chat-input" placeholder="Ketik pesan..." maxlength="100" />
97             <button class="btn sm" onclick="sendChat()" style="margin:0;">Kirim</button>
98         </div>
99     </div>
100   </div>

101   <!-- REPLAY MATCH UI (NEW) -->
102   <div id="panel-replay" class="panel" style="max-width:940px;margin-top:40px">
103       <div class="card" style="padding:20px;">
104         <h2 style="text-align:center; color:var(--gold); margin-bottom: 5px;">🎥 REPLAY PERTANDINGAN</h2>
105         <p id="replay-secret" style="text-align:center; color:var(--muted); margin-bottom: 20px;">Kata Rahasia: ?????</p>
106         
107         <div class="arena-wrap">
108           <div class="arena-col">
109             <div style="font-weight:700;color:var(--green);margin-bottom:6px" id="replay-p1-label">Pemain 1</div>
110             <div class="board" id="replay-board-1"></div>
111           </div>
112           <div class="arena-col">
113             <div style="font-weight:700;color:var(--gold);margin-bottom:6px" id="replay-p2-label">Pemain 2</div>
114             <div class="board" id="replay-board-2"></div>
115           </div>
116         </div>

117         <div style="text-align:center; margin-top:30px;">
118             <button class="btn ghost" onclick="nav('match'); fetchLeaderboard();">Tutup & Kembali ke Menu</button>
119         </div>
120       </div>
121   </div>

122   <!-- SPECTATE LIST -->
123   <div id="panel-spectate" class="panel" style="margin-top:40px">
124     <div class="card">
125       <h2>👁️ Live Spectate</h2>
126       <p style="color:var(--muted);margin-bottom:16px">Tonton pertandingan yang sedang berlangsung.</p>
127       <button class="btn sm ghost" onclick="fetchLiveMatches()">🔄 Refresh List</button>
128       <table class="tbl" style="margin-top:16px;">
129         <thead><tr><th>Pemain 1</th><th>VS</th><th>Pemain 2</th><th>Aksi</th></tr></thead>
130         <tbody id="spectate-body"><tr><td colspan="4" style="color:var(--muted);text-align:center;padding:20px">Klik refresh untuk memuat...</td></tr></tbody>
131       </table>
132     </div>
133   </div>

134   <!-- DAILY -->
135   <div id="panel-daily" class="panel" style="margin-top:40px">
136     <div class="card">
137       <h2>📅 Daily Quiz</h2>
138       <p id="daily-countdown" style="color:var(--gold);font-size:0.88rem;margin:8px 0 16px">Kata baru dalam: --:--:--</p>
139       <div class="board" id="daily-board"></div>
140       <div class="keyboard" id="daily-kb"></div>
141       <button id="btn-share" class="btn gold" style="display:none;margin-top:20px" onclick="shareDaily()">🔗 Bagikan Hasil</button>
142     </div>
143   </div>

144   <!-- PRACTICE -->
145   <div id="panel-practice" class="panel" style="margin-top:40px">
146     <div class="card">
147       <h2>🏋️ Mode Latihan</h2>
148       <p style="color:var(--muted);margin-bottom:16px">Latihan tanpa batas. Kata baru setiap ronde.</p>
149       <div class="board" id="prac-board"></div>
150       <div class="keyboard" id="prac-kb"></div>
151       <button id="btn-next" class="btn" style="display:none;margin-top:16px" onclick="newPracticeWord()">Kata Berikutnya →</button>
152     </div>
153   </div>

154   <!-- RANK -->
155   <div id="panel-rank" class="panel" style="margin-top:40px">
156     <div class="card">
157       <h2>🏆 Leaderboard</h2>
158       <table class="tbl">
159         <thead><tr><th>#</th><th>Username</th><th>MMR</th><th>W</th><th>L</th><th>D</th><th>TOTAL</th></tr></thead>
160         <tbody id="lb-body"><tr><td colspan="7" style="color:var(--muted);text-align:center;padding:20px">Memuat...</td></tr></tbody>
161       </table>
162     </div>
163   </div>

164 </div>

165 <!-- MATCH MODAL -->
166 <div id="match-modal">
167   <div class="modal-box" id="modal-card">
168     <div class="modal-icon"  id="m-icon">🏆</div>
169     <div class="modal-title" id="m-title">MENANG!</div>
170     <div class="modal-sub"   id="m-sub">Pertandingan selesai.</div>
171     <div class="modal-secret">Kata rahasia:</div>
172     <div class="modal-word"  id="m-word">?????</div>
173     <div class="mmr-box" id="m-mmr-box">
174       <div class="mmr-label">Perubahan MMR</div>
175       <div class="mmr-delta" id="m-delta">+0</div>
176       <div class="mmr-new">Rating sekarang: <strong id="m-newmmr" style="color:var(--gold)">–</strong></div>
177     </div>
178     <button class="btn full" id="m-btn-1" onclick="modalPlayAgain()">Cari Lawan Lagi</button>
179     <!-- TOMBOL REPLAY (NEW) -->
180     <button class="btn full gold" id="m-btn-replay" onclick="showReplay()" style="display: none;">🎥 Lihat Replay</button>
181     <button class="btn full ghost" onclick="modalToDashboard()">Kembali ke Dashboard</button>
182   </div>
183 </div>

184 <script src="script.js"></script>

=== script.js ===

1 const API      = "http://127.0.0.1:8000";  // base API
2 const WS_BASE  = "ws://127.0.0.1:8000/ws/"; // base websocket
3 const ROWS = 6, COLS = 5; // board dimensions
4 const REVEAL_MS    = COLS * 150 + 380; // reveal animation timing
5 const MATCH_DUR    = 300; // match duration seconds
6 const KB_ROWS = [
  ["Q","W","E","R","T","Y","U","I","O","P"],
  ["A","S","D","F","G","H","J","K","L"],
  ["ENTER","Z","X","C","V","B","N","M","⌫"],
];
  — Keyboard layout array digunakan oleh `buildKB()`.

// State variables
15 let sessionUser  = "";            // username saat ini
16 let sessionMmr   = 0;             // mmr saat ini
17 let currentPanel = "match";      // panel aktif
18 let ws           = null;          // websocket instance
19 let roomId       = null;          // id room jika berada di match
20 let inputLocked  = false;         // apakah input dikunci
21 let arenaOppRow  = 0;             // progres baris lawan

// disconnect timers
22 let myDcInterval = null;
23 let oppDcInterval = null;

// spectate / replay
24 let isSpectating = false;
25 let specP1 = ""; let specP2 = "";
26 let replayData = null;

const B = {
  arena:    { r:0, c:0, g:"", over:false, secret:"" },
  daily:    { r:0, c:0, g:"", over:false },
  practice: { r:0, c:0, g:"", over:false, secret:"" },
};

const DAILY_KEY = "kat_daily_" + new Date().toISOString().slice(0,10);

function toast(msg, type = "") {
  const root = document.getElementById("toast-root");
  const el   = document.createElement("div");
  el.className   = "toast " + type;
  el.textContent = msg;
  root.appendChild(el);
  setTimeout(() => el.remove(), 3000);
}
  — Menampilkan notifikasi singkat; `type` mengontrol kelas (error/success).

setInterval(() => {
    if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({action: "ping", ts: Date.now()}));
    }
}, 2000);
  — Ping ke server via WS tiap 2 detik untuk mengukur latency.

async function doAuth(type) {
  const user = document.getElementById("auth-user")?.value.trim();
  const pass = document.getElementById("auth-pass")?.value;
  if (!user || !pass) { toast("Username dan password tidak boleh kosong!", "error"); return; }

  const btnLogin = document.getElementById("btn-login");
  const btnReg = document.getElementById("btn-reg");
  if(btnLogin) btnLogin.disabled = true;
  if(btnReg) btnReg.disabled = true;
  if (type === 'login' && btnLogin) btnLogin.textContent = "Memproses...";
  if (type === 'register' && btnReg) btnReg.textContent = "Memproses...";

  let data;
  try {
    const res  = await fetch(`${API}/${type}`, {
      method: "POST", headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ username: user, password: pass }),
    });
    data = await res.json();
    if (!res.ok) {
        toast(data.detail || "Terjadi kesalahan API.", "error");
        if(btnLogin) { btnLogin.disabled = false; btnLogin.textContent = "Masuk (Login)"; }
        if(btnReg) { btnReg.disabled = false; btnReg.textContent = "Daftar Akun Baru"; }
        return;
    }
  } catch(e) {
    toast("❌ Gagal terhubung ke API! Pastikan server berjalan.", "error");
    if(btnLogin) { btnLogin.disabled = false; btnLogin.textContent = "Masuk (Login)"; }
    if(btnReg) { btnReg.disabled = false; btnReg.textContent = "Daftar Akun Baru"; }
    return;
  }

  try {
    sessionUser = data.username;
    sessionMmr  = data.mmr;

    updateProfile(data);
    const authScreen = document.getElementById("auth-screen");
    if(authScreen) authScreen.style.display = "none";

    toast(type === "register" ? `✅ Akun dibuat!` : `👋 Selamat datang, ${data.username}!`, "success");

    buildBoard("prac-board",  "prac"); buildBoard("daily-board", "daily");
    buildKB("prac-kb",  "prac"); buildKB("daily-kb", "daily");
    restoreDaily(); newPracticeWord();

    if(!window.dailyIntervalTimer) { window.dailyIntervalTimer = setInterval(updateDailyCountdown, 1000); }
    updateDailyCountdown();

    initSocket();
  } catch (err) {} finally {
      if(btnLogin) { btnLogin.disabled = false; btnLogin.textContent = "Masuk (Login)"; }
      if(btnReg) { btnReg.disabled = false; btnReg.textContent = "Daftar Akun Baru"; }
  }
}

function initSocket() {
    if (!sessionUser) return;
    if (ws) { try { ws.close(); } catch(e){} ws = null; }
    ws = new WebSocket(WS_BASE + encodeURIComponent(sessionUser));
    ws.onmessage = e => handleWS(JSON.parse(e.data));
    ws.onclose = () => {
        if(sessionUser) { toast("Terputus dari server!", "error"); setTimeout(initSocket, 3000); }
    };
}

function doLogout() {
  sessionUser = ""; sessionMmr = 0;
  if (ws) { try { ws.close(); } catch(e){} ws = null; }
  const btnLogin = document.getElementById("btn-login");
  if(btnLogin) { btnLogin.disabled = false; btnLogin.textContent = "Masuk (Login)"; }
  document.getElementById("auth-screen").style.display = "flex";
  document.getElementById("auth-user").value = "";
  document.getElementById("auth-pass").value = "";
  if (myDcInterval) { clearInterval(myDcInterval); myDcInterval = null; }
  if (oppDcInterval) { clearInterval(oppDcInterval); oppDcInterval = null; }
}

function updateProfile(data) {
  const n = document.getElementById("pf-name"); if(n) n.textContent = data.username || sessionUser;
  const m = document.getElementById("pf-mmr"); if(m) m.textContent = data.mmr || sessionMmr;
  const w = document.getElementById("pf-w"); if(w) w.textContent = data.wins || 0;
  const l = document.getElementById("pf-l"); if(l) l.textContent = data.losses || 0;
  const d = document.getElementById("pf-d"); if(d) d.textContent = data.draws || 0;
  const dm = document.getElementById("dash-mmr"); if(dm) dm.textContent = (data.mmr || sessionMmr) + " MMR";
}

function nav(panel) {
  document.querySelectorAll(".panel").forEach(p => p.classList.remove("active"));
  document.querySelectorAll(".menu-btn").forEach(b => b.classList.remove("active"));
  const el = document.getElementById("panel-" + panel);
  if(el) el.classList.add("active");
  document.querySelectorAll(".menu-btn").forEach(b => {
    if ((b.getAttribute("onclick")||"").includes("'" + panel + "'")) b.classList.add("active");
  });
  currentPanel = panel;
  if (panel === "rank") fetchLeaderboard();
  if (panel === "spectate") fetchLiveMatches();
}

function buildBoard(id, prefix, small = false) {
  const el = document.getElementById(id);
  if (!el) return;
  el.innerHTML = "";
  for (let r = 0; r < ROWS; r++) {
    const row = document.createElement("div"); row.className = "board-row"; row.id = prefix + "-row-" + r;
    for (let c = 0; c < COLS; c++) {
      const t = document.createElement("div"); t.className = "tile" + (small ? " sm" : ""); t.id = prefix + "-t-" + r + "-" + c;
      row.appendChild(t);
    }
    el.appendChild(row);
  }
}

function buildKB(id, prefix) {
  const el = document.getElementById(id);
  if (!el) return;
  el.innerHTML = "";
  KB_ROWS.forEach(row => {
    const div = document.createElement("div"); div.className = "kb-row";
    row.forEach(k => {
      const btn = document.createElement("button"); btn.className = "key" + (k.length > 1 ? " wide" : "");
      btn.textContent = k; btn.id = prefix + "-k-" + k;
      btn.addEventListener("click", () => handleKey(prefix === "arena-opp" ? "arena" : prefix, k));
      div.appendChild(btn);
    });
    el.appendChild(div);
  });
}

function revealRow(prefix, row, letters, result, animate) {
  for (let c = 0; c < COLS; c++) {
    const t = document.getElementById(prefix + "-t-" + row + "-" + c);
    if (!t) continue;
    t.textContent = letters[c] || "";
    const paintFn = () => {
      const map = { correct: "var(--green)", present: "var(--yellow)", absent: "var(--absent)" };
      t.style.background = map[result[c]] || ""; t.style.borderColor = "transparent"; t.style.color = "#fff";
      if (prefix !== "opp" && prefix !== "rep1" && prefix !== "rep2") colorKey(prefix, letters[c], result[c]);
    };
    if (animate) { setTimeout(() => { t.classList.add("flip"); setTimeout(paintFn, 260); }, c * 150); }
    else { paintFn(); }
  }
}

function colorKey(prefix, ch, status) {
  const el = document.getElementById(prefix + "-k-" + ch);
  if (!el) return;
  const cur = el.style.background;
  if (cur === "var(--green)") return;
  if (cur === "var(--yellow)" && status === "absent") return;
  el.style.background = status === "correct" ? "var(--green)" : status === "present" ? "var(--yellow)" : "var(--absent)";
}

function shakeRow(prefix, row) {
  const el = document.getElementById(prefix + "-row-" + row);
  if (!el) return;
  el.classList.add("shake"); setTimeout(() => el.classList.remove("shake"), 450);
}

document.addEventListener("keydown", e => {
  if (!sessionUser) return;
  if (document.activeElement && (document.activeElement.tagName === "INPUT" || document.activeElement.tagName === "TEXTAREA")) return;
  const k = e.key === "Backspace" ? "⌫" : e.key.toUpperCase();
  const modeMap = { match: null, arena: "arena", daily: "daily", practice: "prac", rank: null };
  const mode = modeMap[currentPanel];
  if (mode) handleKey(mode, k);
});

document.getElementById("chat-input")?.addEventListener("keypress", function(e) {
    if(e.key === "Enter") sendChat();
});

function handleKey(mode, key) {
  if (mode === "arena" && (inputLocked || isSpectating)) return;
  const b = (mode === "prac") ? B.practice : B[mode];
  if (!b || b.over) return;
  if (b.r >= ROWS) return;

  if (key === "ENTER") {
    if (b.g.length < COLS) { shakeRow(mode, b.r); toast("Kata belum lengkap!"); return; }
    submitGuess(mode, b.g); return;
  }
  if (key === "⌫" || key === "BACKSPACE") {
    if (b.c > 0) { b.c--; b.g = b.g.slice(0, -1); const t = document.getElementById(mode + "-t-" + b.r + "-" + b.c); if (t) { t.textContent = ""; t.classList.remove("pop"); } }
    return;
  }
  if (/^[A-Z]$/.test(key) && b.c < COLS) {
    const t = document.getElementById(mode + "-t-" + b.r + "-" + b.c);
    if (t) { t.textContent = key; t.classList.add("pop"); }
    b.g += key; b.c++;
  }
}

async function submitGuess(mode, guess) {
  if (mode === "arena") {
    if (!ws || ws.readyState !== WebSocket.OPEN) { toast("Server terputus!", "error"); return; }
    ws.send(JSON.stringify({ action: "submit_arena_guess", room_id: roomId, guess })); return;
  }
  const isDaily = (mode === "daily");
  const url = isDaily ? `${API}/check-daily-guess` : `${API}/check-guess`;
  const body = isDaily ? { guess } : { guess, secret_word: B.practice.secret };

  try {
    const res = await fetch(url, { method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify(body) });
    const data = await res.json();
    const b = isDaily ? B.daily : B.practice;
    const prefix = isDaily ? "daily" : "prac";

    if (data.error) { shakeRow(prefix, b.r); toast(data.error, "error"); return; }

    const letters = guess.split("");
    revealRow(prefix, b.r, letters, data.result, true);
    b.r++; b.c = 0; b.g = "";

    if (isDaily) saveDailyRow(guess, data.result);
    if (data.is_win || b.r >= ROWS) {
      b.over = true;
      setTimeout(() => {
        if(data.is_win) toast(isDaily ? "🎉 Daily Selesai!" : "🎉 Benar!", "success");
        else toast("Kesempatan habis!", "error");
        if (isDaily) { saveDailyFinished(data.is_win); document.getElementById("btn-share").style.display = "inline-block"; }
        else { document.getElementById("btn-next").style.display = "inline-block"; }
      }, REVEAL_MS);
    }
  } catch(e) { toast("Server error!", "error"); }
}

async function newPracticeWord() {
  document.getElementById("btn-next").style.display = "none";
  try {
    const res = await fetch(`${API}/get-practice-secret`); const data = await res.json();
    B.practice = { r:0, c:0, g:"", over:false, secret: data.secret_word };
    buildBoard("prac-board", "prac"); buildKB("prac-kb", "prac");
  } catch(e) { toast("Gagal mengambil mode latihan!", "error"); }
}

function sendChat() {
    const input = document.getElementById("chat-input");
    const text = input.value.trim();
    if(text && ws && roomId) {
        ws.send(JSON.stringify({action: "send_chat", room_id: roomId, text: text}));
        input.value = "";
    }
}

function findMatch() {
  if (!sessionUser) { toast("Login dulu!", "error"); return; }
  const btn = document.getElementById("btn-find"); btn.disabled = true; btn.textContent = "Mencari lawan... 🔍";
  ws.send(JSON.stringify({ action: "find_match" }));
}

function fetchLiveMatches() {
    if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({ action: "get_live_matches" }));
    }
}

function watchMatch(rId) {
    if (ws) ws.send(JSON.stringify({ action: "spectate_room", room_id: rId }));
}

function resetFindBtn() { const btn = document.getElementById("btn-find"); if (btn) { btn.disabled = false; btn.textContent = "Cari Lawan"; } }

function handleWS(data) {
  const st = data.status;

  if (st === "pong") {
      const ms = Date.now() - data.ts;
      const indicator = document.getElementById("ping-indicator");
      if(indicator) indicator.textContent = `Ping: ${ms} ms`;
      return;
  }

  if (st === "searching") { toast("Sedang mencari lawan..."); return; }
  if (st === "timer_tick") { setTimerDisplay(data.remaining); return; }

  if (st === "chat_receive") {
      const box = document.getElementById("chat-box");
      const div = document.createElement("div"); div.className = "chat-msg";
      div.innerHTML = `<span class="sender">${data.sender}:</span> ${data.text}`;
      box.appendChild(div);
      box.scrollTop = box.scrollHeight;
      return;
  }

  if (st === "live_matches_data") {
      const tbody = document.getElementById("spectate-body");
      if(!data.matches || data.matches.length === 0) {
          tbody.innerHTML = '<tr><td colspan="4" style="color:var(--muted);text-align:center;">Tidak ada pertandingan live.</td></tr>';
      } else {
          tbody.innerHTML = data.matches.map(m => `
            <tr>
                <td>${m.p1} <span style="color:var(--muted)">(${m.score1}/6)</span></td>
                <td style="color:var(--gold);font-weight:bold;">VS</td>
                <td>${m.p2} <span style="color:var(--muted)">(${m.score2}/6)</span></td>
                <td><button class="btn sm" onclick="watchMatch('${m.room_id}')">Tonton</button></td>
            </tr>
          `).join("");
      }
      return;
  }

  if (st === "spectate_start") {
    try {
        roomId = data.room_id; isSpectating = true; inputLocked = true;
        specP1 = data.p1; specP2 = data.p2;

        const il = document.getElementById("input-lock"); if(il) il.style.display = "none";
        const akb = document.getElementById("arena-kb"); if(akb) akb.style.display = "none";
        const cb = document.getElementById("chat-box"); if(cb) cb.innerHTML = "";

        buildBoard("arena-board", "arena"); buildBoard("arena-opp-board", "opp");
        
        const mt = document.getElementById("arena-my-tag"); if(mt) mt.textContent = `[P1] ${specP1}`;
        const ot = document.getElementById("arena-opp-tag"); if(ot) ot.textContent = `[P2] ${specP2}`;
        const ml = document.getElementById("arena-my-label"); if(ml) ml.textContent = `Papan ${specP1}`;
        const ol = document.getElementById("arena-opp-label"); if(ol) ol.textContent = `Papan ${specP2}`;
        const oi = document.getElementById("arena-opp-info"); if(oi) oi.textContent = "Papan pemain 2";

        if (myDcInterval) { clearInterval(myDcInterval); myDcInterval = null; }
        if (oppDcInterval) { clearInterval(oppDcInterval); oppDcInterval = null; }
        const ms = document.getElementById("arena-my-status"); if(ms) ms.style.display = "none";
        const os = document.getElementById("arena-opp-status"); if(os) os.style.display = "none";

        B.arena.r = 0; arenaOppRow = 0;
        data.history_p1.forEach((item, i) => { revealRow("arena", i, item.guess.split(""), item.result, false); B.arena.r++; });
        data.history_p2.forEach((item, i) => { revealRow("opp", i, item.guess.split(""), item.result, false); arenaOppRow++; });

        setTimerDisplay(data.duration || MATCH_DUR);
        toast("Mulai menonton pertandingan", "success");
    } catch(err) {} finally {
        nav("arena");
    }
    return;
  }

  if (st === "match_start") {
    try {
        roomId = data.room_id; inputLocked = false; isSpectating = false; arenaOppRow = 0;
        B.arena = { r:0, c:0, g:"", over:false, secret:"" };

        const il = document.getElementById("input-lock"); if(il) il.style.display = "none";
        const akb = document.getElementById("arena-kb"); if(akb) akb.style.display = "flex";
        const cb = document.getElementById("chat-box"); if(cb) cb.innerHTML = ""; 

        if (myDcInterval) { clearInterval(myDcInterval); myDcInterval = null; }
        if (oppDcInterval) { clearInterval(oppDcInterval); oppDcInterval = null; }
        const ms = document.getElementById("arena-my-status"); if(ms) ms.style.display = "none";
        const os = document.getElementById("arena-opp-status"); if(os) os.style.display = "none";

        buildBoard("arena-board", "arena"); buildBoard("arena-opp-board", "opp"); buildKB("arena-kb", "arena");

        const uname = sessionUser; const opp = data.opponent;
        const mt = document.getElementById("arena-my-tag"); if(mt) mt.textContent  = `${uname} (${data.my_mmr} MMR)`;
        const ot = document.getElementById("arena-opp-tag"); if(ot) ot.textContent = `${opp} (${data.opp_mmr} MMR)`;
        const ml = document.getElementById("arena-my-label"); if(ml) ml.textContent  = `Papan ${uname}`;
        const ol = document.getElementById("arena-opp-label"); if(ol) ol.textContent = `Papan ${opp}`;
        const oi = document.getElementById("arena-opp-info"); if(oi) oi.textContent = "Progres lawan (live)";

        if (data.is_reconnect) {
          (data.history_self || []).forEach((item, i) => { revealRow("arena", i, item.guess.split(""), item.result, false); B.arena.r++; });
          (data.history_opp || []).forEach((item, i) => { revealRow("opp", i, Array(5).fill(" "), item.result, false); arenaOppRow++; });
          toast("🔄 Berhasil kembali ke game!", "success");
        } else {
          toast(`🎮 Lawan ditemukan: ${opp}!`, "success");
        }

        setTimerDisplay(data.duration || MATCH_DUR);
    } catch(err) {} finally {
        resetFindBtn(); nav("arena"); 
    }
    return;
  }

  if (st === "spectator_progress") {
      const letters = data.guess.split("");
      if (data.player === specP1) {
          revealRow("arena", B.arena.r, letters, data.result, true); B.arena.r++;
      } else if (data.player === specP2) {
          revealRow("opp", arenaOppRow, letters, data.result, true); arenaOppRow++;
      }
      return;
  }

  if (st === "opponent_disconnected") {
    let pName = data.player || "Lawan";
    let isP1 = isSpectating && (pName === specP1);
    let statusElId = isP1 ? "arena-my-status" : "arena-opp-status";

    toast(`⚠️ ${pName} terputus! Menunggu 60 detik...`, "error");
    const statusEl = document.getElementById(statusElId);
    let sec = 60;
    if(statusEl) { statusEl.style.display = "block"; statusEl.textContent = `Terputus (${sec}s)`; }

    if (isP1) {
        if (myDcInterval) clearInterval(myDcInterval);
        myDcInterval = setInterval(() => {
            sec--;
            if(statusEl) {
                if (sec <= 0) { clearInterval(myDcInterval); statusEl.textContent = `Keluar`; } 
                else { statusEl.textContent = `Terputus (${sec}s)`; }
            }
        }, 1000);
    } else {
        if (oppDcInterval) clearInterval(oppDcInterval);
        oppDcInterval = setInterval(() => {
            sec--;
            if(statusEl) {
                if (sec <= 0) { clearInterval(oppDcInterval); statusEl.textContent = `Keluar`; } 
                else { statusEl.textContent = `Terputus (${sec}s)`; }
            }
        }, 1000);
    }
    return;
  }

  if (st === "opponent_reconnected") {
    let pName = data.player || "Lawan";
    toast(`✅ ${pName} terhubung kembali!`, "success");
    
    let isP1 = isSpectating && (pName === specP1);
    let statusElId = isP1 ? "arena-my-status" : "arena-opp-status";

    if (isP1) { if (myDcInterval) { clearInterval(myDcInterval); myDcInterval = null; } } 
    else { if (oppDcInterval) { clearInterval(oppDcInterval); oppDcInterval = null; } }
    
    const statusEl = document.getElementById(statusElId);
    if(statusEl) statusEl.style.display = "none";
    return;
  }

  if (st === "guess_result_self") {
    const row = B.arena.r; const letters = B.arena.g.split("");
    revealRow("arena", row, letters, data.result, true); B.arena.r++; B.arena.c = 0; B.arena.g = ""; return;
  }

  if (st === "guess_error") { shakeRow("arena", B.arena.r); toast(data.message, "error"); return; }

  if (st === "opponent_progress") { revealRow("opp", arenaOppRow, Array(5).fill(" "), data.result, true); arenaOppRow++; return; }

  if (st === "match_over" || st === "match_over_spectator") {
    inputLocked = true; B.arena.over = true;
    
    if (myDcInterval) { clearInterval(myDcInterval); myDcInterval = null; }
    if (oppDcInterval) { clearInterval(oppDcInterval); oppDcInterval = null; }
    
    const myStat = document.getElementById("arena-my-status"); if(myStat) myStat.style.display = "none";
    const oppStat = document.getElementById("arena-opp-status"); if(oppStat) oppStat.style.display = "none";
    
    const lockEl = document.getElementById("input-lock");
    if (lockEl) lockEl.style.display = "block";

    let outcome = "DRAW";
    let delta = 0;
    let newMmr = sessionMmr;
    let secret = data.secret || "?????";
    let reason = data.reason_msg || "Pertandingan Selesai.";
    let myAtt = 0;
    let oppAtt = 0;
    let winnerName = null;
    let p1Name = null;
    let p2Name = null;

    if (st === "match_over_spectator") {
        outcome = "SPECTATOR";
        myAtt = data.attempts_p1 || 0;
        oppAtt = data.attempts_p2 || 0;
        winnerName = data.winner;
        p1Name = data.p1;
        p2Name = data.p2;
        replayData = { p1: data.p1, p2: data.p2, secret: secret, hist1: data.history_p1 || [], hist2: data.history_p2 || [] };
    } else {
        outcome = data.outcome || "DRAW";
        delta = (typeof data.mmr_delta === 'number') ? data.mmr_delta : 0;
        newMmr = data.new_mmr || sessionMmr;
        myAtt = data.my_attempts || 0;
        oppAtt = data.opp_attempts || 0;
        
        sessionMmr = newMmr;
        const pfMmr = document.getElementById("pf-mmr"); if(pfMmr) pfMmr.textContent = newMmr;
        const dashMmr = document.getElementById("dash-mmr"); if(dashMmr) dashMmr.textContent = newMmr + " MMR";

        replayData = { p1: sessionUser, p2: data.p2, secret: secret, hist1: data.history_self || [], hist2: data.history_opp || [] };
    }

    setTimeout(() => {
      showMatchModal(outcome, delta, newMmr, secret, reason, myAtt, oppAtt, winnerName, p1Name, p2Name);
    }, REVEAL_MS);
    return;
  }

  if (st === "leaderboard_data") { renderLeaderboard(data.leaderboard || []); return; }
}

function setTimerDisplay(remaining) {
  const disp = document.getElementById("timer-disp");
  const fill = document.getElementById("timer-fill");
  if (!disp || !fill) return;

  const mm = String(Math.floor(remaining / 60)).padStart(2, "0");
  const ss = String(remaining % 60).padStart(2, "0");
  disp.textContent = `⏱ ${mm}:${ss}`;

  const pct = (remaining / MATCH_DUR) * 100;
  if(!isNaN(pct)) fill.style.width = pct + "%";

  disp.classList.remove("warn", "crit");
  if (remaining <= 30) {
    fill.style.background = "var(--red)";
    disp.classList.add("crit");
  } else if (remaining <= 60) {
    fill.style.background = "var(--yellow)";
    disp.classList.add("warn");
  } else {
    fill.style.background = "var(--green)";
  }
}

function showMatchModal(outcome, delta, newMmr, secret, reason, myAtt, oppAtt, winner=null, p1=null, p2=null) {
  const icon = document.getElementById("m-icon"), title = document.getElementById("m-title"), sub = document.getElementById("m-sub"), word = document.getElementById("m-word"), dEl = document.getElementById("m-delta"), nEl = document.getElementById("m-newmmr"), card = document.getElementById("modal-card");
  const sign = delta > 0 ? "+" : (delta === 0 ? "+" : "");

  if (outcome === "WIN") {
    icon.textContent = "🏆"; title.textContent = "KAMU MENANG!"; title.style.color = "var(--green)"; card.style.borderColor = "var(--green)"; sub.textContent = reason; dEl.className = "mmr-delta up";
    sub.textContent += ` (Percobaanmu: ${myAtt}/6 | Lawan: ${oppAtt}/6)`;
  } else if (outcome === "LOSE") {
    icon.textContent = "💀"; title.textContent = "KAMU KALAH"; title.style.color = "var(--red)"; card.style.borderColor = "var(--red)"; sub.textContent = reason; dEl.className = "mmr-delta down";
    sub.textContent += ` (Percobaanmu: ${myAtt}/6 | Lawan: ${oppAtt}/6)`;
  } else if (outcome === "DRAW") {
    icon.textContent = "🤝"; title.textContent = "SERI!"; title.style.color = "var(--yellow)"; card.style.borderColor = "var(--yellow)"; sub.textContent = reason; dEl.className = "mmr-delta draw";
    sub.textContent += ` (Percobaanmu: ${myAtt}/6 | Lawan: ${oppAtt}/6)`;
  } else if (outcome === "SPECTATOR") {
    icon.textContent = "👁️"; title.style.color = "var(--gold)"; card.style.borderColor = "var(--gold)";
    if (winner) { title.textContent = `${winner} MENANG!`; } else { title.textContent = "SERI!"; }
    sub.textContent = `Pertandingan Selesai. (${p1}: ${myAtt}/6 | ${p2}: ${oppAtt}/6)`;
  }

  word.textContent = secret;
  dEl.textContent = `${sign}${delta}`; nEl.textContent = newMmr;

  const modal = document.getElementById("match-modal");
  if(modal) modal.style.display = "flex";
  
  const mmrBox = document.getElementById("m-mmr-box");
  const btn1 = document.getElementById("m-btn-1");
  const btnReplay = document.getElementById("m-btn-replay");

  if(btnReplay && replayData) { btnReplay.style.display = "inline-block"; }

  if (isSpectating) {
     if(mmrBox) mmrBox.style.display = "none";
     if(btn1) btn1.style.display = "none";
  } else {
     if(mmrBox) mmrBox.style.display = "block";
     if(btn1) btn1.style.display = "inline-block";
  }
}

function showReplay() {
    const modal = document.getElementById("match-modal"); if(modal) modal.style.display = "none"; 
    const lock = document.getElementById("input-lock"); if(lock) lock.style.display = "none";
    nav("replay");
    buildBoard("replay-board-1", "rep1"); buildBoard("replay-board-2", "rep2");
    document.getElementById("replay-p1-label").textContent = `Papan ${replayData.p1}`;
    document.getElementById("replay-p2-label").textContent = `Papan ${replayData.p2}`;
    document.getElementById("replay-secret").textContent = `Kata Rahasia: ${replayData.secret}`;

    replayData.hist1.forEach((item, i) => { revealRow("rep1", i, item.guess.split(""), item.result, false); });
    replayData.hist2.forEach((item, i) => { revealRow("rep2", i, item.guess.split(""), item.result, false); });
}

function modalToDashboard() {
  const modal = document.getElementById("match-modal"); if(modal) modal.style.display = "none"; 
  const lock = document.getElementById("input-lock"); if(lock) lock.style.display = "none";
  inputLocked = false; isSpectating = false; nav("match"); fetchLeaderboard();
}

function modalPlayAgain() {
  const modal = document.getElementById("match-modal"); if(modal) modal.style.display = "none"; 
  const lock = document.getElementById("input-lock"); if(lock) lock.style.display = "none";
  inputLocked = false; isSpectating = false; nav("match"); setTimeout(findMatch, 300);
}

async function fetchLeaderboard() {
  if (ws && ws.readyState === WebSocket.OPEN) { ws.send(JSON.stringify({ action: "get_leaderboard" })); return; }
  try { const res  = await fetch(`${API}/get-leaderboard`); const data = await res.json(); renderLeaderboard(data.leaderboard || []); } 
  catch(e) { 
      const tbody = document.getElementById("lb-body");
      if(tbody) tbody.innerHTML = '<tr><td colspan="7" style="color:var(--muted);text-align:center;padding:20px">Gagal memuat. Pastikan server berjalan.</td></tr>'; 
  }
}

function renderLeaderboard(list) {
  const tbody  = document.getElementById("lb-body");
  const medals = ["🥇","🥈","🥉"];
  if (!list || !list.length) { 
      if(tbody) tbody.innerHTML = '<tr><td colspan="7" style="color:var(--muted);text-align:center;padding:20px">Belum ada data.</td></tr>'; 
      return; 
  }
  if(tbody) {
      tbody.innerHTML = list.map((p, i) => `
        <tr style="${p.username === sessionUser ? 'background:rgba(83,141,78,0.14)' : ''}">
          <td>${medals[i] || (i+1)}</td>
          <td style="font-weight:600">${p.username}${p.username === sessionUser ? ' <span style="color:var(--green);font-size:0.72rem">(Kamu)</span>' : ''}</td>
          <td style="color:var(--gold);font-weight:700">${p.mmr}</td>
          <td style="color:var(--green)">${p.wins}</td>
          <td style="color:var(--red)">${p.losses}</td>
          <td style="color:var(--muted)">${p.draws}</td>
          <td>${p.total || 0}</td>
        </tr>`).join("");
  }
}

function restoreDaily() {
  try {
    const saved = JSON.parse(localStorage.getItem(DAILY_KEY));
    if (!saved || !saved.rows) return;
    saved.rows.forEach((r, i) => revealRow("daily", i, r.g.split(""), r.res, false));
    B.daily.r = saved.rows.length; B.daily.c = 0; B.daily.g = "";
    if (saved.done) { 
        B.daily.over = true; 
        const bs = document.getElementById("btn-share"); if(bs) bs.style.display = "inline-block"; 
        const ds = document.getElementById("daily-status-home"); if(ds) ds.textContent = "✨ Sudah dimainkan hari ini!"; 
    }
  } catch(e) {}
}

function saveDailyRow(guess, result) {
  const d = JSON.parse(localStorage.getItem(DAILY_KEY) || '{"rows":[],"done":false}');
  d.rows.push({ g: guess, res: result });
  localStorage.setItem(DAILY_KEY, JSON.stringify(d));
}

function saveDailyFinished(won) {
  const d = JSON.parse(localStorage.getItem(DAILY_KEY) || '{"rows":[],"done":false}');
  d.done = true; d.won = won;
  localStorage.setItem(DAILY_KEY, JSON.stringify(d));
}

function shareDaily() {
  try {
    const d = JSON.parse(localStorage.getItem(DAILY_KEY));
    if (!d) return;
    const date  = new Date().toLocaleDateString("id-ID");
    const score = d.won ? d.rows.length : "X";
    let   text  = `KATANYA Daily ${date} ${score}/6\n\n`;
    d.rows.forEach(r => {
      text += r.res.map(s => s === "correct" ? "🟩" : s === "present" ? "🟨" : "⬛").join("") + "\n";
    });
    navigator.clipboard.writeText(text).then(() => toast("Hasil disalin ke clipboard!", "success"));
  } catch(e) { toast("Gagal menyalin.", "error"); }
}

function updateDailyCountdown() {
  const now  = new Date();
  const next = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
  const diff = next - now;
  const hh   = String(Math.floor(diff / 3.6e6)).padStart(2, "0");
  const mm   = String(Math.floor((diff % 3.6e6) / 6e4)).padStart(2, "0");
  const ss   = String(Math.floor((diff % 6e4) / 1e3)).padStart(2, "0");
  const el   = document.getElementById("daily-countdown");
  if (el) el.textContent = `Kata baru dalam: ${hh}:${mm}:${ss}`;
}

=== style.css ===

:root { --bg: #121213; --sidebar: #1e1e1f; --card: #262627; --green: #538d4e; --yellow: #b59f3b; --absent: #3a3a3c; --red: #c54242; --text: #ffffff; --muted: #979798; --border: #3a3a3c; --gold: #ffb703; }
  — Variabel tema global (warna dan aksen) yang dipakai di seluruh CSS.

* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Roboto, Arial, sans-serif; background: var(--bg); color: var(--text); display: flex; height: 100vh; overflow: hidden; }
  — Reset dasar dan layout root: membuat sidebar + main berdampingan.

/* AUTH SCREEN */
#auth-screen { position: fixed; inset: 0; background: var(--bg); z-index: 999; display: flex; justify-content: center; align-items: center; }
.auth-box { background: var(--sidebar); padding: 44px 40px; border-radius: 16px; box-shadow: 0 12px 40px rgba(0,0,0,0.6); width: 100%; max-width: 380px; text-align: center; }
.auth-box input { width: 100%; padding: 13px 14px; margin: 7px 0; border-radius: 8px; border: 2px solid var(--border); background: var(--bg); color: #fff; }

/* TOAST */
#toast-root { position: fixed; top: 20px; left: 50%; transform: translateX(-50%); z-index: 9999; display: flex; flex-direction: column; align-items: center; gap: 8px; pointer-events: none; min-width: 200px; }
.toast { background: #fff; color: #111; padding: 11px 24px; border-radius: 8px; font-weight: 700; box-shadow: 0 6px 20px rgba(0,0,0,0.45); animation: toastPop 2.8s ease forwards; white-space: nowrap; }

/* SIDEBAR */
.sidebar { width: 248px; background: var(--sidebar); display: flex; flex-direction: column; padding: 22px 14px; border-right: 1px solid #2a2a2b; flex-shrink: 0; }
.logo { font-size: 1.9rem; font-weight: 900; letter-spacing: 5px; color: var(--green); text-align: center; margin-bottom: 6px; }
.menu-btn { background: none; border: none; color: var(--muted); padding: 12px 18px; text-align: left; font-size: 0.97rem; font-weight: 600; cursor: pointer; border-radius: 8px; margin-bottom: 4px; }
.menu-btn.active { background: var(--card); color: var(--text); border-left: 4px solid var(--green); padding-left: 14px; }

/* MAIN & PANELS */
.main { flex: 1; padding: 36px; display: flex; justify-content: center; align-items: flex-start; overflow-y: auto; position: relative; }
.panel { display: none; width: 100%; max-width: 660px; flex-direction: column; align-items: center; animation: fadeUp 0.25s ease; }
.panel.active { display: flex; }

/* BOARD & TILES */
.board { display: grid; grid-template-rows: repeat(6,1fr); gap: 5px; margin: 18px auto; width: max-content; }
.board-row { display: grid; grid-template-columns: repeat(5,1fr); gap: 5px; }
.tile { width: 54px; height: 54px; border: 2px solid var(--border); display: flex; align-items: center; justify-content: center; font-size: 1.75rem; font-weight: 700; text-transform: uppercase; user-select: none; transition: border-color 0.08s; }
.tile.flip { animation: flip 0.52s ease forwards; }

/* KEYBOARD */
.keyboard { width: 100%; max-width: 490px; display: flex; flex-direction: column; gap: 5px; margin-top: 14px; }
.kb-row { display: flex; justify-content: center; gap: 4px; }
.key { background: #818384; color: #fff; border: none; border-radius: 4px; height: 52px; flex: 1; font-weight: 700; display: flex; align-items: center; justify-content: center; }

/* MODAL & INPUT LOCK */
#match-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.82); z-index: 2000; justify-content: center; align-items: center; backdrop-filter: blur(5px); }
.modal-box { background: var(--sidebar); border-radius: 18px; padding: 44px 48px; width: 100%; max-width: 420px; text-align: center; box-shadow: 0 16px 50px rgba(0,0,0,0.7); border: 2px solid var(--border); }
#input-lock { display: none; position: fixed; inset: 0; z-index: 500; pointer-events: all; cursor: not-allowed; }

---
