# Pertemuan 8 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Dictionary nilai = {"Ani": 85, "Budi": 70, "Cici": 92}. Tentukan rata-rata
#   dan nama siswa dengan nilai tertinggi.
# ------------------------------------------------------------

nilai = {"Ani": 85, "Budi": 70, "Cici": 92}
rata = sum(nilai.values()) / len(nilai)
terbaik = max(nilai, key=nilai.get)
print(f"Rata-rata: {rata:.2f}")
print("Tertinggi:", terbaik, nilai[terbaik])

# Contoh output:
#   Rata-rata: 82.33
#   Tertinggi: Cici 92
