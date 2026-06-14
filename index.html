<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KATANYA - Tebak Kata Multiplayer</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<div id="ping-indicator">Ping: -- ms</div>
<div id="input-lock"></div>
<div id="toast-root"></div>

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

</div>

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