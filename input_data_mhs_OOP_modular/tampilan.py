class MahasiswaView:
    def input_mahasiswa(self):
        try:
            nama = input("Nama Mahasiswa: ")
            kehadiran = float(input("Nilai Kehadiran (0-100): "))
            tugas = float(input("Nilai Tugas (0-100): "))
            uts = float(input("Nilai UTS (0-100): "))
            uas = float(input("Nilai UAS (0-100): "))

            for nilai in [kehadiran, tugas, uts, uas]:
                if nilai < 0 or nilai > 100:
                    raise ValueError("Semua nilai harus 0 - 100")

            return nama, kehadiran, tugas, uts, uas
        except ValueError as e:
            print("Input tidak valid:", e)
            return None

    def tampilkan_tabel(self, daftar_mahasiswa, rata_rata):
        print("\n===== DATA NILAI MAHASISWA =====")
        print("| No | Nama            | Nilai Akhir |")
        print("-------------------------------------")
        for i, mhs in enumerate(daftar_mahasiswa, start=1):
            print(f"| {i:<2} | {mhs.get_nama():<15} | {mhs.get_nilai_akhir():<11.2f} |")
        print("-------------------------------------")
        print(f"Rata-rata Nilai Akhir: {rata_rata:.2f}")
