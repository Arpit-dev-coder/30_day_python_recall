

#--------------> exceptiopn handling <------------------


# try:
#         {    run this code
#
# except:        may or may not have condition
#         {   exicute this code when there is an exception
#
# else:
#         {   no exception? run this code
#
# finally:
#
#         {   always run code
#

# syntax
# -------------------------------------------------------------
# | try:                                                      |
# |     code _in_ this block  _if_ things go well             |
# | except:                                                   |
# |      code _in_ this block _if_ things go wrong            |
# |------------------------------------------------------------

# ex :1
try:
    print(10+"5")
except:
    print("something wrong")

# ex :2
try:
    #from datetime import datetime
    name=input("pls give input to python ")
    #year=input("give birth year here ")
    # year_born_int=datetime.strptime(year,"%Y")
    # year_born=int(year_born_int.strftime("%Y"))
    year_born=input("year  i born  ")
    age=2025-year_born
    print(f"you are {name}. and age is {age}.")
except:
    print("something wents wrong!!")

# ex :3
try:
    year_born=2004
    age=2025-year_born
    print(f"you are {name}. and age is {age}.")
except TypeError:
    print("type error occured")
except ValueError:
    print("value error occured")
except ZeroDivisionError:
    print("zero division eror occured")

# ex :4
try:
    year_born=2004
    age=2025-year_born
    print(f"you are {name}. and age is {age}.")
except TypeError:
    print("type error occured")
except ValueError:
    print("value error occured")
except ZeroDivisionError:
    print("zero division eror occured")
else:
    print("i usually run with try block")
finally:
    print("i always run")
# ex :6
a=input("enter the number")
print(f"multiplication table of {a} is:")
try:
    for i in range(1,11):
           print(f"{int(a)} x {i} ={int(a)*i}")
except Exception as e:
      print(e)

print("\n") 

# ex:7
a=input("enter the number")
print(f"multiplication table of {a} is:")
try:
    for i in range(1,11):
           print(f"{int(a)} x {i} ={int(a)*i}")
except:
      print("invalid input !")
print("\n")

# ex:8
try:
      num=int(input("enter an integer :"))
      a=[6,3]
      print(a[num])
except ValueError:
      print("number entered is not an intenger")
except IndexError:
      print("imdex error")
# ex :9
try:
    l=[1,5,6,7]# total element 4 4-1=3 ,total 0-3 index means 0,1,2,3
    i=int(input("enter a valid index: "))
    print(l[i])
except:
    print("some error occur")
finally:
    print(" iam execute alwayas")
# print("i am always execute")

# but if we can't use finally but we use a simple code outside of indentation the it must be executed so the diffrent when we use the both 
#code in a function

# ex :10
def fun1():
    try:
      l=[1,5,6,7]# total element 4 4-1=3 ,total 0-3 index means 0,1,2,3
      i=int(input("enter a valid index: "))
      print(l[i])
      return 1 # let 1 for true and 0 for false
    except:
      print("some error occur")
      return 0
    finally:
       print(" iam execute alwayas")
      #  print("i am always execute")
x=fun1()
print(x)
# sorten method
try:
    year_born="2004"
    age=2025-year_born
    print(f"you are {name}. and age is {age}.")
except Exception as e:
    print(e)

# packing and unpacking argument
#   two operator:
#   1) *  : for tuple
#   2) ** : for dictonary

# unpacking:

# unpacking list:

# it give error because this function takes number(not a list) as argument

# sum_five=lambda a,b,c,d,e:a+b+c+d+e
# lst=[i for i in range(1,6)]
# print(sum_five(lst))

sum_five=lambda a,b,c,d,e:a+b+c+d+e
lst=[i for i in range(1,6)]
print(sum_five(*lst))

# we also use unpacking in _range_ builtin function that excepts a start and an end

num=range(2,7)   # normal call with separate argument
print(list(num)) # [2,3,4,5,6]
args=[2,7]
num=range(*args) # call with argument unpacked from a list
print(num)       # [2,3,4,5,6]

# a list or a tuple can also unpacked

city=["balasore","nilagiri","bhadrak","bhubaneswar","raurkela","mumbai"]
bal,nil,bha, *rest=city
print(bal,nil,bha,rest)
nums=[1,2,3,4,5,6,7]
one, *middle,last=nums
print(one,middle,last)

# from city the string in list each string assign to a variable,and rest are assign by *rest
# "balasore"->bal
# "nilagiri"->nil
# "bhadrak"->bha
# "bhubaneswar","raurkela","mumbai"->*rest


# unpacking dictonary

person=lambda name ,country,city,age:print(f"{name} live in {country},city is {city},my age is {age} ")
dct={"name":"arpit","country":"india","city":"balasore","age":22}
person(**dct)

# packing : use packing to allow our function to take  unlimitted number of argument

# packing list
def sum(*args):
    s=0
    for i in args:
        s+=1
    return s
print(sum(1,2,3))
print(1,2,3,4,5,6,7)

# packing dictonary
def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key}={kwargs[key]}")
    return kwargs
print(packing_person_info(name="arpit",country="india",city="balasore",age=22))

# spreading in python

lst_one=[1,2,3]
lst_two=[4,5,6,7]
lst=[0,*lst_one,*lst_two]
print(lst)

city_one=["balasore","cuttak","nilagiri"]
city_two=["bbsr","raurkela","mumbai"]
lst=[*city_one,*city_two]

# enumerate : if we are intrested in index the we can use enumerate built in function

# ex :1
for index,item in enumerate([12,19,36]):
    print(index,item)

# ex :2
for index ,i in enumerate(["balasore"]):
    print("hi")
    if i=="balasore":
        print(f"the country {i} has been found at index{index}")

# ex :3
marks=[12,56,32,98,12,44,1,4]
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("arpit awesome!")
    index+=1

print("\n")

# ex :4
marks=[12,56,32,98,12,44,1,4]
for index, mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("arpit awesome!")

print("\n")

# ex :5
marks=[12,56,32,98,12,44,1,4]
for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("arpit awesome!")

# ex :6
list=["eat","sleep","repeat"]
for count, ele in enumerate(list):
    print(count,ele)

# zip : we would like to combine lists when looping through them

fruit=["banana","orange","mango","lemon"]
veges=["potato","tomato","onion"]
fruit_and_veges=[]
for f,v,in zip(fruit,veges):
    fruit_and_veges.append({"fruit":f,"veg":v})
print(fruit_and_veges)