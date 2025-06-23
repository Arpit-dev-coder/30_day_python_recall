
# -------> string <-------

# (1) writeing method of single line string('' or "")

letter='a'
print(len(letter))

greeting='hello world'
print(len(greeting)) # length including space

sentences="i hope you are enjoying the python language"
print(sentences)
print("length of sentences is :",len(sentences))

# (2) writing method of multi line string(''' ''' or """ """)

multiline_string="""hello ,i am arpit 
   i am enjoying 30 days of python learning
   """
print(multiline_string)

  # multi line print statement
print("""hello ,i am arpit 
   i am enjoying 30 days of python learning
   """)

#  (3) string connection

first_name="arpit"
last_name="mishra"
space=" "
full_name =first_name+space+last_name
print(full_name)

print(len(first_name)>len(last_name))

# (4) unpacking character : unpack sequence of character into variable

# language="python"
a,b,c,d,e,f="python"
print(a)  # p
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

language="python"
a,b,c,d,e,f=language
print(a)  # p
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
# print(g) # no language left ,so if we print 'g' it throws error,  ValueError: not enough values to unpack 

# ex:-
m,n,m,n=[0,1,2,3]
print(m,n)

m=1
n=2
m,n,m,n=[3,4,5,6]
print(m,n)
#   m=1
#   n=2
# then:
#   m=3
#   n=4
# then:
#   m=5
#   n=6
# (5) Accessing character in the string by index

# (i) positive indexing

language='python'
first_latter=language[0]
print(first_latter) #p
second_latter=language[1]          # 0 1 2 3 4 5             li=len(language)-1
print(second_latter)#y               p y t h o n
last_index=len(language)-1
last_latter=language[last_index]
print(last_latter)

# (ii) negetive indexing

language='java'
last_latter=language[-1]             # -6 -5 -4 -3 -2 -1     fi=(-len(latter))   
print(last_latter)                    # p  y  t  h  o n
second_last_latter=language[-2]
print(second_last_latter)
first_index=-len(language)
print(first_index)
first_latter=language[first_index]
print(first_latter)


# (6) slicing

language="python"
first_three=language[0:3] # start with 0 and end upto 3 bu not including 3
print(first_three)
last_three=language[3:6]
print(last_three)
# another way
last_three=language[-3:]  # [len(language)-3:]-----> [3:]
print(last_three)#                            direct way
last_three=language[3:]                      #------>[3:]
print(last_three)

fruit="mango"
print(fruit[0:])
print(fruit[:])
print(fruit[0:-3])#or
print(fruit[0:len(fruit)-3]) #above and this line both are same 2nd line just the meaning of above line[0:5-3]=[0:2]-->ma,python tke autometically len()of variable
print(fruit[-1:len(fruit)-3])#5-1=4 &5-3=2 it means[4:2]there is no sence so nothing should be print here
print(fruit[-3:-1])# or
print(fruit[-3:len(fruit)-1])# it means 5-3=2 and 5-1=4 so limit is[2:4] 2 to 3 rd character m=0,a=1,(n=2,g=3),o=4="ng"

# (7) skipping character while splitting  python string

language="python"
pto=language[0:6:2]  # sequence[start,stop,step] this three parameter will skip
print(pto)           # 0 1 2 3 4 5 6
#                      p y t h o n
#                      ^   ^   ^
#                      start with 0 
#                      move upto 6 but not 6
#                      step->2,take every second character,it means first and step will skip


# (8) escape sequence.

print("i hope every one enjoying the python challenge.\nDo you?")
print()
print("days\tTopic\texercises")
print("day 1\t3\t5")
print("day 2\t3\t5")
print("day 3\t3\t5")
print("day 4\t3\t5")

# (9) string method

# len()

a="arpit!!! !!!!!"
print(len(a))

# upper()

b=a.upper()
print(b)

# lower()

c=b.lower()
print(c)                             # string are unmutable

# rstrip()

print(a.rstrip("!"))                 # it remove symbols and give required output,it  is not for starting symbol but it for the symbol after series of alphabate

# replace()

print(a.replace("arpit","jhon"))     # it  replace a string to another string,it means it replace "arpit"-->"jhon",if we give multipule string "arpit" that also change to multipule "jhon"

# split()

print(a.split(" "))                  #it create a list

# capitalize()

blogheading="welcome to python and JS tutorial"
print(blogheading.capitalize())      # w is in capital, convert JS to js .it means it capitalize first word of a line not after ,if it found any captal after first word then it convert to lowercase

# center()

str1="welcome to console!!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))          # it give the n input number space before line

# count()

d="arpit!!!!!!!!!!!arpit!!!!!!!arpit"
print(d.count("arpit"))
e="aeroplane"
print(e.count("a"))

# endswith()

print(str1.endswith("!!"))            # it return boolean
print(str1.endswith("to",4,10))       # it count 4 to 9 iteration

# find()

str1="he's name is dan.he is an honest man."
print(str1.find("is"))                #it return idex
print(str1.find("ishh"))              #it return -1 because no index should be found

#                alphanumeric:A-Z,a-z,0-9 cobination string
 
# isalnum()

str1= "welcometoconsole"                # if any space or other symbole comes inside this line the it return false and ? this symbole in a string give error
print(str1.isalnum())
str1= "welcometoconsole&&"
print(str1.isalnum())

#               isalpha:A-Z,a-z ,no number

# isalpha()

str1= "welcometoconsole"
print(str1.isalpha())
str1= "welcometoconsole67"
print(str1.isalpha())

# islower()

str1="hello world"
print(str1.islower())
str1="hello worlD"
print(str1.islower())                        # it return because D is capital

# isprintable()

str1="hello\n"
print(str1.isprintable())                    #  \n give next line so it is not printable so it return false

# isspace()

str1="                  "                    # using: space bar
print(str1.isspace())
str2="              "                        # using:tab
print(str2.isspace())

# title()

str1="he's name is dan.he is an honest man."  #it capitalize every word 1st alphabate
print(str1.title())

# startswith("string")

str1="he's name is dan.he is an honest man."
print(str1.startswith("he"))

# swapcase()

str1="he's name is dan.he is an honest man."
print(str1.swapcase())

# expandstab()

challenge="thirty\tday's\tof\tpython"
print(challenge.expandtabs())              # default tab size is 8
print(challenge.expandtabs(10))            # costumize tab size

# format()

first_name="arpit"
last_name="mishra"
job="student"
country="india"
sentences="i am {} {}. i am a {}. i live in {}.".format(first_name,last_name,job,country)
print(sentences)

# isdecimal()

num='10'
print(num.isdecimal())
num="10.5"
print(num.isdecimal())

# isdigit()

challenge="thirty"
print(challenge.isdigit())
challenge="30"
print(challenge.isdigit())

# join()

web_tech=["HTML","JS","JAVA","REACT JS"]
result='#, ' .join(web_tech)
print(result)

# isidentifier():    it check weather a string valid variable or not

challenge="30daysofpython"
print(challenge.isidentifier())           # false
challenge="thirty_days_of_python"
print(challenge.isidentifier())           # true

# isupper()

challenge="thirty days of python"
print(challenge.isupper())                # false
challenge=challenge.upper()
print(challenge.isupper())                # true

# f string use for string formating
bio="hi! my name is {} & i am from {}"
name="Arpit"
country="india"
print(bio.format(name,country))

bio="hi! my name is {} & i am from {}"
name="Arpit"
country="india"
print(bio.format(country,name))

bio="hi! my name is {1} & i am from {0}"
name="Arpit"
country="india"
#print(bio.format(0th,1th))
print(bio.format(country,name))

#   f"string"
bio="hi! my name is {1} & i am from {0}"
name="Arpit"
country="india"
print(f"hi! my name is {name} & i am from {country}")

#ex2
txt="for only price {price:.2f}$"
print(txt.format(price=49.09999))
#now do this by f"string"
price=49.0999
txt=f"for only price {price:.2f}$"
print(txt)
price=49.0999
txt=f"for only price {{price:.2f}}$"#if we want to show our curly bracket we can use: {{}}
print(txt)
#ex3
print(f"{2*30}")
print(type(f"{2*30}"))