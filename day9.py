

# -------------------> CONDITIONAL <------------------------


# if condition

# if condition:
#    this part of code run FOR truthy condition

a=3
if a>0:
    print("{} is positive number".format(a))


# if-else

a=4
if (a<4):
    print("{} is negetive number".format(a))
else:
    print("{} is positive number".format(a))

# if elif else

a=0
if (a>0):
    print("{} is positive number".format(a))
elif (a<0):
    print("{} is negetive number".format(a))
else:
    print("a value is neither positive nor negethive ,i.e {}".format(a))

# short hand of conditional

a=3
print("a is positive") if a>0 else print("a is negetive")

# syntax
# code_of_if if (condition) else else_code

# nested condition

a=0
if (a>0):
    if (a%2==0):
        print("a is positive and even integer")
    else:
        print("a is positive integer")

elif (a<0):
    print("{} is negetive number".format(a))
else:
    print("its zero")

# condition and logical operator

num=input("give input here !! ")  # the input that we give that is a string form,so we use type cast here to convert string to int
a=int(num)  
if (a > 0) and (a%2==0) :
     print("a is positive and even integer")
elif (a>0) and (a%2!=0):
    print("a is positive ")
elif (a==0):
    print("a is a zero")
else:
    print("a is negetive")

user="james"
access_level=3
if user == "admin" or access_level>=4: # type: ignore
    print("access granted")
else:
    print("access denied")

