my_name = 'ryu'


def print_name():
    # overrides the global variable
    global my_name
    my_name = 'Jay'
    print('the name inside the function is', my_name)


print_name()
print('outside the function the name is', my_name)
