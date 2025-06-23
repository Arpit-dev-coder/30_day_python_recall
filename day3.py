# ---------> OPETRATOR <----------

# arithmetic operator

# integer
print('addition',1+2)
print('substraction',2-1)
print('multiplication',4*2)
print('division',4/2)
print('modulus',3%2)
print('floor division or division without any remainder',7//3)
print('exponential',2**2)

# floating number
print('pi value is :',3.14)
print('gravity value is :',9.81)


# complex number

print('complex number',1-3j)
print('multiplication of complex number',(1+5j) * (3+6j)) # don't do print('multiplication of complex number',1+5j * 3+6j)

# declare value and organize them together
num_one=3
num_two=4
total=num_one + num_two
diff=num_two - num_one
mul=num_one * num_two
div=num_two / num_one

print('total is :',total)
print('diff is :',diff)
print('mul is :',mul)
print('div is :',div)

# comparing operator

print(3>2)
print(3>=2)
print(3<2)
print(3<=2)
print(3==2) # type: ignore
print(3!=2) # type: ignore
print(len('mango')==len('avocado'))
print(len('mango')!=len('avocado'))
print(len('mango')<len('avocado'))

# boolean comaprision

print('True == True',True==True)
print('True==False',True==False) # type: ignore
print('False==False',False==False)
print('True and True',True and True)
print('True or False',True or False)

# another way of comparision

print('1 is 1',1 is 1)
print('1 is not 2',1 is not 2) # type: ignore
print('A in Arpit','A' in 'Arpit')
print('B in Arpit','B' in 'Arpit')
print('4 is 2**2',4 is 2**2)

print(3>2 and 4>3)
print(3>2 and 4<3)
print(3<2 and 4<3)
print(3>2 or 4>3)
print(3>2 or 4<3)
print(3<2 or 4<3)
print(not 3>2)
print(not True)
print(not False)
print(not not True)
print(not not False)
