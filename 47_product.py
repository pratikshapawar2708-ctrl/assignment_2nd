# 47. Product of digits
num = 234
prod = 1
for d in str(num):
    prod *= int(d)
print("Product:", prod)