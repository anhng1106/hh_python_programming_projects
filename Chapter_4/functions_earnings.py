def compute_earnings(hourly_wage, hours):
    if hours <= 40:
        return hours * hourly_wage
    else:
        overtime = hours - 40
        return (40*hourly_wage) + (overtime*(hourly_wage*1.5))

def main():
    hourly_wage = float(input("Enter wage: "))
    hours = int(input("Enter hours: "))

    earning = compute_earnings(hourly_wage, hours)

    print(f"The earnings are {earning:.2f}")

main()

