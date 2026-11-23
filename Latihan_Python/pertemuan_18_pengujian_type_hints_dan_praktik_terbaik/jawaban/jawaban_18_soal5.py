# Pertemuan 18 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Buat program kali.py dengan argparse yang menerima dua bilangan bulat a dan
#   b serta opsi --kuadrat untuk mencetak hasil kali dikuadratkan.
# ------------------------------------------------------------

# kali.py
import argparse

parser = argparse.ArgumentParser(description="Mengalikan dua bilangan")
parser.add_argument("a", type=int)
parser.add_argument("b", type=int)
parser.add_argument("--kuadrat", action="store_true", help="kuadratkan hasil")
args = parser.parse_args()

hasil = args.a * args.b
if args.kuadrat:
    hasil **= 2
print(hasil)

# Contoh output:
#   $ python kali.py 3 4 --kuadrat
#   144
