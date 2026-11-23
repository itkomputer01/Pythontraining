# Pertemuan 12 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Buat fungsi catat(pesan) yang menambahkan baris log berformat [2026-11-23
#   09:15:00] pesan ke file log.txt (gunakan datetime).
# ------------------------------------------------------------

from datetime import datetime

def catat(pesan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{waktu}] {pesan}\n")

catat("Program dimulai")
catat("Proses selesai")
