str = "hello there dudes"
str_list = str.split(',')
fib1 = [1, 1, 1, 2, 3, 5, 8, 13]
print(fib1)

print(fib1[0])
print(fib1[-1])

print(fib1[0:4])

fib2 = [21, 34, 55]
new_fib = fib1 + fib2
print(new_fib)

fib1[0] = 9
fib1[0] = 1

new_fib.append(89)
new_fib.pop()
new_fib.append(89)
new_fib.append(89)
new_fib.remove(89)
del(new_fib[0])
print(new_fib)

chars = ['mario', 'luigi', 'bowser']
print(chars)
chars.append(5)

print(chars)

nums = [chars, new_fib, [1, 2, 3, 4]]
print(nums)

print(nums[2][1])
