fname=input("Enter the name of the file: ")
try:
    fhand=open(fname)
except:
    print("File does not exist")
    quit()
count=0
for line in fhand:
    if line.startswith('Test'):
        count=count+1
print('There were',count,'lines starting with Test')