# variable in python
 
first_name='arpit'
last_name='mishra'
country='india'
city='balasore'
age='22'
is_married=True
skills=['html','css','js','py','java']
person_info={
    'first_name':'arpit',
    'last_name':'mishra',
    'country':'india',
    'age':'22',
    'city':'balasore'
}
print(type(person_info))
print()

# printing the values stored in variables

print('first name:', first_name)
print('last name :',last_name)
print('country :',country)
print('city :',city)
print('age :',age)
print('is_married :',is_married)
print('skill :',skills)
print('person_info', person_info)

# declared multipule variable in one line
print()

first_name,last_name,city,country,age,is_married='arpit','osatsuki','hydrabad','india',23,False
print(first_name,last_name,city,country,is_married)
print('first name:', first_name)
print('last name :',last_name)
print('country :',country)
print('city :',city)
print('age :',age)
print('is_married :',is_married)

# len()
print()

print(len(first_name))
print(len(last_name))
print(len(city))
print(len(country))
# print(len(age))                TypeError: object of type 'int' has no len()
# print(len(is_married))         TypeError: object of type 'bool' has no len()
print(len(skills))
print(len(person_info))

# input()


first_name=input('first name is :')
last_name=input('last name is :')

print(first_name)
print(last_name)
print('my name is ', first_name,last_name)

# CASTING:

# int to float
num_int=10
print('num_int',num_int)                  # 10
num_float=float(num_int)
print('num_float :', num_float)           # 10.0

# float to int
gravity=9.8
print(int(gravity))                        # 9

# int to str
num_int=10                                 # 10
print(num_int)
num_str=str(num_int)
print(num_str)                             # '10'

# str to int or float
num_str='10.6'
num_float=float(num_str)
print('num_float',float(num_str))          # 10.6
num_int=int(num_float)
print('num_int',int(num_int))              # 10

# str to list
first_name='arpit'
print(first_name)
first_name_to_list=list(first_name)
print(first_name_to_list)


# *** USEFULL FUNCTION ***


# max min for tuple

print(max(2,3,4,5))
print(min(2,3,4,5))

# max min sum for list

print(max([2,3,4,5]))
print(min([2,3,4,5]))
print(sum([2,3,4,5]))

#  ------> powerfull <--------

help(str)
