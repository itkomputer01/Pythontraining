# Pertemuan 10 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Dengan dictionary comprehension, buat dictionary yang memetakan setiap kata
#   pada ["python", "java", "go"] ke panjang katanya.
# ------------------------------------------------------------

kata = ["python", "java", "go"]
print({k: len(k) for k in kata})

# Contoh output:
#   {'python': 6, 'java': 4, 'go': 2}
