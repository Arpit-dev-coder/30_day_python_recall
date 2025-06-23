

#---------------------> DICTONARY <----------------------------

# def: it is a collection of unorder , modifyable paired(key:value) datatype

# create dictonary

empty_dist={}
print(empty_dist)

dct={"key1":"value1","key2":"value2","key3":"value3"}
print(dct)

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

print(len(person))
print(person)

# accessing dictionary item

dct={"key1":"value1","key2":"value2","key3":"value3"}
print(dct["key1"])
print(dct["key3"])

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

print(person["first_name"])
print(person["ismarries"])
print(person["age"])
print(person["country"])

print(person["skill"])
print(person["skill"][0])

print(person["address"]["street"])
print(person["address"]["pin"])


# add item to dictonary

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

person["job_title"]="student"  # if key present modify that else create new like modifying
person["skill"].append("node js")

print(person)

print()

# modifying item in dictonary

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
person["first_name"]="itachi"
person["age"]=23
print(person)

# checking keys  in dictonary

dct={"key1":"value1","key2":"value2","key3":"value3"}
print("key2" in dct)
print("key9" in dct)

# removing value pair from a dictonary

#     pop("key")  :- remove the specified key item

dct={"key1":"value1","key2":"value2","key3":"value3"}
deleted_value=dct.pop("key1")
print(dct)
print(deleted_value)

#    popitem()    :- remove last item

dct={"key1":"value1","key2":"value2","key3":"value3"}
deleted_value=dct.popitem()
print(dct)
print(deleted_value)


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
deleted_value=person.popitem()
print(person)
print(deleted_value)

deleted_value=person.pop("last_name")
print(person)
print(deleted_value)

#    del          :- removes an item with specified key name


dct={"key1":"value1","key2":"value2","key3":"value3"}
del dct["key2"]
print(dct)

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
del person["address"]
print(person)
del person["skill"][1] # del dct_name["key"][list_index]
print(person)


# changing dictonary to list item 

#     items()

dct={"key1":"value1","key2":"value2","key3":"value3"}
print(dct.items())  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

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
print(person.items())


# getting dictonary keys as a list

#     keys()

dct={"key1":"value1","key2":"value2","key3":"value3"}
keys=dct.keys()
print(keys) #           dict_keys(['key1', 'key2', 'key3'])

# getting dictonary values as list

#     values()

dct={"key1":"value1","key2":"value2","key3":"value3"}
values=dct.values()
print(values) #        dict_values(['value1', 'value2', 'value3'])

#     clear()

dct={"key1":"value1","key2":"value2","key3":"value3"}
print(dct.clear()) #     none

# delecting dictonary by --> del

dct={"key1":"value1","key2":"value2","key3":"value3"}
del dct

# copy() : copy dictonary

dct={"key1":"value1","key2":"value2","key3":"value3"}
copy_dct=dct.copy()
print(copy_dct)
