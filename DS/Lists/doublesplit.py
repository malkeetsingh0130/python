#we are first going to spit string based on whitespace and then split it based on @
string= 'This is a test email test123@gmail.com do not reply to this'
split1=string.split()
print(split1)
split2=split1[5].split('@')
print(split2)
print(split2[0])