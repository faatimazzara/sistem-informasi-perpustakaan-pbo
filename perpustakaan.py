"""
===========================================================
KELAS: Perpustakaan
===========================================================

Konsep OOP yang digunakan:

1. ENCAPSULATION
   - Semua atribut dibuat protected (_).
   - Manipulasi data hanya melalui method resmi.

2. ABSTRACTION
   - Detail penyimpanan buku, pengguna, dan transaksi
     disembunyikan dalam kelas ini.

Peran Kelas:
- Pusat pengelolaan sistem perpustakaan.
- Menyimpan seluruh data koleksi dan transaksi.
- Menyediakan laporan ringkas.
===========================================================
"""


class Perpustakaan:
    def __init__(self, nama_perpustakaan, alamat, tahun_berdiri):

        # ENCAPSULATION
        self._nama_perpustakaan = nama_perpustakaan
        self._alamat = alamat
        self._tahun_berdiri = tahun_berdiri

        self._daftar_buku = []
        self._daftar_pengguna = []
        self._daftar_kategori = []
        self._daftar_rak = []
        self._daftar_transaksi = []
        self._total_pendapatan_denda = 0

    # =====================================
    # MANAJEMEN DATA DASAR
    # =====================================

    def tambah_buku(self, buku):
        self._daftar_buku.append(buku)

    def tambah_pengguna(self, pengguna):
        self._daftar_pengguna.append(pengguna)

    def tambah_kategori(self, kategori):
        self._daftar_kategori.append(kategori)

    def tambah_rak(self, rak):
        self._daftar_rak.append(rak)

    def tambah_transaksi(self, transaksi):
        self._daftar_transaksi.append(transaksi)
        self._total_pendapatan_denda += transaksi.get_jumlah_denda()

    # =====================================
    # FITUR PENCARIAN
    # =====================================

    def cari_buku_berdasarkan_judul(self, kata_kunci):
        print("\n🔎 HASIL PENCARIAN BUKU")
        print("-" * 50)

        ditemukan = False
        for buku in self._daftar_buku:
            if kata_kunci.lower() in buku.get_judul().lower():
                print(f"- {buku.get_judul()}")
                ditemukan = True

        if not ditemukan:
            print("Buku tidak ditemukan.")

    # =====================================
    # TAMPILKAN DATA
    # =====================================

    def tampilkan_semua_buku(self):
        print("\n" + "=" * 70)
        print("📚 DAFTAR SELURUH BUKU PERPUSTAKAAN")
        print("=" * 70)

        if not self._daftar_buku:
            print("Belum ada buku terdaftar.")
        else:
            for buku in self._daftar_buku:
                buku.tampilkan_detail()

    def tampilkan_semua_pengguna(self):
        print("\n" + "=" * 70)
        print("👥 DAFTAR PENGGUNA TERDAFTAR")
        print("=" * 70)

        if not self._daftar_pengguna:
            print("Belum ada pengguna terdaftar.")
        else:
            for pengguna in self._daftar_pengguna:
                print(f"- {pengguna.get_nama_lengkap()}")

    # =====================================
    # LAPORAN RINGKAS
    # =====================================

    def tampilkan_laporan_ringkas(self):
        print("\n" + "=" * 70)
        print("📊 LAPORAN RINGKAS PERPUSTAKAAN")
        print("=" * 70)
        print(f"Nama Perpustakaan     : {self._nama_perpustakaan}")
        print(f"Alamat                : {self._alamat}")
        print(f"Tahun Berdiri         : {self._tahun_berdiri}")
        print(f"Total Buku            : {len(self._daftar_buku)}")
        print(f"Total Pengguna        : {len(self._daftar_pengguna)}")
        print(f"Total Transaksi       : {len(self._daftar_transaksi)}")
        print(f"Total Pendapatan Denda: Rp {self._total_pendapatan_denda}")
        print("=" * 70)

    # =====================================
    # HAPUS BUKU
    # =====================================

    def hapus_buku(self, id_buku):
        for buku in self._daftar_buku:
            if buku.get_id_buku() == id_buku:
                self._daftar_buku.remove(buku)
                return True
        return False