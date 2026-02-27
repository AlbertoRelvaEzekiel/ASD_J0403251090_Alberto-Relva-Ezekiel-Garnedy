# ==========================================================
# PRAKTIKUM 5
# Nama  : Alberto Relva Ezekiel Garnedy
# NIM   : J0403251090
# Kelas : A1
# ==========================================================

# Materi 4 - Backtracking Kombinasi Biner
def biner(n, hasil=""):
    if len(hasil) == n:  # Base Case
        print(hasil)
        return
    biner(n, hasil + "0")
    biner(n, hasil + "1")

biner(3)
