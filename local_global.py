# local vs global

user="Anil"  # global variable

def sayhello():
    global user
    user="John"  # here user variable is a new variable in local scope  
    print(f"Hello {user}")

sayhello()

print(user) # user variable can not access here because it is local variable of
            # sayhello 
