name = input("Enter Employee Name: ").strip().title()

hours_worked = float(input("Enter Hours Worked: "))
hourly_wage = float(input('Enter Hourly Wage: '))

night_shift = float(input('Did You work nightshift? If so, how many shifts this pay period? '))




standard_pay = hours_worked * hourly_wage


overtime_scale = float(hours_worked - 40)

overtime = float(overtime_scale * (hourly_wage * 1.5))

night_pay = ((hourly_wage + 7) * 8)

night_shift_pay = night_pay * night_shift

total_pay_overtime = standard_pay + overtime

total_pay_nightshift = standard_pay + night_shift_pay

total_pay_night_overtime = (standard_pay + night_shift_pay + overtime)

print()
print()

if night_shift >= 1 and hours_worked <=40:
    print(f"Hey {name}, No overtime worked this week.")
    print()
    print(f"Your Check Should be ${standard_pay} and ${night_shift_pay} extra for your differential pay.")
    print()
    print(f"Total paycheck should be ${total_pay_nightshift}.")
    print()
    print(" Good Job! ")

elif hours_worked <= 40:
    print(f'Hey {name}, No overtime worked this week.')
    print(f'Your Check Should be ${standard_pay}.')
    print()
    print('Have a Great Day!')

elif night_shift >=1 and hours_worked > 40:
    print(f'Hey {name}, You are owed ${overtime} in overtime.') 
    print()
    print(f"Please Contact Payroll ASAP.")
    print()
    print(f"As you only got paid ${standard_pay} and ${night_shift_pay} for your night differential.")
    print()
    print(f"Total Paycheck should be ${total_pay_night_overtime}.")
    print()
    print("We apologize for any inconvenience.")

elif hours_worked > 40:
    print(f'Hey {name}, You are owed ${overtime} in overtime.')
    print()
    print(f"Please Contact Payroll ASAP.")
    print()
    print(f"As you only got paid ${standard_pay}")
    print()
    print(f"Total Pay should be ${total_pay_overtime}.")
    print()
    print("We apologize for any inconvenience.")
