# 23. Sum of odd digits
s = 0
for d in str(num):
    if int(d) % 2 != 0:
        s += int(d)
print("Sum odd digits:", s)