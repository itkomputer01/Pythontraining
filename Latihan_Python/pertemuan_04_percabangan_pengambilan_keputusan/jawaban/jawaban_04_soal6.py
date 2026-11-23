# Pertemuan 4 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Sebuah toko memberi diskon: belanja ≥ Rp500.000 diskon 10%, ≥ Rp200.000
#   diskon 5%, selain itu tanpa diskon. Anggota (input y/n) mendapat tambahan
#   diskon 2%. Hitung total bayar.
# ------------------------------------------------------------

belanja = float(input("Total belanja: "))
anggota = input("Anggota? (y/n): ").lower() == "y"

if belanja >= 500000:
    diskon = 10
elif belanja >= 200000:
    diskon = 5
else:
    diskon = 0

if anggota:
    diskon += 2

bayar = belanja * (100 - diskon) / 100
print(f"Diskon {diskon}%, total bayar Rp{bayar:,.0f}")

# Contoh output:
#   Total belanja: 600000
#   Anggota? (y/n): y
#   Diskon 12%, total bayar Rp528,000
