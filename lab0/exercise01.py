"""Lab 0 Exercise 1: American to British spelling.

Use slicing and concatenation. Start with lowercase color, favor, behavior.
Before writing the function, explore the indices and slices below.
"""

word = "color"
# print(list(enumerate(word)))

new_word = word[:4] + "u" + word[4:]
# print(list(enumerate(new_word)))

print(new_word)

# TODO: Print a slice containing everything before the final r.
print(word[:4])
# TODO: Print a slice containing only the final r.
print(word[4:])
# TODO: Plan how to insert "u" between these two slices.
print(word[:4] + "u" + word[4:])


# TODO: Move your expression into a function and try the other two words.
def convert_to_british_spelling(word):
    return word[:4] + "u" + word[4:]


print(convert_to_british_spelling("favor"))
word = "behavior"
print(list(enumerate(word)))
print(word[:7] + "u" + word[7:])
