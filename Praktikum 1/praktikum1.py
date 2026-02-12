# ==========================================================
# Praktikum 1: ADT & File Handling (Studi Kasus: Data Mahasiswa)
#
# Nama  : Alberto Relva Ezekiel Garnedy
# NIM   : J0303251090
# Kelas : 
# ==========================================================

NAMA_FILE = "data_mahasiswa.txt"

def baca_data_mahasiswa(nama_file):
    data_dict = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris == "":
                    continue
                parts = baris.split(",")
                if len(parts) != 3:
                    continue
                nim, nama, nilai_str = parts
                try:
                    nilai_int = int(nilai_str)
                except ValueError:
                    continue
                data_dict[nim] = {
                    "nama": nama,
                    "nilai": nilai_int
                }
    except FileNotFoundError:
        pass
    return data_dict

def tampilkan_semua_mahasiswa(data_dict):
    if len(data_dict) == 0:
        print("Data mahasiswa kosong.")
        return

    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}")
    print("-" * 32)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")

def cari_mahasiswa(data_dict):
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        print("\n=== Data Mahasiswa Ditemukan ===")
        print("NIM   :", nim_cari)
        print("Nama  :", data_dict[nim_cari]["nama"])
        print("Nilai :", data_dict[nim_cari]["nilai"])
    else:
        print("Data tidak ditemukan.")

def update_nilai_mahasiswa(data_dict):
    nim = input("Masukkan NIM yang ingin diupdate nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan.")
        return

    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan.")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan.")
        return

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")

def simpan_data_mahasiswa(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

def main():
    data_mahasiswa = baca_data_mahasiswa(NAMA_FILE)

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua_mahasiswa(data_mahasiswa)
        elif pilihan == "2":
            cari_mahasiswa(data_mahasiswa)
        elif pilihan == "3":
            update_nilai_mahasiswa(data_mahasiswa)
        elif pilihan == "4":
            simpan_data_mahasiswa(NAMA_FILE, data_mahasiswa)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
