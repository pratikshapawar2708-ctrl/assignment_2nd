# 48. Strong number
num = 145
s = sum(math.factorial(int(d)) for d in str(num))
print("Strong:", num == s)