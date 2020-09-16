# def greet():
# print("Hello World")

# def greet(name='Jay', time='Morning'):
#     print(f"Good {time} {name} hope you are well")


# name = input('enter your name:')
# time = input('enter the time of day:')


# greet()
# function that accepts an input of radius and returns the area of a circle
def area(radius):
    return 3.142 * radius**2

# function that takes to parameters to calc the volume of a cylinder


def vol(area, length):
    print(area * length)


# gets users input for radius and length
radius = int(input("enter a radius "))
length = int(input('enter a length: '))

# calls the vol function with the area function as a one of the parameters that will have the users input as a parameter. the second parameter is the length input
vol(area(radius), length)
