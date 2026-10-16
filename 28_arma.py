# 28. Armstrong number
num = 153
s = sum(int(d)**3 for d in str(num))
print("Armstrong:", num == s)