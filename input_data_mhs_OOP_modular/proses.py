class MahasiswaProcess:
    def hitung_nilai_akhir(self, mhs):
        nilai = (
            (mhs.kehadiran * 0.1) +
            (mhs.tugas * 0.2) +
            (mhs.uts * 0.3) +
            (mhs.uas * 0.4)
        )
        return nilai

    def hitung_rata_rata(self, daftar_mahasiswa):
        if len(daftar_mahasiswa) == 0:
            return 0
        total = 0
        for mhs in daftar_mahasiswa:
            total += mhs.get_nilai_akhir()
        return total / len(daftar_mahasiswa)
