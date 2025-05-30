def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

a=float(input("Enter the 1st number: "))
b=float(input("Enter the 2nd number: "))

action=int(input("Enter the serial numbre for the action you want to perform: \n 1. Add \n 2. Substract \n 3. Multiply \n 4. Divide \n"))

if action==1:
    print(add(a,b))
    
elif action==2:
    print(sub(a,b))
elif action==3:
    print(mult(a,b))
elif action==4:
    print(div(a,b))


