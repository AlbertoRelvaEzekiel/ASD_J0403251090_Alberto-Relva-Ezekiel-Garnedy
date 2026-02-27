# ==========================================================
# PRAKTIKUM 5
# Nama  : Alberto Relva Ezekiel Garnedy
# NIM   : J0403251090
# Kelas : A1
# ==========================================================

# Latihan 2 - Countdown Rekursif
def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)
