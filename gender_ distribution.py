try:
	female_students = int(input("Enter the number of female students: "))
	male_students = int(input("Enter the number of male students: "))
	total_students = female_students + male_students
	percentage_female = (female_students / total_students) * 100
	percentage_male = (male_students / total_students) * 100

	print(f"\nFemale: {percentage_female:.1f} %")
	print(f"Male: {percentage_male:.1f} %")
except ZeroDivisionError:
	percentage_female = 0
	percentage_male = 0
	
	print(f"\nFemale: {percentage_female:.1f} %")
	print(f"Male: {percentage_male:.1f} %")
