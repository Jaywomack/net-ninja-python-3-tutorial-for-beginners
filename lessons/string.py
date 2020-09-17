greet = 'hello'
greet[0]
print(greet[0])

# slice
print(greet[0:3])  # the third position is not included
print(greet[-1:2])

str2 = 'dudes'
print(f"{greet + str2}")

print(greet*3)

cheeses = "brie,cheddar,stilton"
cheeses_array = cheeses.split(',')
print(cheeses_array)
