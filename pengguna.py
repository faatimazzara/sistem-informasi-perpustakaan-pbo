"""
===========================================================
KELAS: Pengguna
===========================================================

Konsep OOP yang digunakan:

1. ABSTRACTION
   - Kelas ini dibuat sebagai kelas dasar (parent class).
   - Tidak ditujukan untuk dibuat objek langsung.
   - Akan diwariskan ke kelas Mahasiswa dan Pustakawan.

2. ENCAPSULATION
   - Atribut dibuat dengan tanda underscore (_) 
     untuk menandakan bahwa atribut tidak boleh diakses langsung.
   - Akses dilakukan melalui method (getter).

3. INHERITANCE
   - Kelas ini akan menjadi superclass bagi Mahasiswa dan Pustakawan.

4. POLYMORPHISM
   - Method tampilkan_profil() dapat dioverride oleh kelas turunan.
===========================================================
"""

from datetime import datetime


class Pengguna:
    def __init__(self, id_pengguna, nama_lengkap, email, nomor_telepon, alamat, kata_sandi):
        # ENCAPSULATION: atribut dibuat "protected"
        self._id_pengguna = id_pengguna
        self._nama_lengkap = nama_lengkap
        self._email = email
        self._nomor_telepon = nomor_telepon
        self._alamat = alamat
        self._kata_sandi = kata_sandi
        self._tanggal_registrasi = datetime.now()
        self._status_aktif = True

    # ==============================
    # METHOD AKSES (GETTER)
    # ==============================
    def get_id_pengguna(self):
        return self._id_pengguna

    def get_nama_lengkap(self):
        return self._nama_lengkap

    def get_email(self):
        return self._email

    def get_status(self):
        return self._status_aktif

    # ==============================
    # BEHAVIOR UMUM
    # ==============================
    def login(self, email, kata_sandi):
        print("\n🔐 PROSES LOGIN")
        print("-" * 40)

        if self._email == email and self._kata_sandi == kata_sandi:
            print(f"✅ Login berhasil. Selamat datang, {self._nama_lengkap}")
            return True
        else:
            print("❌ Login gagal. Email atau kata sandi salah.")
            return False

    def logout(self):
        print(f"👋 {self._nama_lengkap} telah logout dari sistem.")

    def ubah_kata_sandi(self, kata_sandi_baru):
        self._kata_sandi = kata_sandi_baru
        print("🔄 Kata sandi berhasil diperbarui.")

    # ==================================
    # METHOD YANG BISA DIOVERRIDE
    # ==================================
    def tampilkan_profil(self):
        """
        POLYMORPHISM:
        Method ini dapat dioverride oleh kelas turunan
        untuk menampilkan informasi tambahan.
        """

        print("\n" + "=" * 50)
        print("📌 PROFIL PENGGUNA")
        print("=" * 50)
        print(f"ID Pengguna       : {self._id_pengguna}")
        print(f"Nama Lengkap      : {self._nama_lengkap}")
        print(f"Email             : {self._email}")
        print(f"No. Telepon       : {self._nomor_telepon}")
        print(f"Alamat            : {self._alamat}")
        print(f"Tanggal Daftar    : {self._tanggal_registrasi.strftime('%d-%m-%Y')}")
        print(f"Status Akun       : {'Aktif' if self._status_aktif else 'Nonaktif'}")
        print("=" * 50)