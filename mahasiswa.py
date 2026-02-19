"""
===========================================================
KELAS: Mahasiswa
===========================================================

Konsep OOP yang digunakan:

1. INHERITANCE
   - Kelas Mahasiswa mewarisi atribut dan method dari kelas Pengguna.

2. POLYMORPHISM
   - Method tampilkan_profil() dioverride untuk menambahkan
     informasi khusus mahasiswa.

3. ENCAPSULATION
   - Atribut tambahan mahasiswa dibuat protected (_).
   - Akses dilakukan melalui method.

Mahasiswa memiliki hak untuk:
- Mengajukan peminjaman buku
- Mengembalikan buku
- Melihat riwayat peminjaman
- Membayar denda
===========================================================
"""

from pengguna import Pengguna


class Mahasiswa(Pengguna):
    def __init__(self, id_pengguna, nama_lengkap, email, nomor_telepon,
                 alamat, kata_sandi, nim, program_studi,
                 fakultas, angkatan):

        # INHERITANCE: memanggil constructor parent
        super().__init__(id_pengguna, nama_lengkap, email,
                         nomor_telepon, alamat, kata_sandi)

        # ENCAPSULATION: atribut khusus mahasiswa
        self._nim = nim
        self._program_studi = program_studi
        self._fakultas = fakultas
        self._angkatan = angkatan
        self._batas_maksimal_pinjam = 3
        self._daftar_peminjaman_aktif = []
        self._total_denda = 0

    # ==============================
    # METHOD KHUSUS MAHASISWA
    # ==============================

    def ajukan_peminjaman(self, buku):
        print("\n📚 PENGAJUAN PEMINJAMAN")
        print("-" * 40)

        if len(self._daftar_peminjaman_aktif) >= self._batas_maksimal_pinjam:
            print("❌ Gagal: Melebihi batas maksimal peminjaman.")
            return False

        print(f"Mahasiswa : {self._nama_lengkap}")
        print(f"Buku      : {buku.get_judul()}")
        print("Status    : Pengajuan berhasil.")
        return True

    def tambah_peminjaman(self, transaksi):
        self._daftar_peminjaman_aktif.append(transaksi)

    def kembalikan_buku(self, transaksi):
        if transaksi in self._daftar_peminjaman_aktif:
            self._daftar_peminjaman_aktif.remove(transaksi)
            print("✅ Buku berhasil dikembalikan.")
        else:
            print("⚠ Transaksi tidak ditemukan.")

    def tambah_denda(self, jumlah):
        self._total_denda += jumlah

    def bayar_denda(self, jumlah):
        print("\n💰 PEMBAYARAN DENDA")
        print("-" * 40)

        if jumlah >= self._total_denda:
            print("✅ Denda lunas.")
            self._total_denda = 0
        else:
            self._total_denda -= jumlah
            print(f"Sisa denda: Rp {self._total_denda}")

    def lihat_riwayat_peminjaman(self):
        print("\n📖 RIWAYAT PEMINJAMAN AKTIF")
        print("-" * 40)

        if not self._daftar_peminjaman_aktif:
            print("Belum ada peminjaman aktif.")
        else:
            for transaksi in self._daftar_peminjaman_aktif:
                print(f"- {transaksi.get_id_transaksi()}")

    # ==================================
    # POLYMORPHISM (Override Method)
    # ==================================
    def tampilkan_profil(self):
        """
        POLYMORPHISM:
        Method ini mengoverride method dari kelas Pengguna
        dan menambahkan informasi khusus mahasiswa.
        """

        super().tampilkan_profil()  # panggil method parent

        print("\n🎓 DATA AKADEMIK MAHASISWA")
        print("-" * 50)
        print(f"NIM              : {self._nim}")
        print(f"Program Studi    : {self._program_studi}")
        print(f"Fakultas         : {self._fakultas}")
        print(f"Angkatan         : {self._angkatan}")
        print(f"Batas Pinjam     : {self._batas_maksimal_pinjam} Buku")
        print(f"Total Denda      : Rp {self._total_denda}")
        print("=" * 50)