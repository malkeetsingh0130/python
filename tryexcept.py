# number=input("input a number ")
# try:
#     number=int(number)
#     if number>=10:
#         print("Large")
#     else: print("small")

# except:
#     print("Enter a number")

#Write pay computation to give employees 1.5 times the hourly rate 
try:
    Hours=float(input("Enter the number of hours worked: "))
    Rate=float(input ("Enter the Rate per hour: "))
    pay=1.5*(Hours*Rate)
    print(pay)
except:
    print("Please enter numerical values")