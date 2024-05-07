print("---------------------------------------------------------------")
print("---------- Operasi Penjumlahan dan Perkalian Matriks ----------")
print("---------------------------------------------------------------")
n = int(input("Masukkan ukuran baris dan kolom matriks A dan B (n x n) : "))
print("---------------------------------------------------------------")
print("Masukkan Elemen Matriks A :")
A = []
for i in range (1,n+1) :
    baris1 = []
    for j in range (1,n+1) :
        a = int(input(f"Baris ke-{i}, Kolom ke-{j} : "))
        baris1.append(a)
    A.append(baris1)
print("---------------------------------------------------------------")
print("Masukkan Elemen Matriks B :")
B = []
for i in range (1,n+1) :
    baris2 = []
    for j in range (1,n+1) :
        b = int(input(f"Baris ke-{i}, Kolom ke-{j} : "))
        baris2.append(b)
    B.append(baris2)
print("---------------------------------------------------------------")
print("Matriks A = {}".format(A) )
print("Matriks B = {}".format(B))
print("---------------------------------------------------------------")
hasil_kali = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            hasil_kali [i][j] += A[i][k] * B[k][j]
print("Hasil Perkalian Matriks A dan B : ")
print("Matriks C = {}".format(hasil_kali))
transpose_a = []
for i in range(n) :
    baris3 = []
    for j in range(n) :
        c = A[j][i]
        baris3.append(c)
    transpose_a.append(baris3)
transpose_b = []
for i in range(n) :
    baris4 = []
    for j in range(n) :
        d = B[j][i]
        baris4.append(d)
    transpose_b.append(baris4)
hasil_jumlah = []
for i in range(n) :
    baris5 = []
    for j in range(n) :
        e = transpose_a[i][j] + transpose_b[i][j]
        baris5.append(e)
    hasil_jumlah.append(baris5)
print("Hasil Penjumlahan matriks A transpose dan matriks B transpose : ")
print("Matriks D = {}".format(hasil_jumlah))