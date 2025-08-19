# Count the number of vowels in a string.

string = input("Enter the string- ").lower()
vowels = "aeiou"
count = 0
for ch in string:
    if ch in vowels:
        count +=1

print(f"The string contains {count}")
    




