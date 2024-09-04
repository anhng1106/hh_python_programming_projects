num = int(input("Enter an integer: "))

if num > 0:
    total_sum = 0
    for i in range (num, 0, -1):
        print(i, end=" ")
        total_sum += i
    print(f"\nThe sum is {total_sum}")
else:
    print("\nNothing to be printed")