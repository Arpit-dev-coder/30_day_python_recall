

#  ------------> higher order function <---------------------

# function as parameter

def addition(nums):
    return sum(nums)
def higher_order_function(f , lst):
    print(lst)
    summation=f(lst)
    return summation
print(higher_order_function(addition,[i for i in range(1,6)]))
print(higher_order_function(addition,[1,2,3,4,5]))
print(higher_order_function(addition,list(map(int,input("give input for lst ").split()))))
# working:
# 1.input():takes a space separate string like "1 2 3 4 5"
# 2.split():turn into a list of string["1","2","3","4","5"]
# 3.map(int,...): convert ech item to integer
# 4.list(): make list

# function return value

sqr=lambda n: n**2
cubr=lambda n: n**3
absolute=lambda n: n if n>=0 else -(n)

def higer_order_function(type):
    if type=="square":
        return sqr
    elif type=="cube":
        return cubr
    else:
        return absolute
    
result=higer_order_function("square")
print(result(2))
result=higer_order_function("cube")
print(result(2))
result=higer_order_function("absolute")
print(result(-2))

# python closure : it allow a nested function to access the outer scope of enclosing function inpython closure is created by nesting
#                  a function inside another encapsulating function and then returning the inner function

def add_ten():
    ten=10
    def add(num):
        return num+ten
    return add
closure_result=add_ten()
print(closure_result(5))
print(closure_result(10))


# python decorators :it allows a user to add new functionality to an existing object without modifying  its structure. it usually called
#                    before the defination of a function you want

#       creating decorator

def greeting():
    return "welcome to python"
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
g=uppercase_decorator(greeting)
print(g())

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return "welcome to python"
print(greeting())

def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thanks fo using this function")
    return mfx

@greet
def hello():
    print("hello world")
def add(a,b):
    print(a+b)
hello()
add(3,4)

#or

def hello():
    print("hello world")
def add(a,b):
    print(a+b)
greet(hello)()

@greet
def add(a,b):
    print(a+b)
add(1,2)
#or
def add(a,b):
    print(a+b)
greet(add)(1,2)


# multipule decorator to a single function

# first decorator
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
# second decortor
def split_string_decorator(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
@split_string_decorator
@uppercase_decorator
def greeting():
    return "welcome python"
print(greeting())

# accepting parameter in decorator function

def decorator_with_parameter(function):
    def wrapper_accepting_parameter(para1,para2,para3):
        function(para1,para2,para3)
        print(f"i live in {para3}")
    return wrapper_accepting_parameter
    
@decorator_with_parameter
def print_full_name(first_name,last_name,city):
    print(f"i am {first_name} {last_name}. i love to learn")

print_full_name("arpit","mishra","balasore")

#--------------------> BUILT IN HIGHER ORDER FUNCTION <----------------------

# map() :it take a function and iterable as parameters

# syntax
# map(function,iterable)

number=[i for i in range(1,5)]# iterable
sqr=lambda x: x**2
num_squared=map(sqr,number)
print(list(num_squared))

num_str=["1","2","3","4","5"] # iterable
num_int=map(int,num_str) # int means int()
print(list(num_int))

#cube of list element
cube=lambda x:x*x*x

l=[1,2,4,6,4,3]
newl=[]
for i in l:
    newl.append(cube(i))
print(newl)

# or use map for shortcut
# map use for applay function of every element of list
cube=lambda x:x*x*x
l=[1,2,4,6,4,3]
newl=list(map(cube,l))#map(function_name,list_variable)
#or
newl=list(map(lambda x:x*x*x,l))
print(newl)

# filter(function,iterable): it return boolean for each item of specified iterable(list),it filter the item that satisfy filtering criteria

l=[1,2,4,6,4,3]
def filter_function(a):
   return a>2
newnewl=list(filter(filter_function,l))
print(newnewl)

l=[1,2,4,6,4,3]
even=lambda x: True if x%2==0 else False
even_num=filter(even,l)
print(list(even_num))

name_lst=["ratikanta","bhakti","divya","bhaba","binay"]
name=lambda n: True if len(n)>5 else False
long_name=filter(name,name_lst)
print(list(long_name))


# reduce(function,iterable): it is defined in the functiontool module and weshould import it from this module,it does not return
#                            another iterable,instead it returns a single value


from functools import reduce
num_str=["1","2","3","4","5"]
add=lambda x,y: int(x)+int(y)
total=reduce(add,num_str)
print(total)

from functools import reduce
numbers=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)
