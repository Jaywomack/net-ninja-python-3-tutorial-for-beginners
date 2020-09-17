# will loop through and print everything from 0 up to but not including 5
# for n in range(5):
# print(n)

# will loop and print a range started at 2 and up to but not including 10
# for n in range(2, 10):
# print(n)


# with a third parameter it will act as a step
# for n in range(0, 21, 4):
#     print(n)

burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

# for n in range(len(burgers)):
#     print(n, burgers[n])

# The len burgers -1 will make the start at the end of the range and the second number idk the third is the step which will iterate back through the range
for n in range(len(burgers) - 1, -1, -1):
    print(n, burgers[n])
