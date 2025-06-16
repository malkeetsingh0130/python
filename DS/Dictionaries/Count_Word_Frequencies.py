# Q: Given a string, count how many times each word appears.
text = "apple banana apple orange banana apple"

# Split the string into words
words = text.split()

# Create an empty dictionary
word_counts = {}

# Loop through each word
for word in words:
    if word in word_counts:
        word_counts[word] += 1  # Increment count if word exists
    else:
        word_counts[word] = 1   # Initialize count if word is new

# Print the result
print(word_counts)

