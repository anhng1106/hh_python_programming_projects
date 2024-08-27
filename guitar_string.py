import math


num_gigs = int(input("Number of gigs: "))
num_gigs_same_setofString = int(input("Gigs to be played with the same set of strings: "))
guitarString_price = float(input("Price of a set of guitar strings: "))

# solution1
# num_of_guitarString_needed = math.ceil(num_gigs / num_gigs_same_setofString)

# solution2
num_of_guitarString_needed = (num_gigs + num_gigs_same_setofString - 1) // num_gigs_same_setofString # Ensures ceiling behavior

total_cost = guitarString_price * num_of_guitarString_needed

print(f"\nThe guitarist needs {num_of_guitarString_needed} new sets of guitar strings")
print(f"The total cost is {total_cost:.2f} euros")


