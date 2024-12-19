nama_prodi = {
    "TI": "Teknik Informatika",
    "SI": "Sistem Informasi",
    "EL": "Teknik Elektro",
    "MT": "Teknik Mesin",
    "AR": "Arsitektur",
    "AK": "Akuntansi",
    "MN": "Manajemen",
}

def dapat_nama_prodi(kode_prodi):
    return nama_prodi.get(kode_prodi.upper(), "Prodi tidak ditemukan")
