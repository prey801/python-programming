num = int(input("enter first number in the range: "))
num2 = int(input("enter second number in the range: "))
def prime_range(num, num2):

    primes = []
    
    for n in range(num, num2 + 1):
        if n > 1:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    break
            else:
                primes.append(n)
    
    return primes
print(prime_range(num, num2))
