"""
===========================================================
KELAS: Buku
===========================================================

Konsep OOP yang digunakan:

1. ENCAPSULATION
   - Semua atribut dibuat protected (_).
   - Perubahan status dan stok hanya bisa melalui method.

2. ABSTRACTION
   - Detail manajemen stok dan status disembunyikan
     dari pengguna luar kelas.

Peran Kelas:
- Menyimpan seluruh informasi detail buku
- Mengatur status ketersediaan
- Mengatur stok
===========================================================
"""

from datetime import datetime


class Buku:
    def __init__(self, id_buku, judul, penulis, isbn,
                 tahun_terbit, penerbit, jumlah_halaman,
                 bahasa, edisi, kategori, rak,
                 kondisi_buku, jumlah_tersedia):

        # ENCAPSULATION
        self._id_buku = id_buku
        self._judul = judul
        self._penulis = penulis
        self._isbn = isbn
        self._tahun_terbit = tahun_terbit
        self._penerbit = penerbit
        self._jumlah_halaman = jumlah_halaman
        self._bahasa = bahasa
        self._edisi = edisi
        self._kategori = kategori
        self._rak = rak
        self._kondisi_buku = kondisi_buku
        self._jumlah_tersedia = jumlah_tersedia
        self._tanggal_input = datetime.now()

    # ==============================
    # GETTER
    # ==============================

    def get_id_buku(self):
        return self._id_buku

    def get_judul(self):
        return self._judul

    def get_kategori(self):
        return self._kategori

    def get_rak(self):
        return self._rak

    def get_stok(self):
        return self._jumlah_tersedia

    # ==============================
    # BEHAVIOR MANAJEMEN STOK
    # ==============================

    def kurangi_stok(self):
        if self._jumlah_tersedia > 0:
            self._jumlah_tersedia -= 1
            return True
        return False

    def tambah_stok(self):
        self._jumlah_tersedia += 1

    def tersedia(self):
        return self._jumlah_tersedia > 0

    def perbarui_kondisi(self, kondisi_baru):
        self._kondisi_buku = kondisi_baru

    # ==============================
    # TAMPILAN DETAIL BUKU
    # ==============================

    def tampilkan_detail(self):
        print("\n" + "-" * 60)
        print(f"📖 DETAIL BUKU [{self._id_buku}]")
        print("-" * 60)
        print(f"Judul            : {self._judul}")
        print(f"Penulis          : {self._penulis}")
        print(f"ISBN             : {self._isbn}")
        print(f"Tahun Terbit     : {self._tahun_terbit}")
        print(f"Penerbit         : {self._penerbit}")
        print(f"Jumlah Halaman   : {self._jumlah_halaman}")
        print(f"Bahasa           : {self._bahasa}")
        print(f"Edisi            : {self._edisi}")
        print(f"Kategori         : {self._kategori}")
        print(f"Lokasi Rak       : {self._rak}")
        print(f"Kondisi Buku     : {self._kondisi_buku}")
        print(f"Stok Tersedia    : {self._jumlah_tersedia}")
        print(f"Tanggal Input    : {self._tanggal_input.strftime('%d-%m-%Y')}")
        print(f"Status           : {'Tersedia' if self.tersedia() else 'Tidak Tersedia'}")
        print("-" * 60)