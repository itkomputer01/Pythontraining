# Pertemuan 9 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Kode berikut memiliki bug. Jelaskan penyebab keluarannya dan perbaiki.
# ------------------------------------------------------------

# Penjelasan: Keluaran kode asli adalah ['apel'] lalu ['apel', 'jeruk'],
# karena list default dibuat satu kali dan dipakai bersama. Perbaikan:

def tambah_item(item, keranjang=None):
    if keranjang is None:
        keranjang = []
    keranjang.append(item)
    return keranjang

print(tambah_item("apel"))
print(tambah_item("jeruk"))

# Contoh output:
#   ['apel']
#   ['jeruk']
