"""
===========================================================
PROGRAM UTAMA: SISTEM INFORMASI PERPUSTAKAAN KAMPUS
===========================================================

File ini berisi simulasi penggunaan sistem:

Alur:
1. Membuat perpustakaan
2. Membuat kategori dan rak
3. Membuat pustakawan
4. Registrasi buku
5. Registrasi mahasiswa
6. Proses peminjaman
7. Simulasi keterlambatan
8. Menampilkan laporan akhir

Seluruh konsep OOP:
✔ Encapsulation
✔ Inheritance
✔ Polymorphism
✔ Abstraction
telah digunakan dalam sistem ini.
===========================================================
"""

from perpustakaan import Perpustakaan
from kategori import Kategori
from rak import Rak
from buku import Buku
from mahasiswa import Mahasiswa
from pustakawan import Pustakawan
from transaksi_peminjaman import TransaksiPeminjaman
from laporan_perpustakaan import LaporanPerpustakaan


def main():

    print("=" * 70)
    print("📚 SISTEM INFORMASI PERPUSTAKAAN KAMPUS")
    print("=" * 70)

    # ======================================================
    # 1️⃣ Membuat Perpustakaan
    # ======================================================
    perpus = Perpustakaan(
        "Perpustakaan Kampus Cerdas",
        "Jl. Pendidikan No. 10",
        2010
    )

    # ======================================================
    # 2️⃣ Membuat Kategori & Rak
    # ======================================================
    kategori_ti = Kategori(1, "Teknologi Informasi", "Buku seputar IT dan komputer")
    kategori_mnj = Kategori(2, "Manajemen", "Buku manajemen dan bisnis")

    rak_a = Rak(1, "A1", 1, 10)
    rak_b = Rak(2, "B1", 2, 10)

    perpus.tambah_kategori(kategori_ti)
    perpus.tambah_kategori(kategori_mnj)
    perpus.tambah_rak(rak_a)
    perpus.tambah_rak(rak_b)

    # ======================================================
    # 3️⃣ Membuat Pustakawan
    # ======================================================
    pustakawan = Pustakawan(
        100,
        "Siti Rahmawati",
        "siti@kampus.ac.id",
        "081234567890",
        "Pekanbaru",
        "admin123",
        "198765",
        "Kepala Perpustakaan",
        "Pagi",
        "01-01-2015"
    )

    perpus.tambah_pengguna(pustakawan)

    # ======================================================
    # 4️⃣ Registrasi Buku
    # ======================================================
    buku1 = Buku(
        101,
        "Pemrograman Berorientasi Objek",
        "Andi Wijaya",
        "978-1234567890",
        2023,
        "Informatika Press",
        350,
        "Indonesia",
        "Edisi 2",
        kategori_ti,
        rak_a,
        "Baik",
        5
    )

    buku2 = Buku(
        102,
        "Manajemen Strategis Modern",
        "Rina Kusuma",
        "978-0987654321",
        2022,
        "Bisnis Media",
        280,
        "Indonesia",
        "Edisi 1",
        kategori_mnj,
        rak_b,
        "Sangat Baik",
        3
    )

    pustakawan.registrasi_buku(perpus, buku1)
    pustakawan.registrasi_buku(perpus, buku2)

    rak_a.tambah_buku_ke_rak(buku1)
    rak_b.tambah_buku_ke_rak(buku2)

    # ======================================================
    # 5️⃣ Registrasi Mahasiswa
    # ======================================================
    mahasiswa = Mahasiswa(
        200,
        "Fatimah Azzahra",
        "fatimah@kampus.ac.id",
        "082233445566",
        "Pekanbaru",
        "mhs123",
        "12550120997",
        "Teknik Informatika",
        "Fakultas Sains dan Teknologi",
        2022
    )

    perpus.tambah_pengguna(mahasiswa)

    # ======================================================
    # 6️⃣ Proses Peminjaman
    # ======================================================
    transaksi = TransaksiPeminjaman(1, mahasiswa, buku1)

    pustakawan.validasi_peminjaman(transaksi)
    perpus.tambah_transaksi(transaksi)

    # ======================================================
    # 7️⃣ Simulasi Pengembalian Terlambat 3 Hari
    # ======================================================
    pustakawan.validasi_pengembalian(transaksi)
    transaksi.proses_pengembalian(simulasi_terlambat_hari=3)

    # ======================================================
    # 8️⃣ Menampilkan Laporan
    # ======================================================
    laporan = LaporanPerpustakaan(perpus)

    laporan.laporan_daftar_buku()
    laporan.laporan_transaksi()
    laporan.laporan_total_denda()
    laporan.tampilkan_ringkasan()


if __name__ == "__main__":
    main()