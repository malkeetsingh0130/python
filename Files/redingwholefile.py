#read() function is used to read the contents of the file.
#it is a combination of /n and characters that is being read
#we should not read a big file at once.

file=open('D:/Projects/pyhton-git/python/Files/test_file.txt')
data=file.read() #dont use this with big files as it will store a big string in one variable.
#print(data)
print(len(data))
print(data[:20])