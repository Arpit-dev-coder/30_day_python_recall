

#----------------------> File Handling <---------------------------------

# open("file_name",mode)

# r= read mode
# a= append mode
# w= write mode
# x= create mode
# t= text mode
# b= binary mode(images)

# openfile for reading mode
# hello.txt path=   C:\Users\bapun\OneDrive\Desktop\python\30_day_python_recall\hello.txt
import os
print(os.getcwd())
# working directory=C:\Users\bapun\OneDrive\Desktop\python

# hello.txt path != current directory path ,so it not working,so to convert ones path to another

f=open('hello.txt')
print(f)
f.close() # <_io.TextIOWrapper name='hello.txt' mode='r' encoding='cp1252'>

f=open('hello.txt')
txt=f.read()
print(type(txt))
print(txt)# hello bro,how are you
f.close() # why are you so serious

# read first 10 character from first
f=open('hello.txt')
txt=f.read(10)
print(txt)
f.close() # hello bro,

# readline(): read only first line
f=open('hello.txt')
txt=f.readline()
print(txt)
f.close()# hello bro,how are you

# readlines():read all the text line by line and return list of line
f=open('hello.txt')
txt=f.readlines()
print(txt)
f.close() #          ['hello bro,how are you\n', 'why are you so serious'] here \n is created

# or use splitlines()
f=open('hello.txt')
txt=f.read().splitlines()
print(txt)
f.close() #         ['hello bro,how are you', 'why are you so serious']  here no \n is create

# when open a file we must to close them,but it has high tendency to forgot to close file ,so write it in new way
with open("hello.txt") as h:
    lines=h.read().splitlines()
    print(lines) # ['hello bro,how are you', 'why are you so serious']

# opening file for writing and updating
#  w = will over write any existing content,if file does not exist it create
#  a = append to the end of the file,if the file does not it create a new file
with open("file_handling_ex1.txt","a") as f:
    f.write("this text has to be appened at the end")
with open("file_handling_ex1.txt") as f:
    lines=f.readline(39)
    print(lines)    # this text has to be appended at the end

print("\n")

with open("file_handling_ex2.txt","w") as g:
    g.write("this text will be written in a newly created file ")
with open("file_handling_ex2.txt") as g:
    lines=g.readline(80)
    print(lines)    # this text will be written in a newly created file

# delete file
with open("file_handling_deleted.txt","w") as g:
    print("file is created")
    g.write("i am going to delete this file")
with open("file_handling_deleted.txt") as g:
    lines=g.readline(31)
    print(lines)
# import os
# os.remove("file_handling_deleted.txt")# here we make a file and delete it,if we have not such a file then deleting the file rise the error

# beter way to delete file
import os
if os.path.exists("file_handling_deleted.txt"):
    os.remove("file_handling_deleted.txt")
    print("file is deleted")
else:
    print("it does not exist")

print()

with open("file_handling_deleted.txt","w") as g:
    print("file is created")
    g.write("i am going to delete this file")
with open("file_handling_deleted.txt") as g:
    lines=g.readline(31)
    print(lines)
import os
if os.path.exists("file_handling_deleted1.txt"):
    os.remove("file_handling_deleted.txt")
    print("file is deleted")
else:
    print("it does not exist")

# FILE TYPE
# mainly use here
# (1) txt extention:
# (2) json extention(javascript object notation): it stringified javascript object or python dictonary
# (3) cvc extention( comma separeted value)
# (4) xlsx extention :to read excel files we need to install xlrd package
# (5) xml extention

# Json structure:

#json in dictonary form
# person_dct={
#     "name":"arpit",
#     "age":22,
#     "skills":["js","py","react"]
# }

# # json in string form
# person_json="{'name':'arpit','age':22,'skills'=['js','py','react,]}"

# # use 3 quotes make multipule line
# person_json=''''{
#     "name":"arpit",
#     "age":22,
#     "skills":["js","py","react"]
# }'''

# changing json to dictonary
import json
person_json='''{
    "name":"arpit",
    "age":22,
    "skills":["js","py","react"]
}'''
person_dct=json.loads(person_json)
print(type(person_dct))
print(person_dct)# {'name': 'arpit', 'age': 22, 'skills': ['js', 'py', 'react']}
print(person_dct["name"])

# changing dictonary to json
import json
person_dct={
     "name":"arpit",
     "age":22,
     "skills":["js","py","react"]
 }
person_json=json.dumps(person_dct,indent=4)
print(type(person_json))
print(person_json)
# o/p:

# {
#     "name": "arpit",
#     "age": 22,
#     "skills": [
#         "js",
#         "py",
#         "react"
#     ]
# }


# saving json file

import json
#  python dictonary
person_dct={
     "name":"arpit",
     "age":22,
     "skills":["js","py","react"]
 }
with open("jsonEx.json","w",encoding='utf-8') as save:
    json.dump(person_dct,save,ensure_ascii=False,indent=4)# indent coulde be 2,4,8.it beautifies json 
with open("jsonEx.json") as save:
    lines=save.read()
    print(lines)
#{
#     "name": "arpit",
#     "age": 22,
#     "skills": [
#         "js",
#         "py",
#         "react"
#     ]
# }


# csv: it is a simple file used to store tabular data,such as a spreadsheet ordata base.it is very common in data science

import csv
with open("csvex.csv") as f:
    csv_reader=csv.reader(f,delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count==0:
            print(f"column name are {", ".join(row)}")
            line_count+=1
        else:
            print(f'\t{row[0]} is a teacher . he lives in {row[1]},{row[2]}.')
            line_count+=1
    print(f'number of lines:{line_count}')

# xlsx extention

# import xlrd
# excel_book=xlrd.open_workbook("ex.xlsx")
# print(excel_book.nsheets)
# print(excel_book.sheet_name)

# xml extention

import xml.etree.ElementTree as et
tree=et.parse("xml_ex.xml")
root=tree.getroot()
print("root tag",root.tag)
print("attribute:",root.attrib)
for child in root:
    print("field:",child.tag)
    