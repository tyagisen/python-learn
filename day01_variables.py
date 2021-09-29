'''Variables are the container where we can store the values we want.
variables can be global variable and local variable. variable that is out side function globally is global variable.
variable that are inside any function. that can be executed inside the same function cannot be accessed to other function
variables inside the function can be made global variable by using global keyword. The examples are below. The triple quote i have used here in python calls docstrings
'''
# this is a variable. As it is in between a-z alphabetes. Also, it is not started with number. Dash should be excluded. they are case sensative.
x = 'Tyagi' #It is a global variable.
def func1():
    y= 'sen' #This is local variable
    print(x)

func1()



