#input
print("-"*50)
print("PT.XYZ TRAVEL")
print("-"*50)
nama =      input ("Nama calon penumpang            : ")
hp   =      input ("no HP aktif                     : ")
kd_jurusan= input ("pilih kode jurusan [SBY/BL/LMP] : ")
jml_bli= int(input("jumlah beli                      : "))

#proses
if kd_jurusan=="BL" or kd_jurusan=="bl" : 
    kota="BALI"
    harga= 350000
elif kd_jurusan=="SBY" or kd_jurusan=="sby" :
    kota="SURABAYA"
    harga=300000
elif kd_jurusan=="LMP" or kd_jurusan=="lmp" :
    kota="LAMPUNG"
    harga=600000
else:
    kota="salah kode"
    harga=0

#proses menghitung diskon
if jml_bli>=3 : 
    diskon=(harga*0.1)
else: 
    diskon=0

#proses hitung total
total=(harga*jml_bli)-diskon

#output
print("-"*50)
print("penjualan tiket bus")
print("PT.XYZ TRAVEL")
print("-"*50)
print("nama penumpang : ",nama)
print("NO. HP : ",hp)
print("kode jurusan : ",kd_jurusan)
print("kota tujuan :",kota)
print("harga tiket : ",harga)
print("jumalah beli tiket : ",jml_bli)
print("="*50)
print("potongan : ",diskon)
print("total bayar : ",total)
bayar=int(input("masukan uang bayar : "))
kembali=bayar-total
print("Uang kembali : ",kembali)