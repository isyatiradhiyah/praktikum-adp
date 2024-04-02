#LAMPIRAN BARANG DENGAN HARGA 
print("========| DAFTAR BELANJA |========")
print("----------------------------------")
print("| A: GAMIS         : Rp350.000,- |")
print("| B: KEMEJA        : Rp180.000,- |")
print("| C: ROK CARGO     : Rp150.000,- |")
print("| D: CELANA CARGO  : Rp120.000,- |")
print("| E: JILBAB PETAK  : Rp70.000,-  |")
print("| F: PASHMINA      : Rp80.000,-  |")
print("----------------------------------")
print("==========================================================================")
print("| GAMIS diskon 30""%" " untuk setiap pembelian 3 atau lebih dari 3 pcs" "        |")
print("| Diskon 20""%" " untuk total belanja Rp800.000,- atau lebih dari Rp800.000,-" " |")
print("==========================================================================")

# Daftar barang dengan harga per pcs dan promo diskon
daftar_barang = {
    "A": {"nama": "GAMIS", "harga": 350000, "promo": {"jumlah_minimal": 3, "diskon": 0.3}},
    "B": {"nama": "KEMEJA", "harga": 180000, "promo": None},
    "C": {"nama": "ROK CARGO", "harga": 150000, "promo": None},
    "D": {"nama": "CELANA CARGO", "harga": 120000, "promo": None},
    "E": {"nama": "JILBAB PETAK", "harga": 70000, "promo": None},
    "F": {"nama": "PASHMINA", "harga": 80000, "promo": None}
}

# Fungsi untuk menghitung total harga belanjaan
def hitung_total_belanja(daftar_belanja):
    total = 0
    total_diskon = 0
    for kode_barang, jumlah in daftar_belanja.items():
        harga = daftar_barang[kode_barang]['harga']
        promo = daftar_barang[kode_barang]['promo']
        if promo and jumlah >= (promo['jumlah_minimal']):
            diskon = harga * jumlah * promo['diskon']
            total_diskon += diskon
            total += (harga * jumlah) - diskon
        else:
            total += harga * jumlah
    return total, total_diskon

# Inisialisasi variabel total belanja dan diskon akhir
total_belanja = 0
diskon_akhir = 0

# Input jenis barang dan jumlah barang yang dibeli
daftar_belanja = {}
while True:
    kode_barang = input("Masukkan kode barang (A/B/C/D/E/F/selesai) : ").upper()
    if kode_barang.lower() == "selesai":
        break
    elif kode_barang not in daftar_barang:
        print("Kode barang tidak valid, silahkan masukkan kode barang kembali!")
        continue
    jumlah_barang = int(input(f"Masukkan jumlah {daftar_barang[kode_barang]['nama']} : "))
    if jumlah_barang <= 0:
        print("Jumlah barang tidak boleh kurang dari 0, silahkan masukkan jumlah barang kembali!")
        continue
    if kode_barang in daftar_belanja:
        daftar_belanja[kode_barang] += jumlah_barang
    else:
        daftar_belanja[kode_barang] = jumlah_barang

# Hitung total harga belanjaan
total_belanja, total_diskon = hitung_total_belanja(daftar_belanja)

# Berikan diskon potongan harga untuk total belanja
if total_belanja >= 800000:
    diskon_akhir = 0.2 * total_belanja

# Hitung total harga setelah diskon
total_setelah_diskon = total_belanja - diskon_akhir

# Output Struk Belanja
print("----------------------------------------")
print("===========| STRUK BELANJA |============")
for kode_barang, jumlah in daftar_belanja.items():
    print(f"{daftar_barang[kode_barang]['nama']} ({jumlah} pcs) : Rp{daftar_barang[kode_barang]['harga']*jumlah}")
if total_diskon > 0:
    print(f"Total Diskon GAMIS : ", total_diskon)
print("========================================")
print(f"Total Belanja            : Rp{total_belanja}")
if diskon_akhir > 0:
    print(f"Total Diskon             : Rp{diskon_akhir}")
print(f"Total yang harus dibayar : Rp{total_setelah_diskon}")
print("========================================")
print("| TERIMA KASIH KARENA TELAH BERBELANJA |")
print("--------SAMPAI JUMPA KEMBALI !!!--------")
