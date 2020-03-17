# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1 : {}, arg2 : {}".format(arg1, arg2))

# Okay that args is pointless, we can just do this 

def print_two_again(arg1, arg2):
    print("arg1 : {}, arg2 : {}".format(arg1, arg2))

# this just takes one argument

def print_one(arg1):
    print("arg1 : {}".format(arg1))

# this takes nothing

def print_none():
    print("I got nothing")

print_two("Ramu", "Somu")
print_two_again("Manu", "Reni")
print_one("Raj")
print_none()
