import os
import time
from datetime import datetime
from termcolor import cprint

os.system('cls')

# Fungsi untuk animasi loading
def loading_animation():
    for i in range(1, 4):
        print("Loading" + "." * i, end="\r")
        time.sleep(1)
        print(" " * 10, end="\r")

# Fungsi untuk menampilkan menu utama
def menu_utama():
    print("\n=== Menu Utama ===")
    print("1. Pinjam Buku")
    print("2. Kembalikan Buku")
    print("3. Lihat Daftar Buku")
    print("4. Lihat Daftar Peminjaman")
    print("5. Lihat Daftar Pengembalian")
    print("6. Keluar")

# Fungsi untuk meminjam buku
def pinjam_buku():
    nama = input("Masukkan nama Anda: ")
    judul = input("Masukkan judul buku yang ingin dipinjam: ")
    tanggal_pinjam = input("Masukkan tanggal pinjam (DD-MM-YYYY): ")
    peminjaman.append([nama, judul, tanggal_pinjam])
    print("Buku berhasil dipinjam!")

# Simpan data ke dalam file
def simpan_data():
    with open('peminjaman.txt', 'w') as file:
        for pinjam in peminjaman:
            file.write(f"{pinjam[0]},{pinjam[1]},{pinjam[2]}\n")
    print("Data peminjaman berhasil disimpan.")
    print()

# Fungsi untuk mengembalikan buku
def kembalikan_buku():
    nama = input("Masukkan nama Anda: ")
    judul = input("Masukkan judul buku yang ingin dikembalikan: ")
    tanggal_kembali = input("Masukkan tanggal kembali (DD-MM-YYYY): ")

    with open('pengembalian.txt', 'a') as file:
        file.write(f"{nama},{judul},{tanggal_kembali}\n")

    for pinjam in peminjaman:
        if pinjam[0] == nama and pinjam[1] == judul:
            tanggal_pinjam = datetime.strptime(pinjam[2], "%d-%m-%Y")
            tanggal_kembali_dt = datetime.strptime(tanggal_kembali, "%d-%m-%Y")
            telat = (tanggal_kembali_dt - tanggal_pinjam).days - 7
            denda = 1000 * max(telat, 0)
            cprint(f"Denda keterlambatan: Rp {denda}", "black", "on_red")
            print("Buku berhasil dikembalikan!\n")
            break
    else:
            print("Data peminjaman tidak ditemukan.\n")

# Fungsi untuk melihat daftar buku
def lihat_daftar_buku():
    print("\n=== Daftar Buku ===")
    for buku in daftar_buku:
        print(f"Judul: {buku['Judul']}, Penulis: {buku['Penulis']}")
    print()

# Fungsi untuk melihat daftar peminjaman
def lihat_daftar_peminjaman():
    print("\n=== Daftar Peminjaman ===")
    if os.path.exists('peminjaman.txt'):
        with open('peminjaman.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            print(f"Nama: {data[0]}")
            print(f"Judul Buku: {data[1]}")
            print(f"Tanggal Pinjam: {data[2]}")
            print()
    else:
        print("Belum ada data peminjaman.")
    print()

#Fungsi untuk melihat daftar pengembalian
def lihat_daftar_pengembalian():
    print("\n=== Daftar Pengembalian ===")
    if os.path.exists('pengembalian.txt'):
        with open('pengembalian.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            print(f"Nama: {data[0]}")
            print(f"Judul Buku: {data[1]}")
            print(f"Tanggal Kembali: {data[2]}")
            print()
    else:
        print("Belum ada data pengembalian.")
    print()
        
# Array 2D untuk menyimpan data peminjaman
peminjaman = []

# Dictionary untuk daftar buku
daftar_buku = [
    {"Judul": "Kalkulus 1", "Penulis": "Varberg, Purcell, Rigdon"},
    {"Judul": "Kalkulus 2", "Penulis": "Varberg, Purcell, Rigdon"},
    {"Judul": "Aljabar Linier Elementer", "Penulis": "Anton, Rorres"},
    {"Judul": "Bumi", "Penulis": "Tere Liye"},
    {"Judul": "Pengantar Statistika", "Penulis": "Ronald E. Walpole"}
]

# Loop utama program
while True:
    loading_animation()
    menu_utama()
    pilihan = input("Pilih menu: ")
    if pilihan == '1':
        pinjam_buku()
        simpan_data()
    elif pilihan == '2':
        kembalikan_buku()
    elif pilihan == '3':
        lihat_daftar_buku()
    elif pilihan == '4':
        lihat_daftar_peminjaman()
    elif pilihan == '5':
        lihat_daftar_pengembalian()
    elif pilihan == '6':
        print("Terima kasih telah meminjam buku disini.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
