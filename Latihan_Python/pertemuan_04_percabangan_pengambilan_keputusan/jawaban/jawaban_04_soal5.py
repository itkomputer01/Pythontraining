# Pertemuan 4 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Minta panjang tiga sisi segitiga. Tentukan apakah dapat membentuk segitiga
#   (jumlah dua sisi mana pun harus lebih besar dari sisi ketiga), lalu tentukan
#   jenisnya: sama sisi, sama kaki, atau sembarang.
# ------------------------------------------------------------

a = float(input("Sisi a: "))
b = float(input("Sisi b: "))
c = float(input("Sisi c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Segitiga sama sisi")
    elif a == b or b == c or a == c:
        print("Segitiga sama kaki")
    else:
        print("Segitiga sembarang")
else:
    print("Bukan segitiga")
