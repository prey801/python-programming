try:
    num = int(input("Enter a number: "))
    results = 10 / num
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Results:", results)
finally:
    print("closing the program.")