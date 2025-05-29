#taking input for word and letter in the word
#searching for the letter in the word and giving the count
word=input("Enter the word: ")
count=0
letter=input("Enter the letter you want to search: ")
for value in word:
    if value==letter:
        count=count+1
print(count)
