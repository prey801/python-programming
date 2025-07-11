john = 170
alice = 172
Bob = 150

def max_height():
    """Returns the maximum height among John, Alice, and Bob."""
    if john > alice and john > Bob:
        print("John is the tallest.")
    elif alice > john and alice > Bob:
        print("Alice is the tallest.")
    elif Bob > john and Bob > alice:
        print("Bob is the tallest.")
    else:
        print("There is a tie for the tallest height.")
    return max(john, alice, Bob)

max_height_value = max_height()
print(f"The maximum height is: {max_height_value} cm")