#Program Manajemen Kontak

kontak1 = {'nama': "Andi", 'HP': "089620", 'email': "aku@email.com"}
kontak2 = {'nama': "Ani", 'HP': "08962000", 'email': "aku1@email.com"}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1, 2, 3 atau 4): ")

    if pilihan == '1':
        #melihat semua kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("\nKontak Kosong!")

    elif pilihan =='2':
        #maka ingin menambahkan kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor HP yang baru: ")
        email = input("Masukkan alamat email yang baru: ")
        kontak_baru ={'nama':nama, 'HP':HP, 'email':email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")

    elif pilihan == '3':
        #menghapus kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("\nKontak Kosong!")
            continue

        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus-1]
        print("Kontak berhasil dihapus")

    elif pilihan == '4':
        #keluar dari kontak
        break
    else:
        print("Anda salah memasukkan angka")