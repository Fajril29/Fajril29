kode_baju = input("masukan kode baju [SP/AD] : ")
ukuran = input("masukan ukuran baju [S/M] : ")

if kode_baju == "SP" or kode_baju == "sp" :
    merk="superdry"
    if ukuran=="s" or ukuran=="s" :
        harga = 45000
    elif ukuran=="M" or ukuran=="m" :
        harga = 50000  
    else:
        harga= 0 
elif kode_baju == "AD" or kode_baju == "ad" : 
    merk = "adidas"
    if ukuran== "s" or ukuran=="s":
        harga = 65000
    elif ukuran=="m" or ukuran=="m":
        harga = 70000
    else:
        harga = 0

else: 
    merk = "anda salah input kode merk"
    harga = 0

print("-----------------")
print("merk baju : "+str(merk))
print("harga baju : Rp.",harga)


