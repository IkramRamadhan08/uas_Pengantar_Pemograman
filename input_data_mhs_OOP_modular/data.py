class Mahasiswa:
    def __init__(self, nama, kehadiran, tugas, uts, uas):
        self.nama = nama
        self.kehadiran = kehadiran
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = 0

    def set_nilai_akhir(self, nilai):
        self.nilai_akhir = nilai

    def get_nama(self):
        return self.nama

    def get_nilai_akhir(self):
        return self.nilai_akhir
