
# -------------> SET <-----------------

# set is a collection of un-ordered and un-indexed distinct element.set is used to store uniqe item,and it is possible to find
# union, intersection,difference,symmetric difference,subset,super set and disjoint set among set

# creating a set

st=set()
print(st)

st={"item1","item2","item3","item4"}
print(st)

# getting sets length

st={"item1","item2","item3","item4"}
print(len(st))

#  accessing item in set   : element are access by loop not by index ,we will see this in loops section


# checking items

st={"item1","item2","item3","item4"}
print("item2" in st)

fruit={"banana","lime","apple","lemon","mango"}
print("banana" in fruit)

# add item to set

#   for single value use : add()

st={"item1","item2","item3","item4"}
st.add("item5")
print(st)

fruit={"banana","lime","apple","lemon","mango"}
fruit.add("pine apple")
print( fruit)


#    for multipule value use : update()

st={"item1","item2","item3","item4"}
st.update(["item5","item6","item7"])
print(st)

fruit={"banana","lime","apple","lemon","mango"}
veges={"potato","tomato","onion","garlic"}
fruit.update(veges)
print(fruit)


# remove item in set 

st={"item1","item2","item3","item4"}
st.remove("item2")
print(st)


# pop()

st={"item1","item2","item3","item4"}
removed_item=st.pop()
print(st)
print(removed_item)

# st.pop("item3") # TypeError: set.pop() takes no arguments (1 given)
# print(st)

# clearing item in set

st={"item1","item2","item3","item4"}
st.clear()
print(st)      # set()


fruit={"banana","lime","apple","lemon","mango"}
fruit.clear()
print(fruit)

# deleting set 

fruit={"banana","lime","apple","lemon","mango"}
del fruit


# converting list to set

fruit_list=["banana","lime","apple","lemon","mango"]
print(fruit_list)
fruit_set=set(fruit_list)
print(fruit_set)

# joining of set

#     union() method

fruit={"banana","lime","apple","lemon","mango"}
veges={"potato","tomato","onion","garlic"}
set_join=fruit.union(veges)
print(set_join)

#     update() method

st1={"item1","item2","item3","item4"}
st2={"item5","item6","item7"}
st1.update(st2)
print(st1)


# intersection of set

st1={"item1","item2","item3","item4"}
st2={"item2","item4","item7"}
inter=st1.intersection(st2)
print(inter)

python={"p","y","t","h","o","n"}
dragon={"d","r","a","g","o","n"}
print(python.intersection(dragon))

# subset() and superset()

st1={"item1","item2","item3","item4"}
st2={"item2","item3"}
print(st2.issubset(st1))
print(st1.issuperset(st2))

python={"p","y","t","h","o","n"}
dragon={"d","r","a","g","o","n"}
print(python.issubset(dragon))


# difference between two set

st1={"item1","item2","item3","item4"}
st2={"item2","item3"}
print(st2.difference(st1)) # set()
print(st1.difference(st2)) #  item1 , item4

python={"p","y","t","h","o","n"}
dragon={"d","r","a","g","o","n"}
print(python.difference(dragon))
print(dragon.difference(python))

# symetric difference between 2 set
# (A\B)U(B\A)

st1={"item1","item2","item3","item4"}
st2={"item2","item3"}
print(st2.symmetric_difference(st1))      # {'item1', 'item4'}

python={"p","y","t","h","o","n"}
dragon={"d","r","a","g","o","n"}
print(python.symmetric_difference(dragon)) # {'g', 'r', 'p', 'h', 'a', 'y', 'd', 't'}

# disjoint set      :     if 2 sets do not have a common item or item we call them disjoint sets

st1={"item1","item2","item3","item4"}
st2={"item2","item3"}
print(st2.isdisjoint(st1))

even={2,4,6,8}
odd={1,3,5,7}
print(even.isdisjoint(odd))

python={"p","y","t","h","o","n"}
dragon={"d","r","a","g","o","n"}
print(python.isdisjoint(dragon))


# --------------------> harry <--------------------------

#set
s={2,4,2,6}# in st it takes unique element it means not reapet value
print(s)
info={"arpit",19,True,5.9,19}# it takes different data type
print(info)
# it is not empty set
es={}# both set and dictonary stars and ends with curly bracket,so always give set() for empty set,but this give wrong answer
print(es)
print(type(es))
# but it is emptu set
es=set()# yes we represent the element of set by curly bracket
print(es)
print(type(es))
#excessing of set element
info={"arpit",19,True,5.9,19}#set dont mentain order
for i in info:
      print(i)


s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)#the  value which not in a but in b  updated in a
print(s1,s2)
#symmetric set=(aub)-(anb)
print(s1.symmetric_difference(s2))
# difference()=a-b
print(s1.difference(s2))
#isdisjoint()
print(s1.isdisjoint(s2))
#issuperjoint()
print(s1.issuperset(s2))#it means is all the element of be intially present in a or note
print(s2.issubset(s1))
#add()
s1.add("arpit")
s1.add(10)
print(s1)
s1.remove("arpit")
# s1.remove(11)     #sometime it arrise error if element not present in set And we use remove() by giving that value
print(s1)
#discard()
s1.discard("arpit")
s1.discard(11)# here 11 is not present in set but when we use discard() it can't gibe error
print(s1)
#pop()
temp=s1.pop()
print(s1)
print(temp)
#del()
del s1# here we delete the s1 set so we can't print it
#clear()
#s1.clear()# it gives error because s1 set is deleted by del key word so we have to delete a another set
s2.clear()

