

# -----------------> LIST COMPREHENSION <---------------------

# LIST COMPREHENSION:it is a way of creating a list from a sequence.it is sort way to create a new list

# syntax
# [i for i in iterable if expression]

# ex:1
# method :1

language="python"
lst=list(language)
print(lst)

# method : 2
language="python"
lst=[i for i in language]
print(lst)

# ex:2

number=[i for i in range(11)]
print(number)# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square=[i*i for i in range(11)]
print(square)# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# make list of tuples
number=[(i,i*i) for i in range(11)]
print(number)# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

# ex:3

# if combined
even_number=[i for i in range(11) if i%2==0]
print(even_number)# [0, 2, 4, 6, 8, 10]

odd_number=[i for i in range(11) if i%2!=0]
print(odd_number)# [1, 3, 5, 7, 9]

lst=[-8.-7,-6,-5,-3,0,1,2,3,4,5,6,7,8,9]
positive_even_num=[i for i in lst if i>0 and i!=0 and i%2==0]
print(positive_even_num)# [2, 4, 6, 8]

# flattening a three decimal array
lst_of_lst=[[1,2,3],[4,5,6],[6,7,8]]
flattened_lst=[num for row  in lst_of_lst for num in row]
print(flattened_lst)

#------------------------> LAMBDA FUNCTION <-------------------

# create lambda function

# syntax
# x=lambda param1,param2,param3:param1+param2+param3
# print(x(arg1,arg2,arg3))


# basic function

def addition(a,b):
    return a+b
print(addition(2,4))

# do with lambda function

#    self invoking lambda
print((lambda a,b:a+b)(2,4))

# basic function

def square(n):
    return n*n
print(square(2))

# self invoke lambda function

print((lambda n:n*n)(2))

# extra variable lambda function

square=lambda n:n**2
print(square(2))

multipule_variable=lambda a,b,c:a**2-3*b+4*c
print(multipule_variable(5,5,3))

# LAMBDA FUNCTIO INSIDE ANOTHER FUNCTION

def power(x):
    return lambda n:x**n
cube=power(2)(3) # function power now need 2 arg. to run ,in separate rounded bracket,for x=2 and n=5
print(cube)
two_power_of_five=power(2)(5)
print(two_power_of_five)

