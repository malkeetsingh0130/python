string=input("Enter a string: ")
#logic for printing string with index
index=0
while index <len(string):
    letter=string[index]
    print(index,letter)
    index=index+1
print(string[2:4]) #prints from index 2 to 4. Letter on index 4 is not printed.
print(string[:])#prints all the letters
print(string[2:])#prints from index 2 to end
print(string[:5])#prints from index 0 to 5