
# -----------------> LIST <-------------------

# list as similar to array but they are different by some cases
# ---> it holds the mix data type
# ---> python has separate ARRAY MODULE.if we want arrays of fix type element for perfor mance reason

# (1) using array module (for fixed type arrays)

    # import arrays
    # a=array.array('typecode',[element])    if typecode is missing it throws TypeError: array() argument 1 must be a unicode character, not list
    # print(a)

    # type code supports: b,B,u,h,H,i,I,l,L,q,Q,f,d ,instead of these if we write anything it throws error


import array
a=array.array("i",[1,2,3,4]) # 'i' stands for integer type
print(a)

# (2) using a list (most common way in python)

a=[1,2,3,4]
print(a)

# basic concept of list

empty_list=list()                                        # this is an empty list,no item inside the list
print(len(empty_list))                                   # no item so length is 0

# list the element

fruit=["banana","orange","lemon","mango"]
vegetables=['potato',"tomato","onion","carrot"]
web_tech=["html","css","js","java"]

# print listed element

print("fruit s are :",fruit)
print("vagetables are : ",vegetables)
print("subjects are : ",web_tech)

# accessing list element by index

fruit=["banana","orange","lemon","mango"]
first_fruit=fruit[0]
print(first_fruit)
second_fruit=fruit[1]
print(second_fruit)

last_fruit=fruit[-1]
print(last_fruit)
second_last_fruit=fruit[-2]
print(second_last_fruit)

# last index

last_index=len(fruit)-1
last_fruit=fruit[last_index]

# slicing list item

fruit=["banana","orange","lemon","mango"]

all_fruit=fruit[0:4]
print(all_fruit)
# or
all_fruit=fruit[0:]
print(all_fruit)

orange_mango=fruit[1:3]
print(orange_mango)

first_fruit=fruit[-4]
print(first_fruit)

orange_mango=fruit[-3:-1]
print(orange_mango)

print(fruit[-3:])


# modification of list

fruit=["banana","orange","lemon","mango"]
fruit[0]="apple"
print(fruit)
fruit[1]="dragon fruit"
print(fruit[1])
print(fruit)

# check item in list or not

fruit=["banana","orange","lemon","mango"]
does_exist="banana" in fruit
print(does_exist)
does_exist="lime" in fruit
print(does_exist)

# methods

# (1) append():

fruit=["banana","orange","lemon","mango"]
fruit.append("apple")
print(fruit)                                  # apple

print(fruit.append("lime"))                   # none

# here variabe.append("string"/any data type) -> it's work is ,it only add something to list and return none,in order to print list
#                                                  we have to print that variable like print(something)
# but here print(variable.append()) -> it only add the item to list,and return none,so printing statement is none,but when we print
#                                      fruit individually it add the item to list
print(fruit)

# (2) remove():

fruit=["banana","orange","lemon","mango"]
fruit.remove("banana")
print(fruit)
fruit.remove("lemon")
print(fruit)

# (3) insert()
 
fruit=["banana","orange","lemon","mango"]
fruit.insert(2,"apple")
print(fruit)
fruit.insert(5,"lime")
print(fruit)
# vaiable.insert(array_position,element)

# (4) pop()

fruit=["banana","orange","lemon","mango"]
fruit.pop()
print(fruit)                             # ['banana', 'orange', 'lemon'] , it pop 1 element from right, if no argument are passed
fruit.pop(0)
print(fruit)                             # ['orange', 'lemon']


# (5) del()


fruit=["banana","orange","lemon","mango"]
del fruit[0]
print(fruit)
del fruit[1]
print(fruit)

# del fruit
# print(fruit)
# NameError: name 'fruit' is not defined


# (6) clear()

fruit=["banana","orange","lemon","mango"]
fruit.clear()
print(fruit)

# (7) copying list

fruit=["banana","orange","lemon","mango"]
fruit_copy=fruit.copy()
print(fruit_copy)

# (8) join(+)

positive_number=[1,2,3,4,5]
zero=[0]
negetive_number=[-5,-4,-3,-2,-1]
integer=negetive_number+zero+positive_number
print(integer)

# (9) join with extend()

num1=[0,1,2,3]
num2=[4,5,6,7]
num1.extend(num2)
print("Numbers are",num1)

negetive_number=[-5,-4,-3,-2,-1]
zero=[0]
positive_number=[1,2,3,4,5]

negetive_number.extend(zero)
negetive_number.extend(positive_number)
print("integer are",negetive_number)

# (10) count()

fruit=["banana","orange","lemon","mango"]
print(fruit.count("banana"))
age=[20,19,18,18,35,17,18]
print(age.count(18))

# (11) index():

fruit=["banana","orange","lemon","mango"]
print(fruit.index("banana"))
age=[20,19,18,18,35,17,18]
print(age.index(18)) # it scan from left  and find index of given element,if it repetade,then it took 1st element from left side

# (12) reverse()

fruit=["banana","orange","lemon","mango"]
fruit.reverse()
print(fruit)
age=[20,19,18,18,35,17,18]
age.reverse()
print(age)

# sort()

fruit=["banana","orange","lemon","mango"]
fruit.sort()
print(fruit)
fruit.sort(reverse=True)
print(fruit)

age=[20,19,18,18,35,17,18]
age.sort()
print(age)
age.sort(reverse=True)
print(age)