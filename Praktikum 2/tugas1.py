# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Alberto Relva Ezekiel Garnedy
# NIM   : J0303251090
# Kelas : 
# ==========================================================

NAMA_FILE = "stok_barang.txt"

def baca_stok(nama_file):
    stok_dict = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()
                if baris == "":
                    continue
                parts = baris.split(",")
                if len(parts) != 3:
                    continue
                kode, nama_barang, stok_str = parts
                try:
                    stok_int = int(stok_str)
                except ValueError:
                    continue
                stok_dict[kode] = {
                    "nama": nama_barang,
                    "stok": stok_int
                }
    except FileNotFoundError:
        pass
    return stok_dict

def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in sorted(stok_dict.keys()):
            nama_barang = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama_barang},{stok}\n")

def tampilkan_semua(stok_dict):
    if len(stok_dict) == 0:
        print("Stok barang kosong.")
        return
    print("\n=== DAFTAR STOK BARANG ===")
    print(f"{'Kode':<10} | {'Nama':<15} | {'Stok':>5}")
    print("-" * 36)
    for kode in sorted(stok_dict.keys()):
        nama_barang = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama_barang:<15} | {stok:>5}")

def cari_barang(stok_dict):
    kode = input("Masukkan kode barang: ").strip()
    if kode in stok_dict:
        print("\n=== Barang Ditemukan ===")
        print("Kode :", kode)
        print("Nama :", stok_dict[kode]["nama"])
        print("Stok :", stok_dict[kode]["stok"])
    else:
        print("Barang tidak ditemukan.")

def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return
    nama_barang = input("Masukkan nama barang: ").strip()
    try:
        stok_awal = int(input("Masukkan stok awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka.")
        return
    if stok_awal < 0:
        print("Stok tidak boleh negatif.")
        return
    stok_dict[kode] = {
        "nama": nama_barang,
        "stok": stok_awal
    }
    print("Barang berhasil ditambahkan.")

def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    try:
        jumlah = int(input("Masukkan jumlah: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka.")
        return
    if jumlah < 0:
        print("Jumlah tidak boleh negatif.")
        return
    stok_sekarang = stok_dict[kode]["stok"]
    if pilihan == "1":
        stok_dict[kode]["stok"] = stok_sekarang + jumlah
        print("Stok berhasil ditambahkan.")
    elif pilihan == "2":
        if stok_sekarang - jumlah < 0:
            print("Stok tidak boleh negatif. Update dibatalkan.")
            return
        stok_dict[kode]["stok"] = stok_sekarang - jumlah
        print("Stok berhasil dikurangi.")
    else:
        print("Pilihan tidak valid.")

def main():
    stok_barang = baca_stok(NAMA_FILE)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
