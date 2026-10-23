def buat_biodata(nama, umur, jurusan):
    print("Nama    :", nama)
    print("Umur    :", umur)
    print("Jurusan :", jurusan)

print("--- Positional argument ---")
buat_biodata("Lidya Amelia Putri", 19, "Sistem Informasi")


print("--- Keyword argument ---")
buat_biodata(jurusan="Sistem Informasi", nama="Lidya Amelia Putri", umur=19)