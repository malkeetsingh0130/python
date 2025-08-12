#we can use the sort item by it only works for like items ex string or int it cannot sort both
fruits=["orange", "pineapple", "banana", "mango"]
years=[1990, 1998, 2000, 2001, 29.97, 7826]

merged_list= fruits+years
print(merged_list)

#sort method wont work below since list contains both string and int
# merged_list.sort()
# print(merged_list)

#sorting works in ascending order
fruits.sort()
years.sort()
print(fruits, years)

