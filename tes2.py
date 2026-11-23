import tkinter as tk
from tkinter import messagebox


def hitung_jumlah():
    teks1 = entry_angka1.get().strip()
    teks2 = entry_angka2.get().strip()

    try:
        angka1 = float(teks1)
        angka2 = float(teks2)
        hasil = angka1 + angka2

        # Tampilkan sebagai bilangan bulat jika tidak ada pecahan desimal
        if hasil.is_integer():
            hasil = int(hasil)

        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError:
        messagebox.showerror("Input Tidak Valid", "Masukkan angka yang valid pada kedua kolom.")


# Membuat jendela utama
window = tk.Tk()
window.title("Penjumlahan Angka")
window.geometry("320x190")
window.resizable(False, False)

# Form input 1
tk.Label(window, text="Angka 1:").pack(pady=(12, 2))
entry_angka1 = tk.Entry(window, width=25)
entry_angka1.pack()

# Form input 2
tk.Label(window, text="Angka 2:").pack(pady=(8, 2))
entry_angka2 = tk.Entry(window, width=25)
entry_angka2.pack()

# Tombol hitung
tk.Button(window, text="Jumlahkan", command=hitung_jumlah, width=15).pack(pady=12)

# Label hasil
label_hasil = tk.Label(window, text="Hasil: -", font=("Arial", 11, "bold"))
label_hasil.pack()

# Menjalankan loop aplikasi GUI
window.mainloop()