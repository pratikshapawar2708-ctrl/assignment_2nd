# 22. Sum of even digits
num = 123456
s = 0
for d in str(num):
    if int(d) % 2 == 0:
        s += int(d)
print("Sum even digits:", s)