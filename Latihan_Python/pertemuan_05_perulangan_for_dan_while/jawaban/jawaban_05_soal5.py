# Pertemuan 5 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Cetak FizzBuzz dari 1 sampai 30: kelipatan 3 diganti Fizz, kelipatan 5
#   diganti Buzz, kelipatan keduanya FizzBuzz.
# ------------------------------------------------------------

for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
