# Pertemuan 6
## Tugas Pengantar Pemograman 
Ini adalah code program UAS mata kuliah pengantar pemograman dari ikram ramadhan dengan dosen pengampu bapak Agung Nugroho, S.Kom., M.Kom

````shell
Nama   : Ikram Ramadhan
Nim    : 312110478
Matkul : Pengantar Pemograman
````
## Konsep Object Oriented Programming (OOP)

Object Oriented Programming (OOP) adalah paradigma pemrograman yang berfokus pada penggunaan objek yang merepresentasikan entitas di dunia nyata. Setiap objek memiliki data (atribut) dan perilaku (method).
Dalam program ini menggunakan
1.Class
2.Object
3.Encapsulation
* 
## Konsep Modular Programming

Modular Programming adalah teknik pemrograman dengan cara membagi program besar menjadi beberapa modul atau file terpisah, di mana setiap modul memiliki tanggung jawab tertentu.
Dalam program ini menggunakan 4 data class terpisah;
1. class Mahasiswa
2. class MahasiswaProcess
3. class MahasiswaView
4. class Main
* 

## code,flowchart dan output program pada materi 1
## Class Mahasiswa
````shell
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
````

## Class MahasiswaProcess
````shell
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


````
  ## Class MahasiswaView
  ````shell
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

````

  ## Class Main
  ````shell
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

````