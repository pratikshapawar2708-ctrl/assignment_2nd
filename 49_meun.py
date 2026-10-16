# 49. Menu-driven program
while True:
    print("1. Add\n2. Subtract\n3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        a, b = map(int, input("Enter two numbers: ").split())
        print("Sum:", a+b)
    elif choice == 2:
        a, b = map(int, input("Enter two numbers: ").split())
        print("Difference:", a-b)
    elif choice == 3:
        break