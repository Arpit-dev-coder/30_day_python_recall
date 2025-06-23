

#------------------> Statistics <----------------------

import numpy as n
print(n.__version__)
# available method
print(dir(n))
['False_', 'ScalarType', 'True_', '_CopyMode', '_NoValue', '__NUMPY_SETUP__', '__all__', '__array_api_version__', '__array_namespace_info__',
 '__builtins__', '__cached__', '__config__', '__dir__', '__doc__', '__expired_attributes__', '__file__', '__former_attrs__', '__future_scalars__',
 '__getattr__', '__loader__', '__name__', '__numpy_submodules__', '__package__', '__path__', '__spec__', '__version__', '_array_api_info',
 '_core', '_distributor_init', '_expired_attrs_2_0', '_get_promotion_state', '_globals', '_int_extended_msg', '_mat', '_msg', '_no_nep50_warning',
 '_pyinstaller_hooks_dir', '_pytesttester', '_set_promotion_state', '_specific_msg', '_type_info', '_typing', '_utils', 'abs', 'absolute', 'acos', 'acosh',
 'add', 'all', 'allclose', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 
 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array',
 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 
 'ascontiguousarray', 'asfortranarray', 'asin', 'asinh', 'asmatrix', 'astype', 'atan', 'atan2', 'atanh', 'atleast_1d', 'atleast_2d',
 'atleast_3d', 'average', 'bartlett', 'base_repr', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_count', 'bitwise_invert', 'bitwise_left_shift', 
 'bitwise_not', 'bitwise_or', 'bitwise_right_shift', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool', 'bool_', 'broadcast', 'broadcast_arrays',
 'broadcast_shapes', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'bytes_', 'c_', 'can_cast', 'cbrt', 'cdouble', 'ceil', 
 'char', 'character', 'choose', 'clip', 'clongdouble', 'column_stack', 'common_type', 'complex128', 'complex64', 'complexfloating', 'compress', 'concat',
 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 
 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumsum', 'cumulative_prod', 'cumulative_sum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad',
 'degrees', 'delete', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'divide', 'divmod', 'dot', 'double', 'dsplit', 
 'dstack', 'dtype', 'dtypes', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exceptions', 'exp', 
 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'f2py', 'fabs', 'fft', 'fill_diagonal', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr',
 'flipud', 'float16', 'float32', 'float64', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_float_positional', 'format_float_scientific',
 'frexp', 'from_dlpack', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'gcd', 'generic', 'genfromtxt', 
 'geomspace', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 
 'histogram', 'histogram2d', 'histogram_bin_edges', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact',
 'inf', 'info', 'inner', 'insert', 'int16', 'int32', 'int64', 'int8', 'int_', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'is_busday', 'isclose', 'iscomplex',
 'iscomplexobj', 'isdtype', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issubdtype', 'iterable', 'ix_',
 'kaiser', 'kron', 'lcm', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 
 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longdouble', 'longlong', 'ma', 'mask_indices', 'matmul', 'matrix', 'matrix_transpose',
 'max', 'maximum', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mod', 'modf', 'moveaxis', 'multiply', 'nan', 'nan_to_num',
 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanquantile', 'nanstd', 'nansum', 'nanvar', 'ndarray', 'ndenumerate', 'ndim',
 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'number', 'object_', 'ogrid', 'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition', 'percentile',
 'permute_dims', 'pi', 'piecewise', 'place', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'positive', 'pow', 'power', 'printoptions', 
 'prod', 'promote_types', 'ptp', 'put', 'put_along_axis', 'putmask', 'quantile', 'r_', 'rad2deg', 'radians', 'random', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'reciprocal', 'record', 
 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'row_stack', 's_', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctypeDict',
 'searchsorted', 'select', 'set_printoptions', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'show_runtime', 'sign', 'signbit', 'signedinteger', 'sin',
 'sinc', 'single', 'sinh', 'size', 'sort', 'sort_complex', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str_', 'strings', 'subtract', 'sum', 'swapaxes', 'take', 'take_along_axis', 'tan', 'tanh', 
 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 'transpose', 'trapezoid', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide',
 'trunc', 'typecodes', 'typename', 'typing', 'ubyte', 'ufunc', 'uint', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulong', 'ulonglong', 'union1d', 'unique', 'unique_all', 'unique_counts', 'unique_inverse', 'unique_values', 
 'unpackbits', 'unravel_index', 'unsignedinteger', 'unstack', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vecdot', 'vectorize', 'void', 'vsplit', 'vstack', 'where', 'zeros', 'zeros_like']

# create  numpy array  using

 # create int numpy array
import numpy as n
py_lst=[1,2,3,4,5]
print(type(py_lst))
print(py_lst)

two_d_lst=[[0,1,2],[3,4,5],[6,7,8]]
print(two_d_lst)

 # creating numpy array from python list
numpy_array_from_list=n.array(py_lst)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# create float numpy array
py_lst=[1,2,3,4,5]
numpy_array_from_list2=n.array(py_lst,dtype=float)
print(numpy_array_from_list2)# [1. 2. 3. 4. 5.]

# create boolean numpy array
numpy_bool_array=n.array([0,1,-1,0,0],dtype=bool)
print(numpy_bool_array)# [False  True  True False False]

# creating multidimentionl array using numpy
two_d_lst=[[0,1,2],[3,4,5],[6,7,8]]
numpy_2d_lst=n.array(two_d_lst)
print(type(two_d_lst))
print(numpy_2d_lst)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# convert numpy array to list
py_lst=[1,2,3,4,5]
numpy_array_from_list=n.array(py_lst)

np_to_lst=numpy_array_from_list.tolist()
print(type(np_to_lst))
print(np_to_lst)

# for 2D 
two_d_lst=[[0,1,2],[3,4,5],[6,7,8]]
numpy_2d_lst=n.array(two_d_lst)

np_to_2D_lst=numpy_2d_lst.tolist()
print(type(np_to_2D_lst))
print(np_to_2D_lst)

# create numpy array from tuple
py_tuple=(1,2,3,4,5)
print(type(py_tuple))
print(py_tuple)

numpy_array_to_tuple=n.array(py_tuple)
print(type(numpy_array_to_tuple))
print(numpy_array_to_tuple)

# shape of numpy array : shape return a tuple of row and column of given list-> .shap ---return--> (given_array_row,given_array_col)
nums=n.array([1,2,3,4,5])
print(nums)
print(nums.shape)# (5,)

two_d_nums=n.array([[0,1,2],[3,4,5],[6,7,8]])
print(two_d_nums)
print(two_d_nums.shape)# (3, 3)

# datatype of numpy array
int_lists=[-3,-2,-1,0,1,2,3]
int_array=n.array(int_lists)
flot_array=n.array(int_lists,dtype=float)
print(int_array)
print(int_array.dtype)
print(flot_array)
print(flot_array.dtype)

# size of numpy array
numpy_array_from_list=n.array([1,2,3,4,5])
two_d_lst=n.array([[0,1,2],[3,4,5],[6,7,8]])
print(numpy_array_from_list.size)
print(two_d_lst.size)

# mathmetical operation using numpy

# addition
numpy_array_from_list=n.array([1,2,3,4,5])
print(numpy_array_from_list)
add_with_original=numpy_array_from_list+10
print(add_with_original)

# substraction
numpy_array_from_list=n.array([1,2,3,4,5])
print(numpy_array_from_list)
substract_with_original=numpy_array_from_list-5
print(substract_with_original)

# multiplication
numpy_array_from_list=n.array([1,2,3,4,5])
print(numpy_array_from_list)
multiply_with_original=numpy_array_from_list*5
print(multiply_with_original)

# division
numpy_array_from_list=n.array([1,2,3,4,5])
print(numpy_array_from_list)
div_with_original=numpy_array_from_list/10
print(div_with_original)

# module
numpy_array_from_list=n.array([1,2,3,4,5])
print(numpy_array_from_list)
module_with_original=numpy_array_from_list%3
print(module_with_original)

# floor division
numpy_array_from_list=n.array([1,2,3,4,5])
print(numpy_array_from_list)
floordiv_with_original=numpy_array_from_list//10
print(floordiv_with_original)

# exponential
numpy_array_from_list=n.array([1,2,3,4,5])
print(numpy_array_from_list)
exponent_with_original=numpy_array_from_list**2
print(exponent_with_original)

# checking datatype by "dtype"
numpy_int_arr=n.array([1,2,3,4])
numpy_float_arr=n.array([1.1,2.1,3.1])
numpy_bool_arr=n.array([-3,-2,-1,0,1,2,3,4] ,dtype="bool")
print(numpy_int_arr.dtype)# int64
print(numpy_float_arr.dtype)# float64
print(numpy_bool_arr.dtype)# bool

# converting types
#    int to float
numpy_int_arr=n.array([1,2,3,4],dtype="float")
print(numpy_int_arr) #[1. 2. 3. 4.]

#    float to int
numpy_float_arr=n.array([1.1,2.2,3.1,4.1],dtype="int")
print(numpy_float_arr)# [1 2 3 4]

#    int to bool   
numpy_int_arr=n.array([-3,-2,-1,0,1,2,3,4] ,dtype="bool")
print(numpy_int_arr)# [ True  True  True False  True  True  True  True]

#     int to string
numpy_arr=n.array([1,2,3,4],dtype="float")
print(numpy_arr.astype("int").astype("str"))# ['1' '2' '3' '4']


# MULTIDIMENTIONAL ARRAY
two_d_array=n.array([(1,2,3),(4,5,6),(7,8,9)])
print(type(two_d_array))
print(two_d_array.shape)
print(two_d_array.size)
print(two_d_array.dtype)

print()

# getting items from numpy array
two_d_array=n.array([(1,2,3),(4,5,6),(7,8,9)])
first_row=two_d_array[0]
second_row=two_d_array[1]
third_row=two_d_array[2]
print(first_row)
print(second_row)
print(third_row)

print()

two_d_array=n.array([(1,2,3),(4,5,6),(7,8,9)])
first_col=two_d_array[:,0]
second_col=two_d_array[:,1]
third_col=two_d_array[:,2]
print(first_col)
print(second_col)
print(third_col)

print()

# slicing of numpy array
two_d_array=n.array([(1,2,3),(4,5,6),(7,8,9)])
first_two_row_and_first_two_col=two_d_array[0:2,0:2]
print(first_two_row_and_first_two_col)

print()

# reverse the row and whole array
two_d_array=n.array([(1,2,3),(4,5,6),(7,8,9)])
print(two_d_array[::])

print()

# reverse row and col position
two_d_array=n.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_d_array[::-1,::-1])

print()

# how to represent assign value
two_d_array=n.array([(1,2,3),(4,5,6),(7,8,9)])
print(two_d_array)
two_d_array[1,1]=55
two_d_array[1,2]=44
print(two_d_array)
# [[ 1  2  3]
#  [ 4 55 44]
#  [ 7  8  9]]

print()

# numpy zeros
# numpy.zeroes(shape,dtype=.order=)
numpy_zeroes=n.zeros((3,3),dtype=int,order="C")
print(numpy_zeroes)

print()

numpy_zeroes=n.zeros((3,3),dtype=int,order="F")
print(numpy_zeroes)

print()

# numpy ones
numpy_zeroes=n.ones((3,3),dtype=int,order="C")
print(numpy_zeroes)

print()

numpy_ones=n.ones((3,3),dtype=int,order="F")
print(numpy_ones)

print()

twos_arr=numpy_ones*2
print(twos_arr)

# reshape
# numpy.reshape(shape,order).numpy.flatten()

print()

first_shape=n.array([(1,2,3),(4,5,6)])
print(first_shape)

print()

reshaped=first_shape.reshape(3,2)
print(reshaped)

print()

flattened=reshaped.flatten()
print(flattened)

print()

# horizontal stack
np_lst_1=n.array([1,2,3])
np_lst_2=n.array([4,5,6])
print(np_lst_1+np_lst_2)
print(n.hstack((np_lst_1,np_lst_2)))
print()

# vertical stack
print(n.vstack((np_lst_1,np_lst_2)))

print()

# generating random number

#   generating  a random float number
random_float=n.random.random()
print(random_float)

#   one random num between [0,1)
one_random_num=n.random.random()
one_random_in=n.random
print(one_random_num)
print(one_random_in)

print()

random_float=n.random.random(5)
print(random_float)

print()

#   generating integer  between 0 to range
random_int=n.random.randint(0,11)# 0-10
print(random_int)

print()
#   generating a random integer between 2 and 11 , and creating a one row array
random_int=n.random.randint(2,11,size=4)
print(random_int)

print()

# generating a random integer between 0 - 10 array
random_int=n.random.randint(2,11,size=(3,3))
print(random_int)

#  a random num between [0,1) size 2,3
r=n.random.random(size=[2,3])
print(r)

print()

# generating random number

#   n.random.normal(mu,sigma,size)
normal_array=n.random.normal(79,15,80)
print(normal_array)

# choice
print(n.random.choice(["a","e","i","o","u"],size=1))
print(n.random.choice(["a","e","i","o","u"],size=10))

# random num between [0,1] shape 2
rand1=n.random.rand(2,2)
print(rand1)

rand2=n.random.randn(2,2)
print(rand2)

# random integer between [0,10) of shape 2,5
rand_int=n.random.randint(0,10,size=[5,3])
print(rand_int)

# numpy and statistics
#pip install matplotlib seaborn
import matplotlib.pyplot as plt
import seaborn as sns
print(sns.set())
print(plt.hist(normal_array,color="grey",bins=50))

print()

# matrix in numpy
four_by_four_matrix=n.matrix(n.ones((4,4),dtype="float"))
print(four_by_four_matrix)

n.asarray(four_by_four_matrix)[2]=2
print(four_by_four_matrix)

# numpy.arange()
lst =range(0,11,2)
print(lst)
for l in lst:
    print(l)

# similar to frange arange numpy.arange(start,stop,step)
whole_num=n.arange(0,11,2)
print(whole_num)

#  natural number
natural_num=n.arange(1,11,1)
print(natural_num)

#  odd number
odd_num=n.arange(1,11,2)
print(odd_num)

# creating sequencce of number using linespace
# linespace()
# it instancely  create 10 value from 1-5 evenly spaced
print(n.linspace(1.0,5.0,num=10))
# not to include the last value in interval
print(n.linspace(1.0,5.0,num=5,endpoint=False))

# logspace:
# it return even spaced numbers on a log scale.logspace has the same parameter as n.linespace
# syntax : n.logspace(start,stop,num,endpoint)
print(n.logspace(2,4.0,num=4))

# check the size of an array in complex term
x=n.array([1,2,3],dtype=n.complex128)
print(x)# [1.+0.j 2.+0.j 3.+0.j]

# item size
print(x.itemsize)# 16

# indexing and slicing of array in python
np_lst=n.array([(1,2,3),(4,5,6)])
print(np_lst)

print("first row",np_lst[0])
print("second_row",np_lst[1])
print("first col",np_lst[:,0])
print("second_col",np_lst[:,1])
print("third _col",np_lst[:,2])

# numpy statestical function
np_normal_dis=n.random.normal(5,0.5,100)
print(np_normal_dis)
print(two_d_array.min())
print(two_d_array.max())
print(two_d_array.mean())
print(two_d_array.std())

print()

print(two_d_array)
print("col with minimum",n.amin(two_d_array,axis=0))
print("col with maximum",n.amax(two_d_array,axis=0))
print("row with minimum",n.amin(two_d_array,axis=1))
print("row with maximum",n.amax(two_d_array,axis=1))

# how to create repeating sequences
a=[1,2,3]
  # repeat whole of "a" two times
print(n.tile(a,2))# [1 2 3 1 2 3]
  # repeat each element of "a" two time
print(n.repeat(a,2))# [1 1 2 2 3 3]

from scipy import stats
np_normal_dis=n.random.normal(5,0.5,100)
print(np_normal_dis)
print(n.min(np_normal_dis))
print(n.max(np_normal_dis))
print(n.mean(np_normal_dis))
print(n.std(np_normal_dis))
plt.hist(np_normal_dis,color="grey",bins=21)
print(plt.show())

# linear algebra
  # dot product: dot product of 2 array
f=n.array([1,2,3])
g=n.array([4,5,6])
print(n.dot(f,g))

# numpy matrix multiplication with np.matmul()
h=[[1,2],[2,3]]
i=[[4,5],[6,7]]
print(n.matmul(h,i))

print()
print(n.linalg.det(i))# Compute the determinant of an array.

Z=n.zeros((8,8))
Z[1::2,::2]= 1
Z[::2,1::2]=1
print(Z)

new_lst=[x *2 for x in range(0,11)]
print(new_lst)


np_arr=n.array(range(0,11))
print(np_arr+2)

# use linear equation for quantities which have linear relationship
temp=n.array([1,2,3,4,5])
pressure=temp*2+5
print(pressure)
plt.plot(temp,pressure)
plt.xlabel("Temperature in oC")
plt.ylabel("pressure in atm")
plt.title("Temperature v/s pressure")
plt.xticks(n.arange(0,6,step=0.5))
plt.show()


mu=28         # mu=mean
sigma=15      # sigma =standard deviation  
samples=100000
x=n.random.normal(mu,sigma,samples)
ax=sns.displot(x);
ax.set(xlabel="x",ylabel="y")
plt.show()