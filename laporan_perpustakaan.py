"""
===========================================================
KELAS: LaporanPerpustakaan
===========================================================

Konsep OOP yang digunakan:

1. ABSTRACTION
   - Proses pembuatan laporan dipisahkan dari kelas Perpustakaan.
   - Perpustakaan hanya menyimpan data, bukan mencetak laporan detail.

2. SINGLE RESPONSIBILITY PRINCIPLE
   - Kelas ini hanya bertanggung jawab membuat laporan.

3. ASSOCIATION
   - Berasosiasi dengan objek Perpustakaan.

Peran Kelas:
- Menampilkan laporan buku
- Menampilkan laporan transaksi
- Menampilkan laporan total denda
===========================================================
"""


class LaporanPerpustakaan:
    def __init__(self, perpustakaan):
        self._perpustakaan = perpustakaan

    # ==========================================
    # LAPORAN DAFTAR BUKU
    # ==========================================
    def laporan_daftar_buku(self):
        print("\n" + "=" * 70)
        print("📚 LAPORAN DAFTAR BUKU")
        print("=" * 70)

        if not self._perpustakaan._daftar_buku:
            print("Belum ada buku terdaftar.")
        else:
            for buku in self._perpustakaan._daftar_buku:
                print(f"- {buku.get_judul()} | Stok: {buku.get_stok()}")

        print("=" * 70)

    # ==========================================
    # LAPORAN TRANSAKSI
    # ==========================================
    def laporan_transaksi(self):
        print("\n" + "=" * 70)
        print("🧾 LAPORAN TRANSAKSI")
        print("=" * 70)

        if not self._perpustakaan._daftar_transaksi:
            print("Belum ada transaksi.")
        else:
            for transaksi in self._perpustakaan._daftar_transaksi:
                transaksi.tampilkan_detail_transaksi()

        print("=" * 70)

    # ==========================================
    # LAPORAN TOTAL DENDA
    # ==========================================
    def laporan_total_denda(self):
        print("\n" + "=" * 70)
        print("💰 LAPORAN TOTAL DENDA")
        print("=" * 70)
        print(f"Total Pendapatan Denda : Rp {self._perpustakaan._total_pendapatan_denda}")
        print("=" * 70)

    # ==========================================
    # RINGKASAN SISTEM
    # ==========================================
    def tampilkan_ringkasan(self):
        print("\n" + "=" * 70)
        print("📊 RINGKASAN SISTEM PERPUSTAKAAN")
        print("=" * 70)
        print(f"Total Buku        : {len(self._perpustakaan._daftar_buku)}")
        print(f"Total Pengguna    : {len(self._perpustakaan._daftar_pengguna)}")
        print(f"Total Transaksi   : {len(self._perpustakaan._daftar_transaksi)}")
        print(f"Total Pendapatan  : Rp {self._perpustakaan._total_pendapatan_denda}")
        print("=" * 70)