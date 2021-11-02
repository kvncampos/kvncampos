name = input("Enter Employee Name: ").strip().title()
while True:
    try:
        hours_worked = float(input("Enter Hours Worked This week: "))
        hourly_wage = float(input('Enter Hourly Wage: '))
        night_shift = float(input('Did You work nightshift? If so, how many shifts this pay period? '))

    except ValueError:
        print("Thats not a Numero Muchacho, Try again. \n")
        continue
    break


standard_pay = hours_worked * hourly_wage

overtime_scale = float(hours_worked - 40)

overtime = float(overtime_scale * (hourly_wage * 1.5))

night_pay = ((hourly_wage + 5) * 12)

night_shift_pay = night_pay * night_shift

total_pay_overtime = standard_pay + overtime

total_pay_nightshift = night_shift + night_shift_pay

total_pay_night_overtime = (standard_pay + night_shift_pay + overtime)


print()

if night_shift >= 1 and hours_worked <=40:
    print(f"Hey {name}, No overtime worked this week.\n Your Check Should be ${standard_pay:,} and ${night_shift_pay:,} extra for your differential pay.\n Total paycheck should be ${total_pay_nightshift:,}.\n Good Job! ")

elif hours_worked <= 40:
    print(f'Hey {name}, No overtime worked this week.\n Your Check Should be ${standard_pay:,}.\n Have a Great Day!')

elif night_shift >=1 and hours_worked > 40:
    print(f'Hey {name}, You are owed ${overtime:,} in overtime.\n Please Contact Payroll ASAP.\n')
    
    print(f"As you only got paid ${standard_pay:,} and ${night_shift_pay:,} for your night differential.\n Total Paycheck should be ${total_pay_night_overtime:,}.\n We Apologize for any inconvenience.")

elif hours_worked > 40:
    print(f'Hey {name}, You are owed ${overtime:,} in overtime.\n Please Contact Payroll ASAP.\n As you only got paid ${standard_pay:,}\n Total Pay should be ${total_pay_overtime:,}.\n We apologize for any inconvenience.')

    