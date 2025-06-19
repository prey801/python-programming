#enter two numbers
def num1():
    num1=int(input("enter your first Number"))
    return num1
def num2():
    num1=int(input("enter your second Number"))
    return num2
num1()
num2()
#enter operation
opp =input("enter - * / ")
#addition
def add():
    result = num1+num2
    return result
#subration
def sub():
    result = num1-num2
    return result
#multiplication
def mult():
    result= num1*num2
    return result
#division
def division():
    result = num1+num2
    return result
#check operation
if opp == "+":
    print("addition is", add())
elif opp == "-":
    print("subtraction is", sub())
elif opp ==("*"):
    print("multiplication is", mult)
elif opp == ("/"):
    print("division is", division())
else:
    print("invalid operation")

