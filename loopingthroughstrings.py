fruit=input("Enter the fruit you want to index: ")
index=0
while index<len(fruit):
    #variable index is being used as an iterator whole value is increasing with every loop.
    #[] brackets are used for indexing.are used in Python to access elements of sequences like lists and strings.
    letter=fruit[index] 
    print(index,letter)
    index=index+1
#this can be done more elegantly using a for loop
#the less code you write the better it is
for alphabet in fruit:
    print(alphabet)