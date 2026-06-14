# KATANYA - Dokumentasi Front-End

Dokumentasi ini menjelaskan semua bagian utama `index.html`, `script.js`, dan `style.css`.

---

## index.html

### Head dan assets

```html
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KATANYA - Tebak Kata Multiplayer</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
```

- `<!DOCTYPE html>` — Menetapkan dokumen sebagai HTML5.
- `<html lang="id">` — Elemen root dengan bahasa Indonesia.
- `<head>` — Mulai metadata dokumen.
- `<meta charset="UTF-8">` — Mengatur encoding karakter UTF-8.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` — Membuat responsif pada perangkat mobile.
- `<title>...</title>` — Judul halaman yang ditampilkan pada tab browser.
- `<link rel="stylesheet" href="style.css">` — Memuat stylesheet utama.
- `</head>` — Menutup blok head.
- `<body>` — Mulai konten halaman.

### Overlay helper dan toast

```html
<div id="ping-indicator">Ping: -- ms</div>
<div id="input-lock"></div>
<div id="toast-root"></div>
```

- `<div id="ping-indicator">Ping: -- ms</div>` — Indikator ping WebSocket live.
- `<div id="input-lock"></div>` — Overlay untuk mengunci input saat permainan selesai.
- `<div id="toast-root"></div>` — Root container untuk notifikasi toast.

### Layar autentikasi

```html
<!-- AUTH SCREEN -->
<div id="auth-screen">
  <div class="auth-box">
    <h1>KATANYA</h1>
    <p>Game Tebak Kata PvP Arena</p>
    <input type="text" id="auth-user" placeholder="Username" autocomplete="off" maxlength="15">
    <input type="password" id="auth-pass" placeholder="Password" maxlength="20">
    <button id="btn-login" class="btn full" onclick="doAuth('login')">Masuk (Login)</button>
    <div class="auth-divider">── atau ──</div>
    <button id="btn-reg" class="btn full ghost" onclick="doAuth('register')">Daftar Akun Baru</button>
  </div>
</div>
```

- `<!-- AUTH SCREEN -->` — Komentar HTML untuk penanda blok autentikasi.
- `<div id="auth-screen">` — Kontainer layar login besar.
- `<div class="auth-box">` — Kotak login dengan styling khusus.
- `<h1>KATANYA</h1>` — Judul aplikasi.
- `<p>Game Tebak Kata PvP Arena</p>` — Deskripsi singkat.
- `<input type="text" id="auth-user" ...>` — Input username.
- `<input type="password" id="auth-pass" ...>` — Input password.
- `<button id="btn-login" ... onclick="doAuth('login')">` — Tombol login memanggil fungsi `doAuth('login')`.
- `<div class="auth-divider">── atau ──</div>` — Pemisah visual antara tombol.
- `<button id="btn-reg" ... onclick="doAuth('register')">` — Tombol registrasi memanggil `doAuth('register')`.

### Sidebar navigasi

```html
<!-- SIDEBAR -->
<div class="sidebar">
  <div class="logo">KATANYA</div>
  <div class="logo-sub">PvP ARENA</div>
  <div class="profile-badge">
    👤 <span id="pf-name" style="font-weight:700;color:var(--green)">–</span><br>
    🏆 MMR: <span id="pf-mmr" style="font-weight:700;color:var(--gold)">–</span>
    &nbsp;|&nbsp; W: <span id="pf-w" style="color:var(--green)">0</span>
    L: <span id="pf-l" style="color:var(--red)">0</span>
    D: <span id="pf-d" style="color:var(--muted)">0</span>
  </div>
  <button class="menu-btn active" onclick="nav('match')">🎮 Play Match</button>
  <button class="menu-btn" onclick="nav('daily')">📅 Daily Quiz</button>
  <button class="menu-btn" onclick="nav('practice')">🏋️ Practice</button>
  <button class="menu-btn" onclick="nav('spectate')">👁️ Spectate</button>
  <button class="menu-btn" onclick="nav('rank')">🏆 Leaderboard</button>
  <button class="menu-btn danger" onclick="doLogout()">🚪 Logout</button>
</div>
```

- `<div class="sidebar">` — Kontainer panel samping.
- `<div class="logo">` dan `<div class="logo-sub">` — Judul aplikasi dan subjudul.
- `<div class="profile-badge">` — Menampilkan username dan statistik MMR, menang/kalah/draw.
- `id="pf-name"`, `id="pf-mmr"`, `id="pf-w"`, `id="pf-l"`, `id="pf-d"` — Elemen terikat data profil.
- Tombol menu menggunakan `onclick="nav('...')"` untuk berpindah antar panel.
- Tombol logout memanggil `doLogout()`.

### Panel MATCH

```html
<!-- MAIN -->
<div class="main">

  <!-- MATCH -->
  <div id="panel-match" class="panel active" style="margin-top:60px">
    <div class="card">
      <h2>⚔️ Live Matchmaking</h2>
      <p style="color:var(--muted);margin-bottom:16px">Bertanding 1v1 real-time. Tebak kata yang sama lebih cepat dari lawan!</p>
      <div style="font-size:1.1rem;margin-bottom:4px">Rating kamu: <strong id="dash-mmr" style="color:var(--gold);font-size:1.4rem">–</strong></div>
      <button class="btn" id="btn-find" onclick="findMatch()">Cari Lawan</button>
    </div>
    <div class="card" style="border-left:3px solid var(--gold)">
      <h2 style="color:var(--gold)">📅 Daily Quiz Hari Ini</h2>
      <p id="daily-status-home" style="color:var(--muted);margin-bottom:14px">Satu kata khusus untuk semua pemain.</p>
      <button class="btn gold sm" onclick="nav('daily')">Main Sekarang</button>
    </div>
  </div>
```

- `<div class="main">` — Kontainer utama konten yang di-scroll.
- `<div id="panel-match" class="panel active">` — Panel dashboard pertandingan aktif.
- `<h2>⚔️ Live Matchmaking</h2>` — Judul panel matchmaking.
- `<p>...</p>` — Deskripsi singkat.</n- `id="dash-mmr"` — Menampilkan MMR pengguna.
- `id="btn-find"` — Tombol untuk memulai pencarian lawan.
- Card kedua menyorot Daily Quiz dan tombol menuju panel `daily`.

### Panel ARENA

```html
  <!-- ARENA & SPECTATE UI -->
  <div id="panel-arena" class="panel" style="max-width:940px;margin-top:20px">
    <div style="display:flex;justify-content:space-between;align-items:center;width:100%;margin-bottom:16px;padding:0 4px">
      <!-- P1 (Kamu) -->
      <div class="arena-header-col" style="text-align:left;">
        <div id="arena-my-tag" style="font-weight:700;color:var(--green);font-size:0.95rem">Kamu</div>
        <div id="arena-my-status" style="color:var(--red); font-size:0.8rem; display:none; margin-top:4px; font-weight: bold;">Terputus (60s)</div>
      </div>
      <!-- Timer -->
      <div class="timer-wrap">
        <div id="timer-disp" class="timer-display">⏱ 05:00</div>
        <div class="timer-bar"><div id="timer-fill" class="timer-fill" style="width:100%"></div></div>
      </div>
      <!-- P2 (Lawan) -->
      <div class="arena-header-col" style="text-align:right;">
        <div id="arena-opp-tag" style="font-weight:700;color:var(--gold);font-size:0.95rem">Lawan</div>
        <div id="arena-opp-status" style="color:var(--red); font-size:0.8rem; display:none; margin-top:4px; font-weight: bold;">Terputus (60s)</div>
      </div>
    </div>

    <div class="card" style="padding:20px; margin-bottom:10px;">
      <div class="arena-wrap">
        <div class="arena-col">
          <div style="font-weight:700;color:var(--green);margin-bottom:6px" id="arena-my-label">Papan Kamu</div>
          <div class="board" id="arena-board"></div>
          <div class="keyboard" id="arena-kb"></div>
        </div>
        <div class="arena-col" style="opacity:0.72" id="opp-board-wrapper">
          <div style="font-weight:700;color:var(--gold);margin-bottom:6px" id="arena-opp-label">Lawan</div>
          <div class="board" id="arena-opp-board"></div>
          <p id="arena-opp-info" style="font-size:0.75rem;color:var(--muted);margin-top:10px;text-align:center">Progres lawan (live)</p>
        </div>
      </div>
    </div>

    <!-- Live Chat -->
    <div class="chat-wrap" id="arena-chat">
        <div id="chat-box" class="chat-msgs"></div>
        <div class="chat-input-row">
            <input type="text" id="chat-input" placeholder="Ketik pesan..." maxlength="100" />
            <button class="btn sm" onclick="sendChat()" style="margin:0;">Kirim</button>
        </div>
    </div>
  </div>
```

- Bagian atas menampilkan judul pemain, timer, dan informasi lawan.
- `#arena-board` dan `#arena-opp-board` adalah papan tebakan utama.
- `#arena-kb` adalah keyboard virtual untuk input arena.
- `#chat-box` menampung pesan chat.
- Input chat `#chat-input` dan tombol `Kirim` memanggil `sendChat()`.

### Panel REPLAY

```html
  <!-- REPLAY MATCH UI (NEW) -->
  <div id="panel-replay" class="panel" style="max-width:940px;margin-top:40px">
      <div class="card" style="padding:20px;">
        <h2 style="text-align:center; color:var(--gold); margin-bottom: 5px;">🎥 REPLAY PERTANDINGAN</h2>
        <p id="replay-secret" style="text-align:center; color:var(--muted); margin-bottom: 20px;">Kata Rahasia: ?????</p>
        
        <div class="arena-wrap">
          <div class="arena-col">
            <div style="font-weight:700;color:var(--green);margin-bottom:6px" id="replay-p1-label">Pemain 1</div>
            <div class="board" id="replay-board-1"></div>
          </div>
          <div class="arena-col">
            <div style="font-weight:700;color:var(--gold);margin-bottom:6px" id="replay-p2-label">Pemain 2</div>
            <div class="board" id="replay-board-2"></div>
          </div>
        </div>

        <div style="text-align:center; margin-top:30px;">
            <button class="btn ghost" onclick="nav('match'); fetchLeaderboard();">Tutup & Kembali ke Menu</button>
        </div>
      </div>
  </div>
```

- Panel replay menampilkan papan revisi untuk dua pemain.
- `#replay-secret` menampilkan kata rahasia pertandingan.
- Tombol kembali mengambil pengguna ke dashboard.

### Panel SPECTATE

```html
  <!-- SPECTATE LIST -->
  <div id="panel-spectate" class="panel" style="margin-top:40px">
    <div class="card">
      <h2>👁️ Live Spectate</h2>
      <p style="color:var(--muted);margin-bottom:16px">Tonton pertandingan yang sedang berlangsung.</p>
      <button class="btn sm ghost" onclick="fetchLiveMatches()">🔄 Refresh List</button>
      <table class="tbl" style="margin-top:16px;">
        <thead><tr><th>Pemain 1</th><th>VS</th><th>Pemain 2</th><th>Aksi</th></tr></thead>
        <tbody id="spectate-body"><tr><td colspan="4" style="color:var(--muted);text-align:center;padding:20px">Klik refresh untuk memuat...</td></tr></tbody>
      </table>
    </div>
  </div>
```

- Menampilkan daftar pertandingan live yang bisa ditonton.
- `#spectate-body` diisi dinamis oleh JavaScript.
- Tombol refresh memanggil `fetchLiveMatches()`.

### Panel DAILY

```html
  <!-- DAILY -->
  <div id="panel-daily" class="panel" style="margin-top:40px">
    <div class="card">
      <h2>📅 Daily Quiz</h2>
      <p id="daily-countdown" style="color:var(--gold);font-size:0.88rem;margin:8px 0 16px">Kata baru dalam: --:--:--</p>
      <div class="board" id="daily-board"></div>
      <div class="keyboard" id="daily-kb"></div>
      <button id="btn-share" class="btn gold" style="display:none;margin-top:20px" onclick="shareDaily()">🔗 Bagikan Hasil</button>
    </div>
  </div>
```

- Panel Daily Quiz memiliki countdown `#daily-countdown`.
- `#daily-board` dan `#daily-kb` adalah papan dan keyboard mode daily.
- Tombol `#btn-share` muncul setelah menyelesaikan daily quiz.

### Panel PRACTICE

```html
  <!-- PRACTICE -->
  <div id="panel-practice" class="panel" style="margin-top:40px">
    <div class="card">
      <h2>🏋️ Mode Latihan</h2>
      <p style="color:var(--muted);margin-bottom:16px">Latihan tanpa batas. Kata baru setiap ronde.</p>
      <div class="board" id="prac-board"></div>
      <div class="keyboard" id="prac-kb"></div>
      <button id="btn-next" class="btn" style="display:none;margin-top:16px" onclick="newPracticeWord()">Kata Berikutnya →</button>
    </div>
  </div>
```

- Panel latihan tanpa batas menampilkan papan `#prac-board`.
- Tombol `#btn-next` untuk mendapatkan kata latihan baru.

### Panel RANK

```html
  <!-- RANK -->
  <div id="panel-rank" class="panel" style="margin-top:40px">
    <div class="card">
      <h2>🏆 Leaderboard</h2>
      <table class="tbl">
        <thead><tr><th>#</th><th>Username</th><th>MMR</th><th>W</th><th>L</th><th>D</th><th>TOTAL</th></tr></thead>
        <tbody id="lb-body"><tr><td colspan="7" style="color:var(--muted);text-align:center;padding:20px">Memuat...</td></tr></tbody>
      </table>
    </div>
  </div>
```

- Leaderboard menampilkan peringkat pemain.
- `#lb-body` diisi secara dinamis oleh fungsi JavaScript.

### Match Modal

```html
<!-- MATCH MODAL -->
<div id="match-modal">
  <div class="modal-box" id="modal-card">
    <div class="modal-icon"  id="m-icon">🏆</div>
    <div class="modal-title" id="m-title">MENANG!</div>
    <div class="modal-sub"   id="m-sub">Pertandingan selesai.</div>
    <div class="modal-secret">Kata rahasia:</div>
    <div class="modal-word"  id="m-word">?????</div>
    <div class="mmr-box" id="m-mmr-box">
      <div class="mmr-label">Perubahan MMR</div>
      <div class="mmr-delta" id="m-delta">+0</div>
      <div class="mmr-new">Rating sekarang: <strong id="m-newmmr" style="color:var(--gold)">–</strong></div>
    </div>
    <button class="btn full" id="m-btn-1" onclick="modalPlayAgain()">Cari Lawan Lagi</button>
    <!-- TOMBOL REPLAY (NEW) -->
    <button class="btn full gold" id="m-btn-replay" onclick="showReplay()" style="display: none;">🎥 Lihat Replay</button>
    <button class="btn full ghost" onclick="modalToDashboard()">Kembali ke Dashboard</button>
  </div>
</div>

<script src="script.js"></script>
</body>
</html>
```

- `#match-modal` adalah overlay modal hasil pertandingan.
- `#m-icon`, `#m-title`, `#m-sub` menampilkan status hasil.
- `#m-word` menampilkan kata rahasia.
- `#m-delta` dan `#m-newmmr` menampilkan perubahan rating.
- Tombol `modalPlayAgain()` dan `modalToDashboard()` mengontrol alur setelah match.
- `#m-btn-replay` muncul untuk melihat replay jika tersedia.
- `script.js` dimuat di akhir body.

---

## script.js

### Konstanta dan state global

```js
const API      = "http://127.0.0.1:8000";
const WS_BASE  = "ws://127.0.0.1:8000/ws/";
const ROWS = 6, COLS = 5;
const REVEAL_MS    = COLS * 150 + 380;
const MATCH_DUR    = 300; 
const KB_ROWS = [
  ["Q","W","E","R","T","Y","U","I","O","P"],
  ["A","S","D","F","G","H","J","K","L"],
  ["ENTER","Z","X","C","V","B","N","M","⌫"],
];

let sessionUser  = "";
let sessionMmr   = 0;
let currentPanel = "match";
let ws           = null;
let roomId       = null;
let inputLocked  = false;
let arenaOppRow  = 0;

let myDcInterval = null;
let oppDcInterval = null;

let isSpectating = false;
let specP1 = "";
let specP2 = "";

let replayData = null;

const B = {
  arena:    { r:0, c:0, g:"", over:false, secret:"" },
  daily:    { r:0, c:0, g:"", over:false },
  practice: { r:0, c:0, g:"", over:false, secret:"" },
};
const DAILY_KEY = "kat_daily_" + new Date().toISOString().slice(0,10);
```

- `API` dan `WS_BASE` — URL dasar API HTTP dan WebSocket.
- `ROWS`, `COLS` — Ukuran board 6x5.
- `REVEAL_MS` — Waktu animasi reveal baris.
- `MATCH_DUR` — Durasi match dalam detik.
- `KB_ROWS` — Konfigurasi keyboard virtual.
- `sessionUser`, `sessionMmr`, `currentPanel` — State sesi pengguna.
- `ws`, `roomId` — Koneksi WebSocket dan ID room.
- `inputLocked`, `arenaOppRow` — Kontrol input dan baris lawan.
- `myDcInterval`, `oppDcInterval` — Interval timer disconnect.
- `isSpectating`, `specP1`, `specP2` — Status spectate.
- `replayData` — Data replay pertandingan.
- `B` — State board untuk `arena`, `daily`, dan `practice`.
- `DAILY_KEY` — Kunci localStorage untuk daily berdasarkan tanggal sekarang.

### Fungsi `toast`

```js
function toast(msg, type = "") {
  const root = document.getElementById("toast-root");
  const el   = document.createElement("div");
  el.className   = "toast " + type;
  el.textContent = msg;
  root.appendChild(el);
  setTimeout(() => el.remove(), 3000);
}
```

- `root` — Elemen container toast.
- `el` — Membuat elemen div baru.
- `el.className` — Menambahkan kelas `toast` dan tipe seperti `error`/`success`.
- `el.textContent` — Menetapkan pesan toast.
- `root.appendChild(el)` — Menampilkan toast.
- `setTimeout(...)` — Menghapus toast setelah 3 detik.

### Ping WebSocket otomatis

```js
setInterval(() => {
    if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({action: "ping", ts: Date.now()}));
    }
}, 2000);
```

- Mengirim pesan ping setiap 2 detik jika WebSocket terbuka.
- `action: "ping"` digunakan oleh server untuk menanggapi `pong`.
- `ts: Date.now()` mencatat timestamp.

### Autentikasi dan inisialisasi sesi

```js
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
```

- `user`/`pass` diambil dari input dan divalidasi.
- Tombol login/register dinonaktifkan selama permintaan.
- `fetch(`${API}/${type}`)` — Memanggil endpoint `/login` atau `/register`.
- Jika gagal, tampilkan toast dan reset tombol.
- Jika berhasil, simpan `sessionUser` dan `sessionMmr`.
- `updateProfile(data)` memperbarui profil sidebar.
- Sembunyikan `#auth-screen`.
- Bangun papan dan keyboard untuk practice/daily.
- `restoreDaily()` memulihkan progress daily sebelumnya.
- `newPracticeWord()` mengambil kata latihan baru.
- `initSocket()` memulai koneksi WebSocket.

### Inisialisasi WebSocket dan logout

```js
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
```

- `initSocket()` membuat koneksi WS ke `ws://.../ws/<username>`.
- `ws.onmessage` mem-parsing JSON data masuk dan meneruskannya ke `handleWS()`.
- `ws.onclose` memicu reconnect setelah 3 detik.
- `doLogout()` mereset state dan menampilkan layar login kembali.
- Interval disconnect dibersihkan pada logout.

### Update profil dan navigasi

```js
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
```

- `updateProfile(data)` mengisi teks profil pada sidebar.
- `nav(panel)` menonaktifkan semua panel dan tombol.
- Kemudian aktifkan panel tujuan.
- Panel `rank` memanggil `fetchLeaderboard()`.
- Panel `spectate` memanggil `fetchLiveMatches()`.

### Membangun board dan keyboard

```js
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
```

- `buildBoard` membersihkan kontainer dan membuat 6 baris berisi 5 tile.
- Setiap tile diberi ID unik `prefix-t-row-col`.
- `buildKB` membuat keyboard virtual berdasarkan `KB_ROWS`.
- Tombol yang memiliki teks panjang (`ENTER`, `⌫`) diberi kelas `wide`.
- Event click tombol memanggil `handleKey()`.

### Reveal, warna, dan animasi board

```js
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
```

- `revealRow` mengisi tile dengan huruf dan memberi warna berdasarkan `result`.
- `paintFn` menentukan warna `correct`, `present`, dan `absent`.
- Jika `animate`, tambahkan kelas `flip` dan jalankan pewarnaan setelah delay.
- `colorKey` memperbarui keyboard virtual kecuali pada board `opp` atau replay.
- `shakeRow` menambahkan efek goyang untuk row invalid.

### Input keyboard global dan chat enter

```js
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
```

- Event `keydown` bekerja di seluruh dokumen.
- Jika pengguna belum login atau sedang mengetik di input lain, event diabaikan.
- `Backspace` dikonversi menjadi `⌫`.
- `currentPanel` menentukan `mode` input.
- Enter pada chat memanggil `sendChat()`.

### Menangani tombol virtual dan input

```js
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
```

- `handleKey` melarang input saat spectating atau arena terkunci.
- `b` memilih state board yang sesuai.
- Jika mode sudah selesai atau sudah mencapai maksimum baris, input diabaikan.
- `ENTER` memvalidasi panjang kata lalu memanggil `submitGuess()`.
- `⌫` menghapus karakter terakhir dari `b.g` dan tile saat ini.
- Huruf valid (`A-Z`) ditambahkan ke board dan state.

### Mengirim tebakan untuk semua mode

```js
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
```

- Jika `mode === "arena"`, kirim tebakan melalui WebSocket.
- Untuk `daily` dan `practice`, gunakan endpoint HTTP lokal.
- `check-daily-guess` untuk daily, `check-guess` untuk practice.
- Validasi error dari server dan tampilkan shake effect bila perlu.
- `revealRow` menampilkan hasil tebakan.
- `b.r++` melanjutkan ke baris berikutnya.
- Jika menang atau habis baris, atur `b.over` dan tampilkan status selesai.
- Daily menyimpan hasil ke localStorage.

### Practice baru

```js
async function newPracticeWord() {
  document.getElementById("btn-next").style.display = "none";
  try {
    const res = await fetch(`${API}/get-practice-secret`); const data = await res.json();
    B.practice = { r:0, c:0, g:"", over:false, secret: data.secret_word };
    buildBoard("prac-board", "prac"); buildKB("prac-kb", "prac");
  } catch(e) { toast("Gagal mengambil mode latihan!", "error"); }
}
```

- Meminta kata rahasia latihan baru dari API.
- Menyimpan secret pada `B.practice.secret`.
- Membangun ulang board dan keyboard practice.

### Chat dan matchmaking

```js
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
```

- `sendChat()` mengirim pesan chat live ke server.
- `findMatch()` mulai mencari lawan lewat WebSocket.
- `fetchLiveMatches()` meminta daftar pertandingan yang sedang berjalan.
- `watchMatch(rId)` masuk ke mode spectate pada room tertentu.
- `resetFindBtn()` mengembalikan tombol pencarian lawan.

### Penanganan event WebSocket

```js
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
```

- `handleWS(data)` adalah dispatcher utama dari event WebSocket.
- `pong` mengukur latensi dan memperbarui `#ping-indicator`.
- `searching` menampilkan toast saat mencari lawan.
- `timer_tick` memanggil `setTimerDisplay()`.
- `chat_receive` menambahkan pesan ke chat box dan menggulir ke bawah.

### Live matches dan spectate start

```js
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
```

- `live_matches_data` merender tabel spectate.
- Jika tidak ada match, menampilkan pesan kosong.
- `spectate_start` mengatur state spectating dan mematikan keyboard input.
- `specP1`/`specP2` menyimpan nama pemain yang disaksikan.
- `buildBoard` dibangun ulang untuk whiteboard dan lawan.
- History pertandingan sebelumnya ditampilkan tanpa animasi.
- `nav("arena")` menavigasi ke panel arena.

### Match start dan progres permainan

```js
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
```

- `match_start` mempersiapkan pertandingan baru dan menampilkan nama lawan.
- `inputLocked` dimatikan agar pemain dapat mengetik.
- Keyboard arena ditampilkan.
- Jika reconnect, history sendiri dan lawan ditampilkan.
- `spectator_progress` memperbarui baris tebakan pemain yang disaksikan.

### Disconnect dan error lawan

```js
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
```

- `opponent_disconnected` menampilkan peringatan dan menghitung mundur 60 detik.
- Status disconnect ditampilkan pada elemen yang sesuai.
- Interval timer dibersihkan saat reconnect.

### Progress tebakan dan match over

```js
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
```

- `guess_result_self` menampilkan tebakan pemain sendiri.
- `guess_error` menampilkan shake saat tebakan invalid.
- `opponent_progress` memperbarui progress lawan.
- `match_over` dan `match_over_spectator` menutup input dan menampilkan modal.
- `inputLocked` true mencegah keyboard arena bekerja.
- Status disconnect disembunyikan.
- `replayData` disimpan untuk replay.
- `showMatchModal(...)` dipanggil setelah delay animasi.
- `leaderboard_data` membuat tabel leaderboard.

### Timer dan modal

```js
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
```

- Menghitung menit dan detik dari `remaining`.
- Memperbarui teks `#timer-disp`.
- Mengubah lebar `#timer-fill` berdasarkan persentase sisa waktu.
- Menambahkan kelas `warn` atau `crit` untuk perubahan warna.

```js
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
```

- `showMatchModal` menampilkan hasil akhir pertandingan.
- `icon`, `title`, dan `sub` disesuaikan berdasarkan `outcome`.
- `secret` dan `delta` ditampilkan.
- `btnReplay` muncul bila data replay tersedia.
- Jika spectating, tombol ulang dan MMR disembunyikan.

```js
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
```

- `showReplay()` menutup modal dan menampilkan panel replay.
- `buildBoard` membuat papan replay.
- Replay history ditampilkan tanpa animasi.
- `modalToDashboard()` kembali ke dashboard dan memuat leaderboard.
- `modalPlayAgain()` menutup modal lalu mencari lawan baru.

### Leaderboard

```js
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
```

- `fetchLeaderboard()` meminta leaderboard lewat WebSocket bila tersedia.
- Jika WS tidak tersedia, fallback ke API HTTP.
- `renderLeaderboard(list)` membuat baris tabel berdasarkan data.
- Baris sendiri diberi highlight.
- `medals` digunakan untuk tiga posisi teratas.

### Daily persistence dan countdown

```js
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
```

- `restoreDaily()` memulihkan progress daily dari `localStorage`.
- `saveDailyRow()` menambahkan satu baris tebakan ke storage.
- `saveDailyFinished()` menandai daily selesai.
- `shareDaily()` membuat teks hasil daily dalam format emoji dan menyalinnya ke clipboard.
- `updateDailyCountdown()` menghitung mundur ke tengah malam berikutnya.

---

## style.css

### Tema warna global

```css
:root {
  --bg: #121213; --sidebar: #1e1e1f; --card: #262627;
  --green: #538d4e; --yellow: #b59f3b; --absent: #3a3a3c;
  --red: #c54242; --text: #ffffff; --muted: #979798;
  --border: #3a3a3c; --gold: #ffb703;
}
```

- Variabel CSS tema dasar untuk background, warna teks, border, dan aksen.
- `--gold` digunakan untuk highlight.

### Reset dan body

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Roboto, Arial, sans-serif; background: var(--bg); color: var(--text); display: flex; height: 100vh; overflow: hidden; }
```

- Reset margin/padding dan box sizing global.
- `body` menggunakan font modern dan layout flex horizontal.
- `overflow: hidden` mencegah scroll body saat konten di dalamnya discroll.

### Layar autentikasi

```css
#auth-screen { position: fixed; inset: 0; background: var(--bg); z-index: 999; display: flex; justify-content: center; align-items: center; }
.auth-box { background: var(--sidebar); padding: 44px 40px; border-radius: 16px; box-shadow: 0 12px 40px rgba(0,0,0,0.6); width: 100%; max-width: 380px; text-align: center; }
.auth-box h1 { color: var(--green); letter-spacing: 6px; font-size: 2rem; margin-bottom: 4px; }
.auth-box p  { color: var(--muted); font-size: 0.88rem; margin-bottom: 28px; }
.auth-box input { width: 100%; padding: 13px 14px; margin: 7px 0; border-radius: 8px; border: 2px solid var(--border); background: var(--bg); color: #fff; font-size: 1rem; }
.auth-box input:focus { border-color: var(--green); outline: none; }
.auth-divider { color: var(--muted); font-size: 0.8rem; margin: 12px 0 4px; }
```

- `#auth-screen` menutup seluruh layar.
- `.auth-box` menampilkan kotak login dengan padding dan bayangan.
- Input mendapat border, background gelap, dan fokus hijau.

### Toast

```css
#toast-root { position: fixed; top: 20px; left: 50%; transform: translateX(-50%); z-index: 9999; display: flex; flex-direction: column; align-items: center; gap: 8px; pointer-events: none; min-width: 200px; }
.toast { background: #fff; color: #111; padding: 11px 24px; border-radius: 8px; font-weight: 700; font-size: 0.92rem; box-shadow: 0 6px 20px rgba(0,0,0,0.45); animation: toastPop 2.8s ease forwards; white-space: nowrap; }
.toast.error { background: #ff4444; color: #fff; }
.toast.success { background: var(--green); color: #fff; }
@keyframes toastPop { 0%{opacity:0;transform:translateY(-14px) scale(0.95);} 12%{opacity:1;transform:translateY(0) scale(1);} 80%{opacity:1;} 100%{opacity:0;transform:translateY(-8px);} }
```

- `#toast-root` memposisikan toast di atas layar.
- `.toast` mendefinisikan tampilan pop-up toast.
- `.toast.error` dan `.toast.success` memberi warna berbeda.
- Animasi `toastPop` membuat notifikasi muncul dan hilang.

### Ping indicator

```css
#ping-indicator { position: fixed; top: 16px; right: 24px; color: var(--green); font-size: 0.85rem; font-weight: bold; z-index: 999; }
```

- Indikator ping diposisikan fixed di sudut kanan atas.

### Sidebar

```css
.sidebar { width: 248px; background: var(--sidebar); display: flex; flex-direction: column; padding: 22px 14px; border-right: 1px solid #2a2a2b; flex-shrink: 0; }
.logo { font-size: 1.9rem; font-weight: 900; letter-spacing: 5px; color: var(--green); text-align: center; margin-bottom: 6px; }
.logo-sub { font-size: 0.68rem; color: var(--muted); text-align: center; letter-spacing: 2px; margin-bottom: 22px; }
.profile-badge { background: var(--bg); border-radius: 8px; padding: 12px 14px; margin-bottom: 24px; border: 1px solid var(--border); font-size: 0.88rem; line-height: 1.7; }
.menu-btn { background: none; border: none; color: var(--muted); padding: 12px 18px; text-align: left; font-size: 0.97rem; font-weight: 600; cursor: pointer; border-radius: 8px; margin-bottom: 4px; transition: all 0.15s; display: flex; align-items: center; gap: 10px; }
.menu-btn:hover, .menu-btn.active { background: var(--card); color: var(--text); }
.menu-btn.active { border-left: 4px solid var(--green); padding-left: 14px; }
.menu-btn.danger { color: var(--red); margin-top: auto; }
```

- Sidebar memiliki lebar tetap dan latar gelap.
- Logo aplikasi ditonjolkan warna hijau.
- `profile-badge` menampung statistik pengguna.
- Tombol menu berubah warna saat hover atau aktif.
- Tombol logout diletakkan di bawah dengan warna merah.

### Main content dan panel

```css
.main { flex: 1; padding: 36px; display: flex; justify-content: center; align-items: flex-start; overflow-y: auto; position: relative; }
.panel { display: none; width: 100%; max-width: 660px; flex-direction: column; align-items: center; animation: fadeUp 0.25s ease; }
.panel.active { display: flex; }
@keyframes fadeUp { from {opacity:0;transform:translateY(10px);} to {opacity:1;transform:translateY(0);} }
.card { background: var(--card); border-radius: 14px; padding: 28px; width: 100%; margin-bottom: 20px; }
.card h2 { font-size: 1.25rem; margin-bottom: 8px; }
```

- `.main` adalah konten utama dinámic dengan scroll vertikal.
- `.panel` tersembunyi secara default, dipakai hanya saat aktif.
- `.card` adalah kartu konten dengan background kontras.
- Animasi fadeUp membuat transisi panel lebih halus.

### Tombol

```css
.btn { background: var(--green); color: #fff; border: none; padding: 14px 40px; font-size: 1.05rem; font-weight: 700; border-radius: 8px; cursor: pointer; transition: all 0.2s; margin-top: 14px; display: inline-block; }
.btn:hover:not(:disabled) { background: #5fa356; transform: translateY(-1px); }
.btn:disabled { background: var(--absent); color: var(--muted); cursor: not-allowed; transform: none; }
.btn.full { width: 100%; margin-top: 10px; }
.btn.ghost { background: var(--absent); }
.btn.gold { background: var(--gold); color: #000; }
.btn.sm { padding: 9px 20px; font-size: 0.88rem; margin-top: 0; }
```

- Tombol utama berwarna hijau dengan transisi hover.
- Tombol disabled berwarna abu-abu.
- Variasi `full`, `ghost`, `gold`, dan `sm` mengubah ukuran dan warna.

### Board dan tile

```css
.board { display: grid; grid-template-rows: repeat(6,1fr); gap: 5px; margin: 18px auto; width: max-content; }
.board-row { display: grid; grid-template-columns: repeat(5,1fr); gap: 5px; }
.tile { width: 54px; height: 54px; border: 2px solid var(--border); display: flex; align-items: center; justify-content: center; font-size: 1.75rem; font-weight: 700; text-transform: uppercase; user-select: none; transition: border-color 0.08s; }
.tile.sm { width: 42px; height: 42px; font-size: 1.3rem; }
.tile.pop { animation: pop 0.1s ease; border-color: #606062; }
@keyframes pop { 50% { transform: scale(1.12); } }
.tile.flip { animation: flip 0.52s ease forwards; }
@keyframes flip { 0%{transform:rotateX(0);} 45%{transform:rotateX(90deg);background:transparent;} 55%{transform:rotateX(90deg);} 100%{transform:rotateX(0);border-color:transparent;color:#fff;} }
.board-row.shake { animation: shake 0.45s ease; }
@keyframes shake { 15%,45%,75%{transform:translateX(-6px)} 30%,60%,90%{transform:translateX(6px)} }
```

- `.board` membuat grid 6 baris.
- `.board-row` membuat lima kolom tile.
- `.tile` mendefinisikan kotak huruf dengan border dan gaya teks.
- `.tile.sm` untuk ukuran lebih kecil di board replay.
- `.tile.pop` memberikan animasi pop saat karakter dimasukkan.
- `.tile.flip` menambahkan animasi membalik saat reveal.
- `.board-row.shake` memberi efek error.

### Keyboard virtual

```css
.keyboard { width: 100%; max-width: 490px; display: flex; flex-direction: column; gap: 5px; margin-top: 14px; }
.kb-row { display: flex; justify-content: center; gap: 4px; }
.key { background: #818384; color: #fff; border: none; border-radius: 4px; height: 52px; flex: 1; font-weight: 700; font-size: 0.9rem; cursor: pointer; display: flex; align-items: center; justify-content: center; text-transform: uppercase; transition: background 0.15s; user-select: none; }
.key.wide { flex: 1.5; font-size: 0.78rem; }
.key:hover { background: #9a9c9d; }
```

- `.keyboard` adalah wrapper untuk baris tombol.
- Setiap `.key` distyling seperti tombol papan ketik.
- `.key.wide` dipakai untuk tombol `ENTER` dan `⌫`.
- Hover memberikan efek visual.

### Arena dan timer

```css
.arena-wrap { display: flex; gap: 44px; justify-content: center; align-items: flex-start; width: 100%; max-width: 920px; }
.arena-col { display: flex; flex-direction: column; align-items: center; }
.arena-header-col { flex: 1; }

timer-wrap { display: flex; flex-direction: column; align-items: center; gap: 4px; }
.timer-display { font-size: 1.55rem; font-weight: 800; padding: 6px 22px; border-radius: 30px; border: 2px solid var(--green); background: var(--card); letter-spacing: 2px; }
.timer-display.warn { border-color: var(--yellow); color: var(--yellow); }
.timer-display.crit { border-color: var(--red); color: var(--red); animation: pulse 0.55s infinite alternate; }
@keyframes pulse { to { transform: scale(1.04); } }
.timer-bar { width: 280px; height: 5px; background: var(--border); border-radius: 3px; overflow: hidden; }
.timer-fill { height: 100%; background: var(--green); border-radius: 3px; transition: width 1s linear, background 0.4s; }
```

- `.arena-wrap` menata dua kolom papan arena.
- `.timer-display` menampilkan countdown waktu.
- `.timer-fill` berubah lebar seiring waktu.
- `.warn` dan `.crit` memberi efek visual saat waktu mendesak.

### Chat

```css
.chat-wrap { width: 100%; max-width: 760px; margin-top: 24px; background: var(--card); border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 10px; }
.chat-msgs { flex: 1; height: 140px; overflow-y: auto; font-size: 0.88rem; padding: 10px; background: var(--bg); border-radius: 8px; border: 1px solid var(--border); }
.chat-msg { margin-bottom: 6px; line-height: 1.4; word-wrap: break-word;}
.chat-msg .sender { font-weight: 700; color: var(--green); margin-right: 6px; }
.chat-input-row { display: flex; gap: 8px; }
.chat-input-row input { flex: 1; padding: 12px; border-radius: 8px; background: var(--bg); border: 1px solid var(--border); color: #fff; outline: none; }
.chat-input-row input:focus { border-color: var(--green); }
```

- `chat-wrap` memformat area chat.
- `chat-msgs` adalah kotak scrollable untuk pesan.
- `chat-msg .sender` membedakan nama pengirim.
- `chat-input-row` menata input dan tombol chat.

### Modal pertandingan dan tabel

```css
#match-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.82); z-index: 2000; justify-content: center; align-items: center; backdrop-filter: blur(5px); }
.modal-box { background: var(--sidebar); border-radius: 18px; padding: 44px 48px; width: 100%; max-width: 420px; text-align: center; box-shadow: 0 16px 50px rgba(0,0,0,0.7); border: 2px solid var(--border); animation: fadeUp 0.3s ease; }
.modal-icon { font-size: 4.5rem; margin-bottom: 12px; }
.modal-title { font-size: 2.1rem; font-weight: 900; letter-spacing: 2px; margin-bottom: 6px; }
.modal-sub { color: var(--muted); font-size: 0.92rem; margin-bottom: 20px; }
.modal-secret{ font-size: 0.8rem; color: var(--muted); margin-bottom: 6px; }
.modal-word { font-size: 1.6rem; font-weight: 800; letter-spacing: 8px; color: var(--gold); margin-bottom: 22px; }
.mmr-box { background: var(--bg); border: 1px solid var(--border); border-radius: 10px; padding: 16px; margin-bottom: 26px; }
.mmr-label { font-size: 0.78rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }
.mmr-delta { font-size: 2.2rem; font-weight: 900; margin: 4px 0; }
.mmr-delta.up { color: var(--green); }
.mmr-delta.down { color: var(--red); }
.mmr-delta.draw { color: var(--yellow); }
.mmr-new { font-size: 0.9rem; }

.tbl { width: 100%; border-collapse: collapse; font-size: 0.88rem; margin-top: 16px; }
.tbl th { padding: 10px 10px; color: var(--muted); border-bottom: 1px solid var(--border); text-align: left; font-size: 0.76rem; text-transform: uppercase; letter-spacing: 0.8px; }
.tbl td { padding: 13px 10px; border-bottom: 1px solid #1f1f20; }
#input-lock { display: none; position: fixed; inset: 0; z-index: 500; pointer-events: all; cursor: not-allowed; }
```

- `#match-modal` adalah overlay fullscreen modal.
- `.modal-box` menampilkan detail hasil pertandingan.
- `.modal-word` menonjolkan kata rahasia.
- `.mmr-box` menunjukkan perubahan MMR.
- `.tbl` styling tabel leaderboard dan spectate.
- `#input-lock` menahan input ketika permainan selesai.

---

## Ringkasan

Aplikasi front-end `KATANYA` membangun UI login, panel menu, match arena, daily quiz, practice, spectate, leaderboard, dan modal hasil.
JavaScript menangani autentikasi, WebSocket, papan permainan, input keyboard, event WebSocket, replay, dan localStorage daily.
CSS mendukung tema gelap, animasi board, tombol, dan tata letak dashboard.

