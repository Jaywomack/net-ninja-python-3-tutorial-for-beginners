# ninja_belts = {"crystal": "red", "ryu": "black"}

# print(ninja_belts)

# print(ninja_belts['crystal'])

# # check to see if a value is in the dictionary
# print('yoshi' in ninja_belts)

# # returns the dictionaries keys
# ninja_belts.keys()

# # print ninja belt values and type cast it as a list
# print(list(ninja_belts.values()))

# vals = list(ninja_belts.values())
# print(vals)

# print(vals.count('red'))
# print(vals.count('black'))

# ninja_belts['yoshi'] = 'red'

# print(ninja_belts)

# person = dict(name="Jay", age=27, height="6ft")

# print(person)

# def a function that takes a dictionary as an argument and iterates through the dictionary returning a formatted string with the key value pairs in it
def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f"I am {key} and I am a {val} belt.")


# sets ninja belts to an empty dictionary
ninja_belts = {}
# while loop that is always true and takes input from the user to enter a name and their belt color
while True:
    ninja_name = input('Enter a ninja name:')
    ninja_belt = input('Enter a belt color:')
    # buy putting ninja name in that sets it as the key and the ninja belt as the value
    ninja_belts[ninja_name] = ninja_belt
    # takes user input and either continues the loop or breaks out of it
    another = input('Add another? (y/n)')
    if another == 'y':
        continue
    else:
        break
# prints the dictionary
print(ninja_belts)

# function that returns an f-string and accepts a dictionary as its argument.
ninja_intro(ninja_belts)
