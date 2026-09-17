'''
Function is a set of instructions under a name.
function always ready to perform a job we need to call this
some time during call function also need to accept data so its duty of
caller to pass that data
Note:
The data which we pass to the function is known as argument
The data where it receive that is know as parameter (variable)

in python to define a function the syntax is:
def funcname(param1, param2,...):
    statement1
    statement2
    return value # it is optional
'''
def greet(name="Guest"): # it is a function which does not accept and return
    print(f"Hello {name} Welcome to Function")
    
def table(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")

def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

def aboutme(name="Guest", age=20):
    print(f"Hi my name is {name} and I am {age} year old.")
    
    
