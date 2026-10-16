# 36. Sum until 0 entered
s = 0
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    s += num
print("Sum:", s)