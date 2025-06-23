

#-------------------> LOOP <-------------------
# DO WHILE LOOP
i=0
while True:
    print(i)
    i=i+1
    if(i%10==0):
        break


# WHILE LOOP

count=0
while count<5:
    print(count)
    count=count+1

# while with conditional

count=10
while count<5:
    print(count)
    count=count+1
else:
    print(count)


# break and continue part-I

#    break : use break when we like to get out of or stop the loop

count=0
while count<5:
    print(count)
    count=count+1
    if (count==3):
        break

#    continue : here we can skip the current iteration and continue with the next

count=0
while count<5:
    if (count==3):
        count=count+1
        continue     # 1,2,4 ____3 is skiped
    print(count)
    count=count+1
    

# FOR LOOP

#               syntax

#             for iterator in 1st:
#                      code goes here   

# for loop with list

numbers=[1,2,3,4,5]
for i in numbers:
    print(i)

# for loop with string

language="python"
for i in language:
    print(i)

for i in range(len(language)):
    print(language[i])

# for loop with tuples

numbers=(1,2,3,4)
for i in numbers:
    print(i)

for i in range(len(numbers)):
    print(numbers[i])

# for loop with dictonary

person={
    "first_name":"arpit",
    "last_name":"mishra",
    "age":22,
    "country":"india",
    "ismarries":True,
    "skill":["js","python","HTML","CSS"],
    "address":{
        "street":"panchalingeswar",
        "town":"nilagiri",
        "pin":756040
    }
}
#    only get key
for key in person:
    print(key)
#    get key and value
for key,value in person.items():
    print(key,value)


# for loop with set

numbers={1,2,3,4,5,}
for num in numbers:
    print(num)


#  break and continue part-II

#   break
numbers={1,2,3,4,5,}
for num in numbers:
    print(num)
    if num==3:
        break

# continue
numbers={1,2,3,4,5,}
for num in numbers:
    print(num)
    if num==3:
        continue
    print("next number should be",num+1) if num!=5 else print("loop is end")
print("outside the loop")

# range()

lst=list(range(8))
print(lst)      # [0, 1, 2, 3, 4,4,5,6,7]

lst=list(range(1,8))
print(lst)     #  [1, 2, 3, 4,5,6,7]

lst=list(range(1,8,3)) # add item with start every 3 iteration
print(lst)     #  [1, 4, 7]    1 +3 =_4_ +3 = _7_ +3 =_10_

st=set(range(0,8,2))
print(st)

# nested for loop

person={
    "first_name":"arpit",
    "last_name":"mishra",
    "age":22,
    "country":"india",
    "ismarries":True,
    "skill":["js","python","HTML","CSS"],
    "address":{
        "street":"panchalingeswar",
        "town":"nilagiri",
        "pin":756040
    }
}
for i in person:
    if i=="skill":
        for j in person["skill"]:
            print(j)

# for else

for number in range(11):
    print(number)
else:
    print("the loop stop at ",number)

# pass      :it is required after semicolon,when we donot like to execute any  code ,there we use pass to avoid error

for number in range(6):
    pass





#--------------------------> Harry<-----------------------

# for loop

#     increment while loop
i=0
while(i<3):
    print(i)
    i=i+1
print("\n")
#     decrement while loop
i=5
while(i>0):
    print(i)
    i=i-1
print("\n")

i=5
while(i>0):
    print(i)
    i=i-1
else:
    print("i am in else")
print("\n")

for i in range(3):
    print(i)

print("\n")

i=int(input("enter the number: "))#we take input i
while(i<=38):# i will check here weather true or false
    i=int(input("enter the number: "))# then it asking us for another input for printing
    print(i)# finally print here. take input let 12 and another time take input 98
print("done with loop")
print("\n")
i=5

# for loop

name="arpit"
for i in name:
    print(i)
 
    if(i=="a"):
        print("a is special")
print("\n")
#ex-2
colours=["red","black","green","blue","yellow"]
for x in colours:
    print(x)
    for i in x:
        print(i)
print("\n")
#ex-3
for k in range(5):#range():if we pass a parameter let n, it give the output n-1
    print(k)
print("\n")
for k in range(1,5):# range(a,b) means a stands for starts from and b stands for ending range which is b-1
    print(k)
print("\n")
for k in range(1,12,3):
    print(k)   

# print a to z character
for ch in range(ord('A'),ord('Z')+1):
   print(chr(ch)) #Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
   #print(chr(ch),end='') # above printing statement only one statement exist fo this code

   #for ch in range('A','Z'):
  #     print(str(ch))# we can't print char like this  like a printing of imteger we have to follow ord() and chr()

   # some useful functinn
    
asii=ord('Z')# ord()--> it convert a character to asii code
print(asii)
ch=chr(asii)#  chr()--> it convert a asii code to character
print(ch)

# small basic concept of for loop in python
for x in range(1,5):
    x=x+1
    print("hi")
# small basic concept of for loop in python
for x in range(0,5):
    x=x+2
    if(x>=5): # before using if the output become 6 whichi is grater then 5 so we use if with break statement
        break
    print(x)

#example
n=int(input("enter the range"))
for x in range(0,n):
    print(x)
print("\n")

# table of 2
for i in range(1,10):
    print("2 *",i,"=",2*i)