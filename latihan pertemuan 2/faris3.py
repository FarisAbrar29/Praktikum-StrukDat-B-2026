

print()
kelas_A = {"struktur data", "basis data", "ai", "pemrograman web"}
kelas_B = {"struktur data", "machine learning", "ai", "cloud computing"}
print("mata kuliah yang diambil  kedua kelas :")

for x in kelas_A:
    if x in kelas_B:
        print(x)
print()
for x in kelas_A:
    if x not in kelas_B:
        print(x)
print()
mata_kuliah_kedua_kelas = kelas_A.union(kelas_B)
print(mata_kuliah_kedua_kelas)
print()
print("mata kuliah yang hanya diambil oleh kelas A : ")
mata_kuliah_kedua_kelas = kelas_A.difference(kelas_B)
print(mata_kuliah_kedua_kelas)
print()
print("mata kuliah yang unik :")
mata_kuliah_kedua_kelas = kelas_A.symmetric_difference(kelas_B)
print(mata_kuliah_kedua_kelas)