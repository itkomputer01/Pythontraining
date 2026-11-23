# Pertemuan 11 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Minta tanggal lahir (tahun, bulan, tanggal) dari pengguna, lalu hitung umur
#   dalam tahun penuh pada hari ini.
# ------------------------------------------------------------

from datetime import date

th = int(input("Tahun lahir: "))
bl = int(input("Bulan lahir: "))
tg = int(input("Tanggal lahir: "))

lahir = date(th, bl, tg)
hari_ini = date.today()
umur = hari_ini.year - lahir.year
if (hari_ini.month, hari_ini.day) < (lahir.month, lahir.day):
    umur -= 1
print("Umur:", umur, "tahun")
