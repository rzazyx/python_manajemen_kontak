#berisi kelas kontak untuk menjalankan project

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()

    def melihat_kontak(self):
        # melihat semua kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
        else:
            print("\nKontak Kosong!")
            return 1

    def menambah_kontak(self):
        # maka ingin menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor HP yang baru: ")
        email = input("Masukkan alamat email yang baru: ")
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kontak()== 1:
            return
        else:
            try:
                i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
                del self.kontak[i_hapus - 1]
                print("Kontak berhasil dihapus")
            except:
                print("Input yang anda masukakan salah")

    def keluar_kontak(self):
        dokumen.menyimpan_kontak(isi=self.kontak)