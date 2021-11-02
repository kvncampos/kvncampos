#This is a simple tip calculator program.
print("Welcome to the Tip Calculator.")

#This is to prevent user errors. 
while True:
    try:
        total = float(input((f"What was the total tip?\n$")))
        break
    except ValueError:
        print(f"Thats not a number. Try again.\n")

while True:
    try:
        split = int(input(f"Will this bill be divided? If so, by how many?\n"))
        break
    except ValueError:
        print(f"Thats not a number. Try again.\n")

while True:
    try:
        tip = int(input(f"How much would you like to tip? 10%, 15% or 20%\n"))
        break
    except ValueError:
        print(f"Thats not a number. Try again.\n")


# This is to calculate the tip % of the total
tip_amount = total + (total * (tip / 100))
split_amount = tip_amount / split

#Program complete
print(f"The total each person pays is: ${split_amount}")


