#for opening files we use the open function
file=open('D:/Projects/pyhton-git/python/Files/test_file.txt')
count=0
for line in file:
    count=count+1
print ("line count: ", count)
