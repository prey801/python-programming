def CheckAnagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)
print(CheckAnagrams("listen", "silent"))  # Should return True
print(CheckAnagrams("hello", "world"))    # Should return False