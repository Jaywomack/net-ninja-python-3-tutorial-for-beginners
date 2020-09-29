from random import shuffle


def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return "".join(anagram)


words = ['beetroot', 'carrots', 'potatoes']
anagrams = []
# # Using a for loop to do what map does
# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

# map(function,data)

# print(list(map(jumble, words)))

# Using the comprehesion

print([jumble(word) for word in words])
