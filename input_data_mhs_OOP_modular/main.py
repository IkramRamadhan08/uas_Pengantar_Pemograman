from data import Mahasiswa
from proses import MahasiswaProcess
from tampilan import MahasiswaView

def main():
    view = MahasiswaView()
    process = MahasiswaProcess()
    daftar_mahasiswa = []

    while True:
        data = view.input_mahasiswa()
        if data is not None:
            nama, kh, tugas, uts, uas = data
            mhs = Mahasiswa(nama, kh, tugas, uts, uas)

            nilai_akhir = process.hitung_nilai_akhir(mhs)
            mhs.set_nilai_akhir(nilai_akhir)

            daftar_mahasiswa.append(mhs)

        lanjut = input("Tambah data? (y/n): ").lower()
        if lanjut != 'y':
            break

    rata_rata = process.hitung_rata_rata(daftar_mahasiswa)
    view.tampilkan_tabel(daftar_mahasiswa, rata_rata)

if __name__ == "__main__":
    main()
