num_days = int(input("Enter the number of days of gym visits per year: "))
price_per_day = float(input("Enter price for a day pass: "))
yearly_fee = float(input("Enter yearly membership fee: "))

total_price = num_days*price_per_day

difference = 0;
if yearly_fee > total_price:
    difference = yearly_fee - total_price
    print(f"\nBuying day passes is {difference:.2f} euros cheaper")
elif total_price > yearly_fee:
    difference = total_price - yearly_fee
    print(f"\nPaying the yearly membership fee is {difference:.2f} euros cheaper")
else:
    print(f"\nThere is no price difference")

 

