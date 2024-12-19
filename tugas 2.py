while True:
    print("     GEROBAK FRIED CHIKEN FAJRIEL          ")
    print("-------------------------------------------")
    print("Kode         Jenis potong            Harga ")
    print("-------------------------------------------")
    print(" D             Dada               RP. 8.000")
    print(" p             Paha               Rp. 7.000")
    print(" S             Sayap              Rp. 6.000")
    print("===========================================")

#harga
    harga = {'D' : 8000,'P' : 7000, 'S' : 6000,}
    kode = {'D': "dada", 'P': "paha", 'S': "Sayap"}

    jml= int(input ("Banyak jenis :"))
    pesan= []

    for i in range (jml) :
        print (f"\nJenis ke - {i+1}")
        potongan = input("Jenis Potongan [D/P/S]: ").upper()
        jml_beli = int(input("Jumlah Potongan: "))
        if potongan in harga:
            pesan.append((potongan, jml_beli))
        else:
            print("kode tidak valid")

#struk 
    print("\n FRIED CHIKEN")
    print("==========================================================================================")
    print("No. Jenis Potong  Harga Satuan  Banyak Beli  Jumlah Harga      ")
    print("------------------------------------------------------------------------------------------")

    total_price = 0
    for i, (potongan, jml_beli) in enumerate(pesan, 1):
       price = harga [potongan]
       total = price * jml_beli
       total_price += total
       print(f"{i}. {kode[potongan]:<15} Rp.{price:<12,} {jml_beli:,<11} Rp.{total:,}")

    pajak = total_price * 0.1
    total_harga = total_price + pajak

    print("-------------------------------------------")
    print(f"Jumlah Bayar Rp.{total_price:,}")
    print(f"Pajak 10% Rp.{pajak:,}")
    print(f"TOTAL BAYAR Rp.{total_harga:,}")

    repeat = input("\nIngin Memesan Lagi? (y/n): ").lower()
    if repeat != 'y':
       print("Terima Kasih")
       break
    