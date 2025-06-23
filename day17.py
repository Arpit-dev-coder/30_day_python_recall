

#------------------> Regular Expression <---------------------


# rgular expression or RegEx: a special text string help to find pattern in data. it check if some pattern exist in a different datatype
#                             to use it first import te module _re_


# method in re module :
# (1)re.match() : search only beginning of first line of the string and return matched object if found,else return none
# (2)re.search  : return matched object if found anywhere in the string,including multiline string
# (3)re.findall : return a list containing all matches
# (4)re.split   : takes a string,split it at the match point,return a list
# (5)re.sub     : replace one or many matches with in a string


#   match(substring,main_string_stored_variable,re.I):
import re
txt="search only beginning of first line of the string and return matched object if found,else return none"
match=re.match("search only beginning",txt,re.I)
print(match)

span=match.span()
print(span)

start,end =span
print(start,end)

substring=txt[start:end]
print(substring)

# print none if faild to search from beginning
import re
txt="search only beginning of first line of the string and return matched object if found,else return none"
match=re.match("search from beginning",txt,re.I)
print(match)

# search("target string",main_string_stored_variable,re.I):
import re
txt="search only beginning of first line of the string and return matched object if found,else return none"
match=re.search("else",txt,re.I)
print(match)

span=match.span()
print(span)

start,end =span
print(start,end)

substring=txt[start:end]
print(substring)

# findall()
txt="search only beginning of first line of the string and return matched object if found,else Return none"
matches=re.findall("return",txt,re.I)
print(matches)

txt="search only beginning of first line of the string and return matched object if found,else RETURN none"
matches=re.findall("return",txt,re.I)
print(matches)

# re.I use for both uppercase and lowercase,if we dont use use that re.I flag then write like bellow
txt="search only beginning of first line of the string and return matched object if found,else Return none"
matches=re.findall("return|Return",txt)
print(matches)

txt="search only beginning of first line of the string and return matched object if found,else return none"
matches=re.findall("[Rr]eturn",txt)
print(matches)

# replace a substring
txt="search only beginning of first line of the string and return matched object if found,else Return none"
replace=re.sub("string","list",txt,re.I)
print(replace) # search only beginning of first line of the _list_ and return matched object if found,else Return none

txt="search only beginning of first line of the STRING and return matched object if found,else Return none"
replace=re.sub("string","list",txt,re.I)
print(replace) # search only beginning of first line of the _STRING_ and return matched object if found,else Return none

txt="search only beginning of first line of the STRING and return matched object if found,else Return none"
replace=re.sub("string|STRING","list",txt)
print(replace) # search only beginning of first line of the list and return matched object if found,else Return none

txt="search only beginning of first line of the String and return matched object if found,else Return none"
replace=re.sub("[sS]tring","list",txt)
print(replace)  # search only beginning of first line of the list and return matched object if found,else Return none

# ex :2
txt="%I% %am %a %stu%de%n%t% %."
replace=re.sub("%","",txt)
print(replace)

# splitting text using RegEx split
txt=txt='''search only beginning of first line of the String and return matched object if found,else Return none.
           return matched object if found anywhere in the string,including multiline string.
           return a list containing all matches.
           takes a string,split it at the match point,return a list.'''
print(re.split("\n",txt))
# ['search only beginning of first line of the String and return matched object if found,else Return none.', ' return matched object if found anywhere in the string,including multiline string.', ' return a list containing all matches.', 'takes a string,split it at the match point,return a list.']



# ---------------------------------------
# | Detail check in image.png file      |
# | Detail check in python2.jpg         |
# ---------------------------------------


# square bracket([])
regex_pattern=r"[Aa]pple"
txt="apple and banana are fruit.an old cliche says an Apple a day a doctor way has been replaced"
matches=re.findall(regex_pattern,txt)
print(matches)  # ['apple', 'Apple']

regex_pattern=r"[Aa]pple|[Bb]anana"
txt="apple and banana are fruit.an old cliche says an Apple a day a doctor way has been replaced"
matches=re.findall(regex_pattern,txt)
print(matches)  # ['apple', 'banana', 'Apple']

# escape character(\)
regex_pattern=r'\d'
txt="this regular expression example was made on may 28"
matches=re.findall(regex_pattern,txt)
print(matches) 

# one or more time(+)
regex_pattern=r'\d+' # d is a special character which means digit,+ means one or more time
txt="this regular expression example was made on may 28"
matches=re.findall(regex_pattern,txt)
print(matches)

# period(.)
regex_pattern=r'[a].'
txt='''''apple and banana are fruit.'''
matches=re.findall(regex_pattern,txt)
print(matches) # ['ap', 'an', 'an', 'an', 'a ', 'ar']

regex_pattern=r'[a].+'
txt='''''apple and banana are fruit.'''
matches=re.findall(regex_pattern,txt)
print(matches) # ['apple and banana are fruit.']

# zero or more time (*)
regex_pattern=r'[a].*'# . any character,* any character zero or more time
txt='''''apple and banana are fruit.'''
matches=re.findall(regex_pattern,txt)
print(matches) # ['apple and banana are fruit.']

# zero or one times(?)
txt='''''i am not sure if there is a convention how to write word email.
some people write it as emial others may write  it as Email.'''
regex_pattern=r'[Ee]-?mail.*'# ? it means - is optional
matches=re.findall(regex_pattern,txt)
print(matches) # ['email.', 'Email.']

txt='''''i am not sure if there is a convention how to write word e-mail.
some people write it as emial others may write  it as Email.'''
regex_pattern=r'[Ee]-?mail.*'# ? it means - is optional
matches=re.findall(regex_pattern,txt)
print(matches) # ['e-mail.', 'Email.']

# quantifier in regex
txt="this regular expression was made  on 28 may ,2025 and revised june 6 ,2026"
regex_pattern=r'\d{4}' # exactly 4 time
matches=re.findall(regex_pattern,txt)
print(matches) # ['2025', '2026']

txt="this regular expression was made  on 28 may ,2025 and revised june 6 ,2026"
regex_pattern=r'\d{1,4}'
matches=re.findall(regex_pattern,txt)
print(matches) # ['28', '2025', '6', '2026']

# cart ^
txt="this regular expression was made  on 28 may ,2025 and revised june 6 ,2026"
regex_pattern=r'^this'# ^ means start with
matches=re.findall(regex_pattern,txt)
print(matches) # ['this']

txt="this regular expression was made  on 28 may ,2025 and revised june 6 ,2026"
regex_pattern=r'[^A-Za-z ]+'
matches=re.findall(regex_pattern,txt)
print(matches) # ['28', ',2025', '6', ',2026']