"""
===========================================================
KELAS: Pustakawan
===========================================================

Konsep OOP yang digunakan:

1. INHERITANCE
   - Pustakawan mewarisi kelas Pengguna.

2. POLYMORPHISM
   - Method tampilkan_profil() dioverride untuk menampilkan
     informasi khusus pustakawan.

3. ENCAPSULATION
   - Atribut dibuat protected (_).
   - Manipulasi data melalui method.

Peran Pustakawan:
- Mendaftarkan buku
- Menghapus buku
- Memvalidasi peminjaman
- Memvalidasi pengembalian
- Membuat laporan
===========================================================
"""

from pengguna import Pengguna


class Pustakawan(Pengguna):
    def __init__(self, id_pengguna, nama_lengkap, email, nomor_telepon,
                 alamat, kata_sandi, nip, jabatan,
                 shift_kerja, tanggal_mulai_bekerja):

        # INHERITANCE
        super().__init__(id_pengguna, nama_lengkap, email,
                         nomor_telepon, alamat, kata_sandi)

        # ENCAPSULATION
        self._nip = nip
        self._jabatan = jabatan
        self._shift_kerja = shift_kerja
        self._tanggal_mulai_bekerja = tanggal_mulai_bekerja

    # ==========================================
    # BEHAVIOR KHUSUS PUSTAKAWAN
    # ==========================================

    def registrasi_buku(self, perpustakaan, buku):
        print("\n📘 REGISTRASI BUKU")
        print("-" * 40)
        perpustakaan.tambah_buku(buku)
        print(f"✅ Buku '{buku.get_judul()}' berhasil ditambahkan.")

    def hapus_buku(self, perpustakaan, id_buku):
        print("\n🗑 PENGHAPUSAN BUKU")
        print("-" * 40)

        berhasil = perpustakaan.hapus_buku(id_buku)
        if berhasil:
            print("✅ Buku berhasil dihapus.")
        else:
            print("❌ Buku tidak ditemukan.")

    def validasi_peminjaman(self, transaksi):
        print("\n✔ VALIDASI PEMINJAMAN")
        print("-" * 40)

        transaksi.proses_peminjaman()
        print("Status: Disetujui oleh pustakawan.")

    def validasi_pengembalian(self, transaksi):
        print("\n✔ VALIDASI PENGEMBALIAN")
        print("-" * 40)

        transaksi.proses_pengembalian()
        print("Status: Pengembalian telah divalidasi.")

    def buat_laporan(self, laporan):
        print("\n📊 GENERATE LAPORAN")
        print("-" * 40)
        laporan.tampilkan_ringkasan()

    # ==================================
    # POLYMORPHISM (Override Method)
    # ==================================
    def tampilkan_profil(self):
        """
        POLYMORPHISM:
        Method ini mengoverride method tampilkan_profil()
        dari kelas Pengguna.
        """

        super().tampilkan_profil()

        print("\n👩‍💼 DATA PUSTAKAWAN")
        print("-" * 50)
        print(f"NIP               : {self._nip}")
        print(f"Jabatan           : {self._jabatan}")
        print(f"Shift Kerja       : {self._shift_kerja}")
        print(f"Tanggal Mulai     : {self._tanggal_mulai_bekerja}")
        print("=" * 50)