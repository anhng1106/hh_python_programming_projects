try:
    user_input = input("Enter a weekday number: ")
    num = int(user_input)
    if num in range(1, 8):
        print("OK")
    else:
        print(f"Please enter an integer between 1 and 7")
except ValueError:
    print(f"Please enter an integer between 1 and 7")
