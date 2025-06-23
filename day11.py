

# ----------------------------> FUNCTION <---------------------------

# declaring and calling function

# declare by def
def hello():
    print("hello world")
# calling
hello()

#   function returning a value part 1

def generate_full_name():
    first_name="itachi"
    last_name="uchiha"
    space=" "
    full_name=first_name+space+last_name
    print(full_name)
print(generate_full_name())

def add_two_number():
    num_one=2
    num_two=3
    total=num_one+num_two
    print(total)
print(add_two_number())


#   function without parameter 


def generate_full_name():
    first_name="itachi"
    last_name="uchiha"
    space=" "
    full_name=first_name+space+last_name
    print(full_name)
generate_full_name()

def add_two_number():
    num_one=2
    num_two=3
    total=num_one+num_two
    print(total)
add_two_number()

# function with one parameter

def greeting(name):
    message=name+" happy birth day"
    return message
print(greeting("itachi"))

def add_ten(num):
    ten=10
    return num+ten
print(add_ten(90))

def sum_of_number(n):
    total=0
    for i in range(n+1):
        total=total+i
    print(total)
sum_of_number(10)
sum_of_number(100)

# function with two parameter

def full_name(first_name,last_name):
    space=" "
    return first_name+space+last_name
print(full_name("Arpit","Mishra"))

def add(first_num,second_num):
    return first_num+second_num
print(add(2,7))

def whats_your_age(birth_year,current_year):
    return current_year-birth_year
print("your age is : ",whats_your_age(2003,2025))

def mass_of_object(mass,gravity):
    return str(mass * gravity)+ "N"
print(mass_of_object(60,9.81))

# passing argument with key value

def full_name(first_name,last_name):
    space=' '
    full_name=first_name+space+last_name
    return full_name
print(full_name(last_name="mishra",first_name="arpit"))

def add(first_num,second_num):
    return first_num+second_num
print(add(first_num=10,second_num=10))

# function returning the value part 2

# returning string

def full_name(first_name,last_name):
    space=" "
    return first_name+space+last_name
print(full_name("Arpit","Mishra"))

# returning integer

def whats_your_age(birth_year,current_year):
    return current_year-birth_year
print("your age is : ",whats_your_age(2003,2025))

# returning boolean

def is_even(n):
    if n%2==0:
        print("even")
        return True
print(is_even(8))

# returning a list

def even_number_lst(n):
    even=[]
    for i in range(n+1):
        if i%2==0:
            even.append(i)
    return even
print(even_number_lst(9))

# function with default parameter

def greeting(name="arpit"):
    message=name+" happy birth day"
    return message
print(greeting())
print(greeting("itachi"))

def mass_of_object(mass,gravity=9.81):
    return str(mass * gravity)+ "N"
print(mass_of_object(60))
print(mass_of_object(60,1.62))# gravity on moon

# arbitary  number of argument

def add(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print(add(2,3,5,7,10))

# default and arbitary nubers of parameter in function

def generate_groups(team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups("team-7 :-","kakashi","sasuke","naruto","sakura")

# function as a parameter of another function

def square_number (n):
    return n*n
def do_something(f,x):       # previous_function=f
    return f(x)
print(do_something(square_number,3))



# -----------------------------> harry <----------------------------


def calculategmean(x,y):
    mean=(x*y)/(x+y)
    print(mean)
def isgreater(x,y):
    if(x>y):
       print("first number is greater",x)
    else:
        print("second number is greater",y)
def islesser(x,y):
     pass # pass say continue your other code or instruction after finish all the instruction,then write this function body.so it execute all the instr. without giving error and at last you can finish this function body
a=9
b=8
calculategmean(a,b)
isgreater(a,b)
islesser(a,b)




# if(a>b):
#     print("first number is greater",a)
# else:
#     print("second number is greater",b)
# gmean=(a*b)/(a+b)
# print(gmean)
c=8
d=7
calculategmean(c,d)
# gmean2=(c*d)/(c+d)
# print(gmean2)

def average(a,b):
     print("the average is ",(a+b)/2)
average(4,6)
print("\n")
def average(a=9,b=1):
     print("the average is ",(a+b)/2)
average(4,6)#here this prarameter take and the parameter which pass in function sould be ignore
print("\n")
def average(a=9,b=1):
     print("the average is ",(a+b)/2)
average(b=1,a=9)

print("\n")
def average(a=9,b=1):
     print("the average is ",(a+b)/2)
average(5)# here 5 is takenas the value of a,and parameter of a which pass in function ignored and by default it take argument of b 
print("\n")
def average(a=9,b=1):
     print("the average is ",(a+b)/2)
average(b=9)# here we have to pass b by using "=",otherwise it take the parameter of "a" and "b"parameter in function should be ignored 
print("\n")
def name(fname,mname="kumar",lname="mishra"):
     print("hello",fname,mname,lname)
name("Arpit")
print("\n")

def average(a,b,c=1):
     print("average is ",(a+b+c)/2)
average(2,3)
print("\n")

def average(*num):
     sum=0
     for i in num:
          sum=sum+i
          #print("average is :",sum/ len(num))
          #or
          return sum/len(num)
#average(5,6,7,1)
#or
c=average(5,6,7,1)
print(c)

def name(**name):
     print("hello,",name["fname"],name["mname"],name["lname"])
name(mname="kumar",fname="arpit",lname="mishra")