def input_data(n):
    data = []
    for i in range(1,n+1):
        nilai = int(input(f"Masukkan data ke-{i}: "))
        data.append(nilai)
    return data

def hitung_mean(data):
    total = 0
    for nilai in data:
        total += nilai
    mean = total / len(data)
    return mean

def hitung_modus(data):
    freq = {}
    for nilai in data:
        if nilai in freq:
            freq[nilai] += 1
        else:
            freq[nilai] = 1
    modus = max(freq, key = freq.get)
    return modus

def hitung_variance(data, mean):
    variance = 0
    for x in data :
        variance += (x - mean) ** 2
    variance = round(variance/len(data),3)
    return variance 

def output(mean, modus, variance):
    print(f"{'| Mean':<10} | {mean:<10} |")
    print(f"{'| Modus':<10} | {modus:<10} |")
    print(f"{'| Variance':<10} | {variance:<10} |")

def main():
    n = int(input("Masukkan jumlah data: "))
    data = input_data(n)
    mean = hitung_mean(data)
    modus = hitung_modus(data)
    variance = hitung_variance(data, mean)
    output(mean, modus, variance)

if __name__ == "__main__" :
    main()