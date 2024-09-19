def compute_discount(price, discount_percentage):
    return price*discount_percentage/100

def main():
    price = float(input("Enter price: "))
    discount_percentage = float(input("Enter discount percentage: "))

    discount_amount = compute_discount(price, discount_percentage)

    print(f"The discount is {discount_amount:.2f} euros")



main()