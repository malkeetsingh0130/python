def person(name,age,*args,**kwargs):
    print("{} is {} years old and live in {}. They like {}".format(name,age,*args,**kwargs))

person("High","27","Bangalore","Badminton")

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))


application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, hire_date = "September 2010")