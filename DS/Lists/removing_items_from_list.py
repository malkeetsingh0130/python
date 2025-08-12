#we use remove method to remove items from a list
fruits=["peaches", "oranges", "apples","pineapple"]

fruits.remove("orange") #this will return an error since orange is not in the list
print(fruits)

# we have to be very specific while using remove method

fruits.remove("oranges")

#we can use pop to remove items as well along with the index number
fruits.pop(0)
