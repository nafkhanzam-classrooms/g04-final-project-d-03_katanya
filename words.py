import random
import urllib.request
from datetime import datetime

KBBI_WORDS: set  = set()
KBBI_LIST: list  = []

def fetch_kbbi_words_from_internet():
    global KBBI_WORDS, KBBI_LIST
    print("🌐 [KATANYA] Sinkronisasi kosakata KBBI via internet...")
    try:
        url = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/id/id_50k.txt"
        with urllib.request.urlopen(url, timeout=8) as response:
            html = response.read().decode('utf-8')
            temp_set = set()
            for line in html.splitlines():
                parts = line.split()
                if parts:
                    word = parts[0].strip().upper()
                    if len(word) == 5 and word.isalpha():
                        temp_set.add(word)
            if len(temp_set) > 500:
                KBBI_WORDS = temp_set
                KBBI_LIST  = sorted(list(KBBI_WORDS))
                print(f"🚀 [KATANYA] {len(KBBI_WORDS)} kata 5 huruf dimuat dari internet.")
                return
    except Exception as e:
        print(f"⚠️  Gagal internet ({e}), pakai cadangan lokal.")

    KBBI_WORDS = {
        "UTAMA","SURYA","KUPAS","SUTRA","DUNIA","WAKTU","MAKAN","MINUM",
        "RUMAH","TANAH","POHON","PAPAN","KILAT","SURAT","BULAN","SAYUR",
        "BENAR","SALAH","CINTA","HUJAN","PASIR","MERAH","HIJAU","PUTIH",
        "HITAM","BESAR","KECIL","PINTU","KURSI","GELAS","MASUK","TARIK",
        "DUDUK","TIDUR","JALAN","BUNGA","KUNCI","MAWAR","ANGKA","KERAS",
        "LEMAH","TAJAM","BIJAK","RAJIN","HEMAT","GIGIH","SABAR","ADIL",
        "JUJUR","DAMAI","CEPAT","TEPAT","SEHAT","MAKAN","MINUM","TIDUR",
        "BUKU","MEJA","LAMPU","MOBIL","MOTOR","KAPAL","PESAWAT","KERETA",
    }
    KBBI_WORDS = {w for w in KBBI_WORDS if len(w) == 5 and w.isalpha()}
    KBBI_LIST  = sorted(list(KBBI_WORDS))
    print(f"✅ Memakai {len(KBBI_WORDS)} kata cadangan lokal.")

# Jalankan saat file di-import
fetch_kbbi_words_from_internet()

def evaluate_guess(guess: str, secret: str) -> list[str]:
    result  = ["absent"] * 5
    s_flags = [False] * 5
    g_flags = [False] * 5
    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "correct"
            s_flags[i] = True
            g_flags[i] = True
    for i in range(5):
        if g_flags[i]: continue
        for j in range(5):
            if not s_flags[j] and guess[i] == secret[j]:
                result[i]  = "present"
                s_flags[j] = True
                break
    return result

def get_daily_secret() -> str:
    if not KBBI_LIST: return "UTAMA"
    seed = int(datetime.now().strftime("%Y%m%d"))
    return random.Random(seed).choice(KBBI_LIST)
