# ==========================================================
# PRAKTIKUM 5
# Nama  : Alberto Relva Ezekiel Garnedy
# NIM   : J0403251090
# Kelas : A1
# ==========================================================

# Materi 2 - Tracing Rekursi
def hitung(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    hitung(n - 1)
    print("Keluar:", n)

hitung(3)
