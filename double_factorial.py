num = int(input("Enter a non-negative integer: "))

# if the input num < 0
if num < 0:
    print("Please enter a non-negative integer")

# if the input num = 0
elif num == 0:
    print("0!! = 1")
    
else:
    result = 1

# if the input num > 0
    for i in range (num, 0, -2):
        result = result*i
    print(f"{num}!! = {result}")

