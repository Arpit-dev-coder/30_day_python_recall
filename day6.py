# --------------> TUPLES <----------------

# tuple :it is a collection of different datatype which is ordered and unchangeable
#        once a tuple is create,we can't change the value,we can't use add,insert,remove methods

# create a tuple

empty_tuple=()
# or use tuple constructor
empty_tuple=tuple()

# tuple with intial value

tpl=("item1","item2","item3")
print(tpl)
fruit=("banana","lime","apple")
print(fruit)

# tuple length

tpl=("item1","item2","item3")
print(len(tpl))


# accessing tuples by index

#   positive indexing:

tpl=("item1","item2","item3")
first_item=tpl[0]
print(first_item)
second_item=tpl[1]
print(second_item)
last_index=len(tpl)-1
last_item=tpl[last_index]
print(last_item)

#   negetive indexing:

tpl=("item1","item2","item3")
first_item=tpl[-3]
print(first_item)
second_item=tpl[-2]
print(second_item)
last_item_item=tpl[-1]
print(last_item)

# slicing of tuple

#     range of positive index

tpl=("item1","item2","item3")
all_item=tpl[0:3]
print(all_item)
all_item=tpl[0:]
print(all_item)
all_item=tpl[:3]
print(all_item)
all_item=tpl[:]
print(all_item)

tpl=("item1","item2","item3","item4")
middle_two_item=tpl[1:3]
print(middle_two_item)

item2_to_rest=tpl[1:]
print(item2_to_rest)

#   range of negetive index

tpl=("item1","item2","item3","item4")
all_item=tpl[-4:]
print(all_item)
middle_two_item=tpl[-3:-1]
print(middle_two_item)

# changing tuples to list

tpl=("item1","item2","item3","item4")
lst=list(tpl)
print(lst)

fruit=("banana","orange","lemon","mango")
print(fruit)
# fruit[0]="apple"
# print(fruit)                TypeError: 'tuple' object does not support item assignment,so convert it into list  to support assignment
fruit=list(fruit)
print(fruit)
# now tuple change to list so modify it
fruit[0]="apple"
print(fruit)                   #so convert it first into list

# checking item present in tuple or not

tpl=("item1","item2","item3","item4")
print("item1" in tpl)
print("banana" in tpl)

# joining tuple (+)

tpl1=("item1","item2","item3","item4")
tpl2=("banana","orange","lemon","mango")
total_is=tpl1+tpl2
print(total_is)

# deleting tuples element using list constructor

fruit=("banana","orange","lemon","mango")

fruit=list(fruit)
del fruit[3]
print(fruit)

fruit=tuple(fruit)# list to tuple
print(fruit)
del fruit
# it is not possible toremove single item in tuple but it's possible to delete the tuple using del

# count()

tup1=(1,1,3,3,3,4)
tup2=tup1.count(3) # we cant directly print tup3  like list but we have to first store in a variable then print that variable
print(tup2)
tup1=(1,1,3,3,3,4)
tup3=tup1.count(1) 
print(tup3)

# index()
tup1=(1,1,3,3,3,4)
tup3=tup1.index(3)# it find the 1st search element index
print(tup3)
print("\n")
tup1=(1,1,3,31,3,4)
tup3=tup1.index(3,3,5)#index(inputelement,startingindex,untilcheckedindex) or index(input,slishingvalue)
print(tup3)
tup4=len(tup3)
print(tup4)
#tup1 is a tupple but tup3,tup4 is a variable which is use for store data not group of data,so we can't print tup3 and tup 4 length but we can print tup1 s length 




#    ---------------------> code with herry <------------------------------




tup1=(1,5,6)
print(type(tup1),tup1)
#tup1[0]=5#it give error because we can not change tuple index
# if we want single value tuple,then we most use , after that element
tup2=(1,)
print(type(tup2),tup2)

#different data type also exist
tup=(1,2,76,342,32,"arpit",True)
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[-1])
print(tup[4-1])
print(tup[len(tup)-1])
# checking
if "arpit" in tup:
    print("yes")
else:
    print("no")
if "pit" in "arpit":
    print("yes")
else:
    print("no")
#when we do tuple slishing it return  a new tuple and we most declare a another tuple
tup2=tup[1:4]
print(tup2)


#Note:-tuple and strings are immutable but list are mutable