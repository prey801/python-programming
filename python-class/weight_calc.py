#user inputs
user_weight = float(input("enter your weight: "))
user_height = float(input("enter your height: "))

#calc BMI using formula
square_height = user_height * user_height

BMI = user_weight / square_height

print(f"your BMI is :",BMI)

#check if person is overweight
if BMI < 18.5:
    print("under weight")
elif BMI >= 18.5 and BMI <= 24.9:
    print(" Normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print("overweight")
elif BMI >= 30:
    print("over weight")
else:
    ("An error occured ")


