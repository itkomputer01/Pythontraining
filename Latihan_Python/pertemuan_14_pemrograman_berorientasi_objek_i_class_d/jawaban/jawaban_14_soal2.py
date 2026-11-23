# Pertemuan 14 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Buat class RekeningBank dengan method setor(), tarik() (tidak boleh melebihi
#   saldo), dan cek_saldo().
# ------------------------------------------------------------

class RekeningBank:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup")
        else:
            self.saldo -= jumlah

    def cek_saldo(self):
        return self.saldo

r = RekeningBank("Rina", 100000)
r.setor(50000)
r.tarik(200000)
r.tarik(75000)
print(r.cek_saldo())

# Contoh output:
#   Saldo tidak cukup
#   75000
