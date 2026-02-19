"""
===========================================================
KELAS: TransaksiPeminjaman
===========================================================

Konsep OOP yang digunakan:

1. ENCAPSULATION
   - Atribut transaksi tidak dapat diubah langsung dari luar.
   - Perhitungan denda dilakukan melalui method internal.

2. ASSOCIATION (Relasi UML)
   - Transaksi berasosiasi dengan Mahasiswa dan Buku.

3. ABSTRACTION
   - Detail perhitungan keterlambatan disembunyikan
     dalam method hitung_keterlambatan().

Peran Kelas:
- Mengelola proses peminjaman dan pengembalian buku.
- Menghitung jumlah hari keterlambatan.
- Menghitung total denda.
===========================================================
"""

from datetime import datetime, timedelta


class TransaksiPeminjaman:
    TARIF_DENDA_PER_HARI = 2000  # bisa diubah sesuai kebijakan

    def __init__(self, id_transaksi, mahasiswa, buku):

        # ENCAPSULATION
        self._id_transaksi = id_transaksi
        self._mahasiswa = mahasiswa
        self._buku = buku

        self._tanggal_peminjaman = datetime.now()
        self._tanggal_jatuh_tempo = self._tanggal_peminjaman + timedelta(days=7)

        self._tanggal_pengembalian = None
        self._jumlah_hari_terlambat = 0
        self._jumlah_denda = 0
        self._status_transaksi = "Diproses"

    # ==============================
    # GETTER
    # ==============================

    def get_id_transaksi(self):
        return self._id_transaksi

    def get_jumlah_denda(self):
        return self._jumlah_denda

    # ==============================
    # PROSES PEMINJAMAN
    # ==============================

    def proses_peminjaman(self):
        print("\n" + "=" * 60)
        print("📚 PROSES PEMINJAMAN BUKU")
        print("=" * 60)

        if not self._buku.tersedia():
            print("❌ Buku tidak tersedia.")
            self._status_transaksi = "Gagal"
            return False

        self._buku.kurangi_stok()
        self._mahasiswa.tambah_peminjaman(self)

        print(f"Mahasiswa        : {self._mahasiswa.get_nama_lengkap()}")
        print(f"Buku             : {self._buku.get_judul()}")
        print(f"Tanggal Pinjam   : {self._tanggal_peminjaman.strftime('%d-%m-%Y')}")
        print(f"Jatuh Tempo      : {self._tanggal_jatuh_tempo.strftime('%d-%m-%Y')}")
        print("Status           : Berhasil Dipinjam")
        print("=" * 60)

        self._status_transaksi = "Dipinjam"
        return True

    # ==============================
    # PROSES PENGEMBALIAN
    # ==============================

    def proses_pengembalian(self, simulasi_terlambat_hari=0):
        print("\n" + "=" * 60)
        print("📦 PROSES PENGEMBALIAN BUKU")
        print("=" * 60)

        self._tanggal_pengembalian = self._tanggal_jatuh_tempo + timedelta(days=simulasi_terlambat_hari)

        self._buku.tambah_stok()
        self._mahasiswa.kembalikan_buku(self)

        self.hitung_keterlambatan()

        print(f"Tanggal Kembali  : {self._tanggal_pengembalian.strftime('%d-%m-%Y')}")
        print(f"Hari Terlambat   : {self._jumlah_hari_terlambat}")
        print(f"Total Denda      : Rp {self._jumlah_denda}")
        print("=" * 60)

        self._status_transaksi = "Selesai"

    # ==============================
    # PERHITUNGAN DENDA
    # ==============================

    def hitung_keterlambatan(self):
        if self._tanggal_pengembalian > self._tanggal_jatuh_tempo:
            selisih = self._tanggal_pengembalian - self._tanggal_jatuh_tempo
            self._jumlah_hari_terlambat = selisih.days
            self._jumlah_denda = self._jumlah_hari_terlambat * self.TARIF_DENDA_PER_HARI
            self._mahasiswa.tambah_denda(self._jumlah_denda)
        else:
            self._jumlah_hari_terlambat = 0
            self._jumlah_denda = 0

    # ==============================
    # TAMPILKAN DETAIL TRANSAKSI
    # ==============================

    def tampilkan_detail_transaksi(self):
        print("\n" + "-" * 60)
        print(f"🧾 DETAIL TRANSAKSI [{self._id_transaksi}]")
        print("-" * 60)
        print(f"Mahasiswa        : {self._mahasiswa.get_nama_lengkap()}")
        print(f"Buku             : {self._buku.get_judul()}")
        print(f"Status           : {self._status_transaksi}")
        print(f"Denda            : Rp {self._jumlah_denda}")
        print("-" * 60)