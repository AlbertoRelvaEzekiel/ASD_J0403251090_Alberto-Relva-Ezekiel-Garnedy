# ==========================================================
# PRAKTIKUM 5
# Nama  : Alberto Relva Ezekiel Garnedy
# NIM   : J0403251090
# Kelas : A1
# ==========================================================

# Latihan 1 - Rekursi Pangkat
def pangkat(a, n):
    if n == 0:
        return 1
    return a * pangkat(a, n - 1)

print("2^4 =", pangkat(2, 4))
