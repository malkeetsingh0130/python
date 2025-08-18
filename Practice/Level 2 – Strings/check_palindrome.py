# Check if a given word is a palindrome (same forward and backward).

string=input("Enter a string: ")

cleaned = string.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Its a Palindrome")

else:
    print("Its not a Palindrome")