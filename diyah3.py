count = 0
for i in range (1,81):
    if count < 8:
        if i % 4 == 1:
            print(i, i+1, i+2, "DOR", end=' ')
            count += 4
    else:
        print()
        count = 0