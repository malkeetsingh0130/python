fhand=open('test_file.txt')
for line in fhand:
    line.rstrip()
    if not line.startswith('Test'): continue
    words=line.split()
    print(words[2])