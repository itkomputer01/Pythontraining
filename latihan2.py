from datetime import datetime
##sdasd

def main():
    nama = input("Masukkan nama Anda: ").strip()
    tahun_lahir_teks = input("Masukkan tahun lahir (contoh: 1998): ").strip()

    try:
        tahun_lahir = int(tahun_lahir_teks)
        tahun_sekarang = datetime.now().year

        if tahun_lahir > tahun_sekarang or tahun_lahir < 1900:
            print("Tahun lahir tidak valid.")
            return

        usia = tahun_sekarang - tahun_lahir
        print(f"Halo, {nama}! Tahun ini usia Anda sekitar {usia} tahun.")
    except ValueError:
        print("Input tahun lahir harus berupa angka.")


if __name__ == "__main__":
    main()