num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
results = num1 / num2
def divide_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print(f"An error occurred: {e}")
        return None
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
    finally:
        print("Execution completed.")
#try:
    #print(f"Results: {results}")
#except ValueError:
    #print("Invalid input! Please enter a valid integer.")
#except ZeroDivisionError:
    #print("Cannot divide by zero!")
#else:
    #print("Division successful.", results)
#finally:
    #print("Closing the program.")
