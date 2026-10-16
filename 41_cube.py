# 41. Perfect cubes (1–100)
for i in range(1, 101):
    if round(i**(1/3))**3 == i:
        print(i, end=" ")