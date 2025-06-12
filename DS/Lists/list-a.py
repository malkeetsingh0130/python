for i in ['John', 'Doe', 'Ruby', 'Rails']:
    print(i)

#lists can be sliced
t=[9,14,20,21,30,40]    
print(t[1:5])

#appending a list
value=list()
while True:
    inp=input('Enter a value: ')
    if inp== 'done' : break
    value.append(inp)
print(value)
    