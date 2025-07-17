#amount = 1000
#balance = int(input("Enter the amount to withdraw: "))
class NegativeBalanceError(Exception):
    pass
def withdraw(amount, balance):
    if amount  > balance:
        raise NegativeBalanceError("Insufficient funds")
    balance -= amount
    return balance
try:
    balance = withdraw(500,100)
except NegativeBalanceError as e:
    print(f"transcation Failed {e}")