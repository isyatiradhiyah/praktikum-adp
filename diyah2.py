print("BERIKUT PAKET YANG TERSEDIA")
print("---------------------------")

#jenis paket makanan
A = 25000
print("Paket A :", A)
B = 30000
print("Paket B :", B)
C = 45000
print("Paket C :", C)

print("---------------")

#harga ongkir
P = 0 #kurang dari 500 m
Q = 10000 #500 m - 1.5 km
R = 20000 #lebih dari 1.5 km

paket = input("Paket yang akan dipesan (A/B/C) : ").upper()
jarak = float(input("Jarak rumah anda ke restoran (masukkan angkanya saja dalam meter): "))

if(paket == "A" and 0 <= jarak < 500) :
    total_biaya = A + P
    print("Total biaya yang harus dibayar adalah Rp", total_biaya)
elif(paket == "A" and 500 <= jarak <= 1500) :
    total_biaya = A + Q
    print("Total biaya yang harus dibayar adalah Rp", total_biaya)
elif(paket == "A" and jarak > 1500) :
    total_biaya = A + R
    print("Total biaya yang harus dibayar adalah Rp", total_biaya)
elif(paket == "B" and 0 <= jarak < 500) :
    total_biaya = B + P
    print("Total biaya yang harus dibayar adalah Rp", total_biaya)
elif(paket == "B" and 500 <= jarak <= 1500) :
    total_biaya = B + Q
    print("Total biaya yang harus dibayar adalah Rp", total_biaya)
elif(paket == "B" and jarak > 1500) :
    total_biaya = B + R
    print("Total biaya yang harus dibayar adalah Rp", total_biaya)
elif(paket == "C" and 0 <= jarak < 500) :
    total_biaya = C + P
    print("Total biaya yang harus dibayar adalah Rp", total_biaya)
elif(paket == "C" and 500 <= jarak <= 1500) :
    total_biaya = C + Q
    print("Total biaya yang harus dibayar adalah Rp", total_biaya)
elif(paket == "C" and jarak > 1500) :
    total_biaya = C + R
    print("Total biaya yang harus dibayar adalah Rp", total_biaya)
else :
    print("Paket tidak diketahui")