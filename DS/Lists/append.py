fruits=["peaches", "pears", "apples"]
years=[3, "1998", 2.5, 987, "1994"]

print(fruits, years)

#adding 1 item to a list
fruits.append("oranges")
print(fruits)

#we can use extend method to combine lists
fruits.extend(years)
print(fruits)