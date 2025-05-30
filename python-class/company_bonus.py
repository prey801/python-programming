user_years = int(input("enter number of years worked: "))
user_salary = int(input("enter your salary: "))


if (user_years < 10):
    bonus = user_salary * 0.1
elif (user_years >= 6):
    bonus = user_salary * 0.06
elif(user_years <= 10):
    bonus = user_salary * 0.05
elif(user_salary < 6):
    bonus  = user_salary * 0.05
else:
    print("yoour not alligable ")

#calculate total
total = user_salary + bonus
print(f"your bonus is {bonus:.2f}")
print(total)