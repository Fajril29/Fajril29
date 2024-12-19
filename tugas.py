#layar pemasukan 
print(" PROGRAM HITUNG GAJI KARYAWAN")
print(" PT. FAJRIEL NIM: 19242025   ")
nama=           input(" nama karyawan                : ")
golongan=   int(input(" golongan jabatan [1/2/3]     : "))
pendidikan=     input(" pendidikan [SMA/D1/D3/S1]    : " )
jam=        int(input(" jumlah jam kerja             : "))

#Tunjangan jabatan
gaji= 300000
if golongan==   1:
    tunjangan_jabtan = gaji*0.05
elif golongan== 2: 
    tunjangan_jabatan = gaji*0.1
elif golongan== 3:
    tunjangan_jabatan = gaji*0.15
else:
     tunjangan = 0

#tunjangan pendidikan 
if pendidikan == "SMA" or pendidikan== "sma" :
    tunjangan_pend= gaji*0.25
elif pendidikan == "D1" or pendidikan== "d1" :
      tunjangan_pend= gaji*0.05
elif pendidikan == "D3" or pendidikan== "d3" :
    tunjangan_pend = gaji*0.20
elif pendidikan == "S1" or pendidikan== "s1" :
      tunjangan_pend = gaji*0.3
else:
     tunjangan = 0

#honor lembur
jam_kerja_normal = 8
lembur = 3500 

if jam>= jam_kerja_normal:
    jam_lembur = jam - jam_kerja_normal
    tarif_lembur = jam_lembur * lembur
else:
     tarif_lembur = 0

#jumlah hasil akhir
Total_gaji = tunjangan_jabatan + tunjangan_pend + tarif_lembur

#outpuT
print ("======================================================")
print ("                  DATA GAJI KARYAWAN                  ")
print("")
print("Karyawan Atas Nama     : " + str(nama))
print("honor yang di terima   : ")
print(f"gaji pokok            : Rp. {gaji:,}")
print(f"Tunjangan jabatan     : Rp. {tunjangan_jabatan:,}" )
print(f"Tunjangan Pendidikan  : Rp. {tunjangan_pend}" )
print(f"Honor Lembur          : Rp. {lembur:,}")
print("                         _______________+ ")
print(f"Total Gaji             : Rp. {Total_gaji:,}")
print("--------------------------------------------------------")