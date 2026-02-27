# ==========================================================
# PRAKTIKUM 5
# Nama  : Alberto Relva Ezekiel Garnedy
# NIM   : J0403251090
# Kelas : A1
# ==========================================================

# Latihan 3 - Cari Nilai Maksimum
def cari_maks(data, index=0):
    if index == len(data) - 1:
        return data[index]
    maks_sisa = cari_maks(data, index + 1)
    return data[index] if data[index] > maks_sisa else maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))
