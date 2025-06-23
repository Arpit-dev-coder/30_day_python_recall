

# -----------------------> PANDAS <------------------------

# pandas:pandas add data structure and tools designed to work with table-like data which is series and data frames

# tools:
# ->reshaping
# ->merging
# ->sorting
# ->slicing
# ->aggregation
# ->imputation

# creating pandas series with default index
import pandas as pd
import numpy as n
nums=[1,2,3,4]
s=pd.Series(nums)
print(s)

print()

# creating pandas series with custom index
import pandas as pd
import numpy as n
nums=[1,2,3,4]
s=pd.Series(nums,index=[1,2,3,4])
print(s)

print()

fruit=["mango","lemon","apple"]
f=pd.Series(fruit,index=[3,2,1])
print(f)
print()

# if u think its safe then use: # type: ignore

Person={ # type: ignore
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
p=pd.Series(Person)  # type: ignore
print(p)

print()

# creating a constant pandas series
s=pd.Series(10,index=[1,2,3,4])
print(s)

print()

# creating a pandas series using linspace
s=pd.Series(n.linspace(5,20,10))# linspace(start,end,item)
print(s)

print()

# Data Frame
  # creating dataframe from list of list
data=[
    ["arpit","nilagiri","odisha"],
    ["kaushik","mumbai","maharastra"],
    ["raghab","banglore","karnatak"]
]
df=pd.DataFrame(data,columns=["name","city","state"])
print(df)

print()

data=[
    ["arpit","nilagiri","odisha"],
    ["kaushik","mumbai","maharastra"],
    ["raghab","banglore","karnatak"]
]
df=pd.DataFrame(data,columns=["name","city","state"],index=[1,2,3])
print(df)

print()

# creating dataframe using list of dictonary
data=[
    {"name":"arpit","city":"nilagiri","state":"odisha"},
    {"name":"kaushik","city":"delhi","state":"delhi"},
    {"name":"raghab","city":"kota","state":"rajastan"}
]
df=pd.DataFrame(data)
print(df)
print()

     # add new coumn
weight=[74,78,79]
df["Weight"]=weight
print(df)
print()

height=[173,175,177]
df["Height"]=height
print(df)
print()

     # modify value
df["Height"]=df["Height"]*0.01
print(df)
print()

     # use function and calulate bmi
def calculate_bmi():                  # type:ignore
    weight=df["Weight"]               # type:ignore
    height=df["Height"]               # type:ignore
    bmi=[]
    for w,h in zip(weight,height):    # type:ignore
        b=w/(h*h)                     # type:ignore
        bmi.append(b)                 # type:ignore
    return bmi                        # type: ignore
bmi=calculate_bmi()                   # type:ignore
df["BMI"]=bmi
print(df)
print()

     # formating dataframe columns:
     # data frame are float with many significant digits after decimal,let change 1 signifacant decimal point
df["BMI"]=round(df["BMI"],1)          # type:ignore
print(df)
print()

     # add birth year and current year
birth_year=["2003","2009","2010"]
current_year=pd.Series(2020,index=[0,1,2])
df["Birth_Year"]=birth_year
df["Current_Year"]=current_year
print(df)
print()

    # checking datatype of column value
print(df.Weight.dtype)                # type:ignore

df["Birth_Year"]=df["Birth_Year"].astype("int")
print(df["Birth_Year"].dtype)
print()

df["Current_Year"]=df["Current_Year"].astype("int")
print(df["Current_Year"].dtype)
print()

ages=df["Current_Year"]-df["Birth_Year"]
print(ages)
print()

df["Age"]=ages
print(df)
print()

mean=(15+10)/2
print(mean)
print()

     # boolean indexing
print(df[df["Age"]>15])
print(df[df["Age"]<15])
print()

# creating a dataframe using dictonary
data={
    "name":["arpit","kaushik","raghab"],
    "city":["nilagiri","mumbai","banlore"],
    "state":["odisha","maharastra","kerala"]
}
df=pd.DataFrame(data)
print(df)
print()

# reading csv file using pandas
import pandas as pd
import os
p=os.getcwd()
print(p)#       C:\Users\bapun\OneDrive\Desktop\python
# csv file path:C:\Users\bapun\OneDrive\Desktop\python\weight-height.csv
print()

df=pd.read_csv("weight-height.csv")# type:ignore
print(df)
print()

# DATA EXPLORATION

# access element from top
print(df.head())# give five row from top,we can increase row by passing argument to head method
print(df.head(7))
print()

# accessing element from bottom
print(df.tail())# give five row from bottom,we can increase row by passing argument to head method
print(df.tail(7))
print()

# to know all the row and col in csv file use ---> shape
print(df.shape)
print()

# know col heading using --->columns
print(df.columns)
print()

# get a specific col using column key
height=df["Height"] # check spelling correctly from csv file # type:ignore
print(height) # type:ignore
print()

weight=df["Weight"] #type:ignore
print(weight) #type:ignore
print()

print(len(height)==len(weight))# type:ignore
print()

# describe():its provide a descriptive statistical value of data set
print(height.describe())# type:ignore
print()

print(weight.describe())# type:ignore
print()
