# =======================================================#
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS) 
# Latihan 1: Membuat Fungsi Menampilkan Data
#========================================================#

nama_file = "data_mahasiswa.txt"
data_dict={}

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = ("Nama:", nama, "NIM:", nim, "Nilai:", int(nilai)) #masukkan dalam 
    return data_dict

buka_data = baca_data(nama_file)
print("Jumlah data terbaca", len(buka_data))

# =======================================================#
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS) 
# Latihan 2: Membuat Fungsi Menampilkan Data
#========================================================#

def tampilkan_data(data_dict):
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM'  : <10} | {'NAMA'    : <12} | {'NILAI': <5}")
    '''
    Untuk tamplan yang rapih, atur lebar kolom
    {'NIM'  : <10} artinya nim rata kiri dengan
    ''' 
    print("-"*35) 
    #Menampilkan isi data
    for nim in sorted (data_dict.keys()):
        nama  = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama: <12} | {int(nilai): <5}")

tampilkan_data(buka_data)

# =======================================================#
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS) 
# Latihan 3: Membuat Fungsi Cari Data   
#========================================================#

#Membuat fungi pencarian data

def cari_data(data_dict) :
    #pencarian berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari 
    nim_cari=input("Masukka nim mahasiswa yang akan dicari : ").strip()
    if nim_cari in data_dict : 
        nama=data_dict[nim_cari]["nama"]
        nilai=data_dict[nim_cari]["nilai"]
        print("==== Data Mahasiswa Ditemukan ====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar.")
    
cari_data(buka_data)

# =======================================================#
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS) 
# Latihan 4: Membuat Fungsi Update Data
#========================================================#

#membuat fungasi update data 
def ubah_data(data_dict) : 
    #awali dulu dengan mencari nim mahasiswa yang diupdate 
    nim =input("Masukkan nim mahasiswa yang ingin diubah datanya : ").strip()

    if nim not in data_dict :
        print("NIM tidak ditemukan. Update dibatalkan.")
        return
    
    try :
        nilai_baru= int(input("Masukkan nilai baru 1-100").strip())
    except ValueError :
        print("Nilai harus berupa angka. Update dibatalkan")
    
    if nilai_baru <0 or nilai_baru >100 :
        print("Nilai harus di antara 0 sampai 100. Update dibatalkan.")

    nilai_lama = data_dict[nim]["nilai"]
    nilai_baru=input("Masukkan nilai baru 1-100 : ").strip()
    data_dict[nim]["nilai"] = nilai_baru
    print(f"Update berhasil. nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")


# =======================================================#
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS) 
# Latihan 5: Membuat Fungsi Simpan Data
#========================================================#

def simpan_data(nama_file, data_dict) :
    with open(nama_file, "r", encoding="utf-8") as file:
        for nim in sorted (data_dict.keys()) :
            nama  = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}")

simpan_data(nama_file, data_dict)

def main():
    buka_data = baca_data(nama_file)

    while True:
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM") 
        print("3. Ubah Nilai Mahasiswa") 
        print("4. Simpan Data ke File")
        print("0. Keluar")
        pilihan = input("Pilih Menu: ").strip()

        if pilihan := "1" :
            baca_data(nama_file)

        elif pilihan := "2" :
            tampilkan_data(data_dict)

        elif pilihan := "3" :
            cari_data(data_dict)
        
        elif pilihan := "4" :
            simpan_data(nama_file, data_dict)

        elif pilihan := "0" :
            print("Progran selesai.")
            break


