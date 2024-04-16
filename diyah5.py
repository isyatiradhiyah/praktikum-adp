# Buat array nilai x dari -10 sampai 10
nilai_x = list(range(-10, 11))

# Buat array f(x) berdasarkan nilai x
nilai_f = []
for x in nilai_x:
    if x > 0:
        nilai_f.append(x**2 + 2*x)
    elif x < 0:
        nilai_f.append(round(1 / x, 3))
    else:
        nilai_f.append(10)

# Tampilkan output dalam format tabel
print("|   x   |   f(x)  |")
print("|-------|---------|")
for i in range(len(nilai_x)):
    print(f"| {nilai_x[i] : 5} | {nilai_f[i] : 7} |")
