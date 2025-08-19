# Take a full name from the user and print the initials.

string = input("Enter your full name: ")

split1=string.split()

initials= "".join([p[0].upper() for p in split1])

print(initials)