print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?\n$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
no_of_people = int(input("How many people to split the bill?\n"))

bill_per_person = (total_bill * (tip_percentage/100 + 1)) / no_of_people
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
