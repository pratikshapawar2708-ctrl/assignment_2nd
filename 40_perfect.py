# 40. Perfect squares (1–100)
for i in range(1, 101):
    if int(i**0.5)**2 == i:
        print(i, end=" ")