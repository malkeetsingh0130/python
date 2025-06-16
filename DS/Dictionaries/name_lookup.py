#Q: Create a dictionary where keys are names and values are ages. Ask the user for a name and print their age.

#Takin input for the name
name = input("Enter the name you want to search: ")

#Converting it into lowecase so that is runs caseinsensitive
lowercase_name = name.lower()

#Creating a dictionary with set of names
user = { 'chandler':25 , 'rachel':25 , 'ross':27 , 'joey':30 }

#Running a loop to check for name in the user dictionary
if lowercase_name in user:
    age = user [lowercase_name] #If user exists in the Dictionary
    print (f"{name} is: {age}") #Concatenate and print the users age 
else:
    print ('The person does not exist in the Dictionary') #If user does not exist then give out a statement