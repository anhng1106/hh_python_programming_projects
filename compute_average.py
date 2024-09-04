first_num = float(input("Enter first number: "))

current_num = first_num
count = 0
sum = 0

if first_num == 0:
    print("Nothing to be calculated")
else:
    while current_num != 0:
        count += 1
        sum += current_num
        next_num = float(input("Enter next number: "))

        current_num = next_num
        
    average = sum / count
    print(f"The average is {average:.2f}")

    