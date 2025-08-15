stuff = {"food": 15, "energy": 100, "friends": 3}

# get method is used to get the value for any item in the Dictionary
print(stuff.get("food"))

#items method acts on the entire dictionary and list every item
print(stuff.items())

# keys method return the keys and acts on the entire dictionary
print(stuff.keys())

#pop allows to remove last item from the dictionary
print(stuff.popitem())
print(stuff)

#set default method allows us to see what value is in the key
#it also allows us to set a default value if item is not present in the dictionary and adds it


print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("enemies", 123))
print(stuff)

#update method 
new_items={"rocks":4, "arrows":18}
stuff.update(new_items)
print(stuff)

#we can upate items in a dictionary as well
new_items={"rocks":2 , "arrows":5}
stuff.update(new_items)
print(stuff)

#adding and updating items at the same time
up_new={"food":3,"webs":2}
stuff.update(up_new)
print(stuff)

#directly updating the value for food
stuff.update(food = 450)
print(stuff)
