def tambah(judul, penulis, sutradara, tahun):
    with open("data_film.txt", "a") as file:
        file.write(f"{judul}, {penulis}, {sutradara}, {tahun}\n")
    print("Data film telah ditambahkan.")

def hapus(judul):
    with open("data_film.txt", "r") as file:
        lines = file.readlines()
    with open("data_film.txt", "w") as file:
        for line in lines:
            if line.split(",")[0] != judul:
                file.write(line)
    print("Data film berhasil dihapus.")

def edit(judul, penulis, sutradara, tahun):
    with open("data_film.txt", "r") as file:
        lines = file.readlines()
    with open("data_film.txt", "w") as file:
        for line in lines:
            if line.split(",")[0] == judul:
                file.write(f"{judul}, {penulis}, {sutradara}, {tahun}\n")
            else:
                file.write(line)
    print("Data film berhasil diubah.")

def tampilkan():
    with open("data_film.txt", "r") as file:
        for line in file:
            judul, penulis, sutradara, tahun = line.strip().split(",")
            print(f"Judul        :  {judul}")
            print(f"Penulis      : {penulis}")
            print(f"Penerbit     : {sutradara}")
            print(f"Tahun terbit : {tahun}\n")

while True :
    print("Menu :")
    print("1. Tambah Film")
    print("2. Hapus Film")
    print("3. Edit Film")
    print("4. Tampilkan Semua Film")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5) : ")
    if pilihan == "1":
        judul = input("Masukkan judul film : ")
        penulis = input("Masukkan penulis skenario film : ")
        sutradara = input("Masukkan sutradara film : ")
        tahun = input("Masukkan tahun rilis : ")
        tambah(judul, penulis, sutradara, tahun)
    elif pilihan == "2":
        judul = input("Masukkan judul film yang akan dihapus : ")
        hapus(judul)
    elif pilihan == "3":
        judul = input("Masukkan judul film yang akan diubah : ")
        penulis = input("Masukkan penulis skenario yang baru : ")
        sutradara = input("Masukkan sutradara film yang baru : ")
        tahun = input("Masukkan tahun rilis yang baru : ")
        edit(judul, penulis, sutradara, tahun)
    elif pilihan == "4":
        tampilkan()
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")