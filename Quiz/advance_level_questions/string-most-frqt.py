def CheckMostFrequent():
    string = input("Enter a string: ")
    frequency = {}
    
    for char in string:
        if char.isalpha():  # Consider only alphabetic characters
            frequency[char] = frequency.get(char, 0) + 1
    
    most_frequent_char = max(frequency, key=frequency.get)
    return most_frequent_char


print(CheckMostFrequent())