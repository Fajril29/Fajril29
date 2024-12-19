from data_prodi import dapat_nama_prodi

def main():
    print("=== Menentukan Asal Prodi ===")
    
    while True:
        kode_prodi = input("Masukkan Asal Prodi anda : ")
        
        if kode_prodi.lower() == "keluar":
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        
        nama_prodi = dapat_nama_prodi(kode_prodi)
        print(f"Nama Program Studi: {nama_prodi}\n")

if __name__ == "__main__":
    main()
