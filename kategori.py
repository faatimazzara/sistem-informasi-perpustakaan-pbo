"""
===========================================================
KELAS: Kategori
===========================================================

Konsep OOP yang digunakan:

1. ENCAPSULATION
   - Atribut dibuat protected (_).
   - Tidak diakses langsung dari luar kelas.

2. ABSTRACTION
   - Detail kategori disederhanakan menjadi satu entitas
     yang dapat digunakan oleh kelas Buku.

Peran Kelas:
- Mengelompokkan buku berdasarkan bidang/topik.
- Membantu pencarian dan pelaporan.
===========================================================
"""


class Kategori:
    def __init__(self, id_kategori, nama_kategori, deskripsi_kategori):
        # ENCAPSULATION
        self._id_kategori = id_kategori
        self._nama_kategori = nama_kategori
        self._deskripsi_kategori = deskripsi_kategori

    # ==============================
    # GETTER
    # ==============================

    def get_id_kategori(self):
        return self._id_kategori

    def get_nama_kategori(self):
        return self._nama_kategori

    # ==============================
    # TAMPILKAN INFORMASI KATEGORI
    # ==============================

    def tampilkan_kategori(self):
        print("\n" + "=" * 50)
        print("📂 INFORMASI KATEGORI")
        print("=" * 50)
        print(f"ID Kategori   : {self._id_kategori}")
        print(f"Nama Kategori : {self._nama_kategori}")
        print(f"Deskripsi     : {self._deskripsi_kategori}")
        print("=" * 50)

    # Agar saat diprint otomatis tampil nama kategori
    def __str__(self):
        return self._nama_kategori