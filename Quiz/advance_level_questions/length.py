import random

def Myfuction():
    word_list = ["apple", "banana", "cherry", "date", "fig"]
    sorted_list = sorted(word_list, key=len)
    return sorted_list
print(Myfuction())