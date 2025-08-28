# import numpy as np
# print(np.__version__)



# import numpy
# arr = numpy.array([1,2,3,4,5,6,7])
# print(arr)




# import numpy as np
# arr = np.array(["done", "deo", 'alise', 23, 34])
# print(arr)
# print(type(arr))

# import numpy as np
# arr = np.array(('alish', 32, 35))
# print(arr)
# print(type(arr))



# import numpy as np
# arr = np.array([[['alise', 'office', 'team'], [123, 456, 789], ['jone', 'deo', 'alise'],[1,2,3]]])
# print(arr)


# import numpy as np
# a = np.array((2))
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[123, 123], [456, 456]])
# d = np.array([[[123, 123, 123], [123, 123, 123]], [[123, 123, 124], [123, 123, 123]]])
# print(a)
# print(b)
# print(c)
# print(d)
# print(np.ndim(d))




# import numpy as np
# arr = np.array([[[123, 123], [1234, 1234]], [[12345, 12345], [123, 123]]])
# print(arr[0, 0, 0])





# import numpy as np                                     
# arr = np.array([[123, 123], [1234, 12345]])             
# arrr = np.array([123], ndmin=3)                           # using ndimn= we can give the dimentation of array
# print(arr)
# print(np.ndim(arr))                                       # using ndim() we can cheke the dimentation of array
# print(arrr)


# import numpy as np 
# arr = np.array([[[123, 123, 123], [456, 456, 456]], [[789, 789, 789], [135, 135, 135]]])
# print(arr)
# print(type(arr))
# print(np.ndim(arr))
# newarr = np.array([1, 2, 3], ndmin=2)
# print(newarr[0])



# import numpy as np
# arr = np.array([[11 ,22, 33, 44], [55, 66, 77, 88]])      #  how to print 2d array 
# print(np.ndim(arr))
# print(arr[0,2])


import numpy as np
arr = np.array([12,13,14,15,16,17])
print(arr[1::3])                    # 13, 16
print(arr[::2])                     # 12, 14, 17