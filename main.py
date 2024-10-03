print("Welcome to the tip calculator!")

bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) + 100
num_of_people = int(input("How many people to split the bill? "))

total_cost = bill * (tip / 100)

payment = round(total_cost / num_of_people, 2)

print(f"Each person should pay: ${payment}")