# Pertemuan 3 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Seseorang menabung Rp5.000.000 dengan bunga 4,5% per tahun. Hitung saldo
#   setelah 1 tahun dan tampilkan dengan pemisah ribuan tanpa desimal, contoh:
#   Saldo: Rp5,225,000.
# ------------------------------------------------------------

tabungan = 5000000
saldo = tabungan * (1 + 4.5 / 100)
print(f"Saldo: Rp{saldo:,.0f}")

# Contoh output:
#   Saldo: Rp5,225,000
