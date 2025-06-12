fname=input("Enter the name of the file: ")
try:
    fhand=open(fname)
except:
    print('File does not exist')
    quit()
file=fhand.read()
uppercasefile=file.upper()
print(uppercasefile)