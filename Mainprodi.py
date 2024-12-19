import mdprodi
prodi=input("Masukkan Kode Prodi Anda :")

prodi=prodi [0:2]
kampus= mdprodi.kampus(prodi)
print("Asal prodi : ",kampus)