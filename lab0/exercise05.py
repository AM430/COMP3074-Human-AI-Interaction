"""5.Create a variable words containing a list of words.  Experiment with words.sort() and
sorted(words) . What is the difference?"""

words = ["banana", "apple", "cherry", "orange", "grape"]
print("Original list:", words)

# Using sort() - modifies the original list
words.sort()
print("After sort():", words)

# Resetting the list
words = ["banana", "apple", "cherry", "orange", "grape"]

# Using sorted() - creates a new sorted list
sorted_words = sorted(words)
print("Original list after sorted():", words)
print("New sorted list:", sorted_words)
