# ==========================================================
# PRAKTIKUM 5
# Nama  : Alberto Relva Ezekiel Garnedy
# NIM   : J0403251090
# Kelas : A1
# ==========================================================

# Materi 1 - Faktorial Rekursif
def faktorial(n):
    if n == 0:  # Base Case
        return 1
    return n * faktorial(n - 1)  # Recursive Case

print("Faktorial 5 =", faktorial(5))
