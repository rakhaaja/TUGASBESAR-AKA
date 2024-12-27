import timeit

class Latihan:
    def __init__(self, nama, kelompok_otot, repetisi_set, beban):
        self.nama, self.kelompok_otot, self.repetisi_set, self.beban = nama, kelompok_otot, repetisi_set, beban

    def __str__(self):
        return f"{self.nama} ({self.kelompok_otot}) - {self.repetisi_set} repetisi/set, {self.beban} kg"

class ProgramLatihan:
    def __init__(self):
        self.daftar_latihan = []

    def tambah_latihan(self, latihan):
        self.daftar_latihan.append(latihan)

    def hapus_latihan(self, nama):
        self.daftar_latihan = [lat for lat in self.daftar_latihan if lat.nama.lower() != nama.lower()]

    def cari_latihan_rekursif(self, kelompok_otot, index=0, hasil=None):
        if hasil is None: hasil = []
        if index >= len(self.daftar_latihan): return hasil
        if self.daftar_latihan[index].kelompok_otot.lower() == kelompok_otot.lower():
            hasil.append(self.daftar_latihan[index])
        return self.cari_latihan_rekursif(kelompok_otot, index + 1, hasil)

    def evaluasi_iteratif(self, kategori=None):
        latihan_filter = self.daftar_latihan if not kategori else [lat for lat in self.daftar_latihan if lat.kelompok_otot.lower() == kategori.lower()]
        total_repetisi = sum(lat.repetisi_set for lat in latihan_filter)
        total_beban = sum(lat.beban for lat in latihan_filter)
        if not latihan_filter: print(f"Tidak ada latihan untuk kelompok otot '{kategori}'."); return
        print(f"Total Repetisi: {total_repetisi}, Total Beban: {total_beban} kg")
        [print(f"- {lat}") for lat in latihan_filter]

    def evaluasi_rekursif(self, daftar=None, index=0, total_repetisi=0, total_beban=0):
        if daftar is None: daftar = self.daftar_latihan
        if index >= len(daftar):
            print(f"Total Repetisi: {total_repetisi}, Total Beban: {total_beban} kg")
            return
        total_repetisi += daftar[index].repetisi_set
        total_beban += daftar[index].beban
        self.evaluasi_rekursif(daftar, index + 1, total_repetisi, total_beban)

    def jalankan(self):
        while True:
            print("\n=== Program Manajemen Latihan ===\n1. Tambah Latihan\n2. Hapus Latihan\n3. Cari berdasarkan Kelompok Otot\n4. Evaluasi Performa\n5. Keluar")
            pilihan = input("Pilih menu (1-5): ")
            if pilihan == "1":
                self.tambah_latihan(Latihan(input("Nama latihan: "), input("Kelompok otot: "), int(input("Repetisi/set: ")), float(input("Beban (kg): "))))
                print("Latihan berhasil ditambahkan.")
            elif pilihan == "2":
                self.hapus_latihan(input("Nama latihan yang dihapus: "))
                print("Latihan berhasil dihapus (jika ditemukan).")
            elif pilihan == "3":
                kelompok_otot = input("Kelompok otot yang dicari: ")
                waktu_rekursif = timeit.timeit(lambda: self.cari_latihan_rekursif(kelompok_otot), number=1)
                waktu_iteratif = timeit.timeit(lambda: [lat for lat in self.daftar_latihan if lat.kelompok_otot.lower() == kelompok_otot.lower()], number=1)
                hasil = self.cari_latihan_rekursif(kelompok_otot)
                print(f"\nHasil pencarian untuk kelompok otot '{kelompok_otot}':")
                [print(f"- {lat}") for lat in hasil] if hasil else print("Tidak ditemukan latihan yang sesuai.")
                print(f"Waktu Rekursif: {waktu_rekursif:.6f} detik, Waktu Iteratif: {waktu_iteratif:.6f} detik")
            elif pilihan == "4":
                kategori = input("Kelompok otot yang dievaluasi (kosongkan untuk semua): ").strip()
                waktu_iteratif = timeit.timeit(lambda: self.evaluasi_iteratif(kategori if kategori else None), number=1)
                waktu_rekursif = timeit.timeit(lambda: self.evaluasi_rekursif(), number=1)
                self.evaluasi_iteratif(kategori if kategori else None)
                print(f"Waktu Iteratif: {waktu_iteratif:.6f} detik, Waktu Rekursif: {waktu_rekursif:.6f} detik")
            elif pilihan == "5":
                print("Program selesai. Sampai jumpa!"); break
            else:
                print("Pilihan tidak valid. Silakan masukkan angka 1-5.")

if __name__ == "__main__":
    ProgramLatihan().jalankan()
