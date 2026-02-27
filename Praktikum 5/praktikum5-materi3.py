# ==========================================================
# PRAKTIKUM 5
# Nama  : Alberto Relva Ezekiel Garnedy
# NIM   : J0403251090
# Kelas : A1
# ==========================================================

# Materi 3 - Rekursi pada List
def jumlah_list(data, index=0):
    if index == len(data):  # Base Case
        return 0
    return data[index] + jumlah_list(data, index + 1)

print("Total:", jumlah_list([2, 4, 6, 8]))
