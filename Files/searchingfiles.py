file=open("D:\\Projects\\pyhton-git\\python\\Files\\test_file.txt")
for line in file:
    line=line.rstrip() #rstrip removes whitespaces from the right end of the string. If line is removed whitespaces will appear in between the output lines
    if line.startswith('Test'): #startswith checks if a string begins with a specific substring
        print(line)