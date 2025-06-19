user_input = input("Enter a number: ")
number = int(user_input)
divisor = 10
def check_divisible(number, divisor):
    print(not number % divisor, end=' ')
    print(number % divisor == 0, end=' ')

check_divisible(number, divisor)
