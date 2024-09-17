
while True:
    user_input = input("Enter a month number: ")

    try:
        num = int(user_input)
        if num in range(1, 13):
            print("OK")
            break
        else:
            print(f"{user_input} is not a valid month number\n")
    except ValueError:
        print(f"'{user_input}' is not a valid month number\n")
