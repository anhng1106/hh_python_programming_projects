car_price = float(input("Enter the car's selling price: "))

if car_price < 50000:
    bonus_price = car_price * 0.01
    
else:
    bonus_price = car_price * 0.015

if bonus_price < 200:
    bonus_price = 200

print(f"The bonus is {bonus_price:.2f} euros.")
