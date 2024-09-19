def print_rectangle(height, width):
    for i in range (height):
        for j in range (width):
            print("*", end="")
        
        print()

def main():
    height = int(input("Enter height: "))
    width = int(input("Enter width: ")) 

    print_rectangle(height, width)

main()