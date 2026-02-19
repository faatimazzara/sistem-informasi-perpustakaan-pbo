"""
===========================================================
KELAS: Rak
===========================================================

Konsep OOP yang digunakan:

1. ENCAPSULATION
   - Atribut dibuat protected (_).
   - Buku tidak bisa langsung dimasukkan dari luar,
     harus melalui method tambah_buku_ke_rak().

2. COMPOSITION (Relasi UML)
   - Rak memiliki daftar buku.
   - Jika rak dihapus, daftar buku di dalamnya ikut terpengaruh.

Peran Kelas:
- Menentukan lokasi fisik buku.
- Mengatur kapasitas maksimal rak.
===========================================================
"""


class Rak:
    def __init__(self, id_rak, kode_rak, lantai,
                 kapasitas_maksimal):

        # ENCAPSULATION
        self._id_rak = id_rak
        self._kode_rak = kode_rak
        self._lantai = lantai
        self._kapasitas_maksimal = kapasitas_maksimal
        self._daftar_buku_di_rak = []

    # ==============================
    # GETTER
    # ==============================

    def get_kode_rak(self):
        return self._kode_rak

    def get_lantai(self):
        return self._lantai

    def get_kapasitas(self):
        return self._kapasitas_maksimal

    # ==============================
    # MANAJEMEN BUKU DI RAK
    # ==============================

    def tambah_buku_ke_rak(self, buku):
        if len(self._daftar_buku_di_rak) >= self._kapasitas_maksimal:
            print("❌ Kapasitas rak penuh.")
            return False

        self._daftar_buku_di_rak.append(buku)
        print(f"✅ Buku '{buku.get_judul()}' ditempatkan di Rak {self._kode_rak}")
        return True

    def tampilkan_informasi_rak(self):
        print("\n" + "=" * 60)
        print(f"📍 INFORMASI RAK {self._kode_rak}")
        print("=" * 60)
        print(f"ID Rak           : {self._id_rak}")
        print(f"Kode Rak         : {self._kode_rak}")
        print(f"Lantai           : {self._lantai}")
        print(f"Kapasitas Maks   : {self._kapasitas_maksimal}")
        print(f"Jumlah Buku      : {len(self._daftar_buku_di_rak)}")
        print("-" * 60)

        if not self._daftar_buku_di_rak:
            print("Belum ada buku di rak ini.")
        else:
            print("Daftar Buku:")
            for buku in self._daftar_buku_di_rak:
                print(f"- {buku.get_judul()}")

        print("=" * 60)

    def cek_kapasitas(self):
        sisa = self._kapasitas_maksimal - len(self._daftar_buku_di_rak)
        return sisa

    # Agar saat diprint langsung tampil ringkas
    def __str__(self):
        return f"{self._kode_rak} (Lantai {self._lantai})"