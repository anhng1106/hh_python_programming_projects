user_input = input("Enter a month number: ")

while True:
    try:
        num = int(user_input)
        if num in range(1, 13):
            print("OK")
            break
        else:
            print(f"{user_input} is not a valid month number")

        user_input = input("\nEnter a month number: ")
    except ValueError:
        print(f"'{user_input}' is not a valid month number")
