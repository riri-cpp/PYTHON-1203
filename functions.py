# positional arguments
# positions matter! 1:1 with function

def happy_birthday(name):
    print(f"Happy Birthday {name}")

happy_birthday("John") # "John" is the argument to the parameter 'name' in happy_birthday function

# John will act as 'name'
# Output: Happy Birthday John

# -------------------------------------------------- #

# default arguments
# constant arguments, less arguments to type

def net_price(list_price, discount=0, tax=0.05): # discount and tax will ALWAYS be set to 0 and 0.05
    print(list_price * (1 - discount) * (1 + tax))

net_price(500) # no need to pass arguments for 'discount' and 'tax' since they are already defined

# 500 will act as 'list_price'
# Output: 525.0

# -------------------------------------------------- #

# keyword arguments
# helps with readability

def greeting(greeting, title, first, last):
    print(f"{greeting} {title}. {first} {last}")

greeting("Hello", title="Mr", first="Spongebob", last="Squarepants") # parameters are easily identified to their arguments

# "Hello" will act as 'greeting'
# Output: Hello Mr. Spongebob Squarepants

# -------------------------------------------------- #

# args and kwargs

# *args (arguments)
# you can pass ANY NUMBER of non keyword arguments

def full_name(*args):
    for arg in args: # the converted tuple is iterated
        print(arg, end=" ")

full_name("Mr.", "Rheman", "Esmael", "Pasia") # arguments are converted into a TUPLE

# Output: Mr. Rheman Esmael Pasia

# **kwargs
# you can pass ANY NUMBER of keyword arguments

print()
def address(**kwargs):
    for key, value in kwargs.items(): # the converted dictionary is iterated
        print(f"{key}: {value}")

address(Street="None", No="068", City="Batangas", Municipality="Ibaan", Barangay="Palindan") # arguments are converted into a DICTIONARY

'''
    Output:
    
    Street: None
    No: 068
    City: Batangas
    Municipality: Ibaan
    Barangay: Palindan
'''

# -------------------------------------------------- #
print()
def shipping_label(*args, **kwargs):
    print("Shipping to: ")
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

shipping_label("Mr.", "Rheman", "Esmael", "Pasia",
               City = "Batangas",
               Municipality = "Ibaan",
               Barangay = "Palindan",
               HouseNum = "068")