#Program Manajemen Kontak

def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)

class Kontak:
    def __init__(self):
        self.kontak = membuka_kontak()

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
        menyimpan_kontak(isi=self.kontak)

kontak_kantor = Kontak()
kontak_keluarga = Kontak()


while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1, 2, 3 atau 4): ")

    if pilihan == '1':
        kontak_kantor.melihat_kontak()

    elif pilihan =='2':
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        #keluar dari kontak
        kontak_kantor.keluar_kontak()
        break
    else:
        print("Anda salah memasukkan angka")