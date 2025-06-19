user_age = int(input("Enter your age kindly: "))
east_african = input("ARE you a east-African YES NO: ")
east_african = east_african.lower()

if (east_african == "yes"):
    print("kindly countinue")
else:
    print("sorry you cant vote")
    exit()

user_enter = input("Enter your nationality: ")
nationality = user_enter.lower()
#choose

if user_age > 18 and nationality == "kenya" :
    print("you can vote")
else:
    print("you can't vote")