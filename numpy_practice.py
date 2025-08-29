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


# import numpy as np
# arr = np.array([12,13,14,15,16,17])
# print(arr[1::3])                    # 13, 16
# print(arr[::2])                     # 12, 14, 17


# import numpy as np
# a = np.array(['office'])
# newarr = np.array([2])
# print(a.dtype)
# print(newarr.dtype)
# b = np.array(True)
# print(b.dtype)
# c = np.array(1.5j)
# print(c.dtype)


# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# newarr = arr.copy()
# newarr.view()
# print(arr)
# print(newarr)
# newarr[0] = 23
# print(newarr)



# import numpy as np
# arr = np.array([2, 3, 4, 5], ndmin=3)
# a = arr.ndim                                                    # ndmin=  give the dimantation of array
# print(a)
# newarr = np.array([[23,45, 45], [24, 35, 56]], ndmin=4)
# b = newarr.ndim                                              # ndim check the dimantation of array
# print(b)

# import numpy as np
# arr = np.array([2, 3, 4, 5], ndmin=4)
# print(arr.shape)

# import numpy as np 
# arr =  np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.reshape(-1))
# newarr = arr.reshape(-1)
# print(newarr)


# import numpy as np
# arr = np.array([[[[23, 34, 45, 56], [12, 13, 14, 15], [22, 33, 44, 55], [24, 24, 24, 24]]]])
# # for x in arr:
# #     for y in x:
# #         for z in y:
# #             for a in z:
# #                 print(a)
# for x in np.nditer(arr):
#     print(x)


# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#     print(x)





# import numpy as a
# arr = a.array([1, 2, 3, 4, 5])
# for z in a.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#     print(z)





# import numpy as np
# arr = np.array([12, 14, 15, 16])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes='S'):
#     print(x)



# import numpy as np
# arr = np.array([[2,3,4,5], [6, 7, 8, 9]])
# for z in np.nditer(arr[:, :, ]):
#     print(z)




# import numpy as np
# arr = np.array([[[2, 3, 4, 5], [6, 7, 8, 9], [12,23,34,45]]])
# for idx, x in np.ndenumerate(arr):
#     print(idx, x)



# import numpy as np
# #arr1 = np.array([1, 2, 3, 4])
# # arr2 = np.array([5, 6, 7, 8])
# # arr = np.concatenate((arr1, arr2))
# # print(arr)
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# #arr = np.concatenate((arr1, arr2), axis=0)
# #arr = np.stack((arr1, arr2), axis=0)
# arr = np.hstack((arr1, arr2))
# print(arr)


# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr[0])
# print(newarr[3])

# import numpy as np
# arr = np.array([2, 1, 3, 4, 5, 2, 5, 2])
# newarr = np.where(arr == 2)
# print(newarr)



# import numpy as np
# arr = np.array(['hello', 'team', 'office', 'team'])
# newarr = np.where(arr == 'team') 
# print(newarr)


# import numpy as np
# arr = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])
# #newarr = np.where(arr%2 != 0)
# newarr = np.searchsorted(arr, 4, side='right')
# print(newarr)


# import numpy as np
# arr = np.array(['mango', 'orange', 'apple'])
# arr1 = np.array([[23,4,56],[66,7,8]])
# print(np.sort(arr))
# print(np.sort(arr1))


# import numpy as np
# arr = np.array([21, 31, 41, 51])
# x = arr[[True, False, True, True]]
# print(x)



# import numpy as np
# arr = np.array([23, 34, 56,67,5, 8, 34])
# newarr = []
# for element in arr:
#     if element >= 40:
#         newarr.append(True)
#     else:
#         newarr.append(False)
# a = arr[newarr]
# print(arr)
# print(newarr)
# print(a)




# import numpy as np
# arr = np.array([23, 34, 45, 56, 12, 60])
# newarr = []
# for element in arr:
#     if element >= 40:
#         newarr.append(True)
#     else:
#         newarr.append(False)
# anotherarr = arr[newarr]
# print(arr)
# print(newarr)
# print(anotherarr)



# import numpy 
# arr = numpy.array([23, 45, 6])
# newarr = arr > 40
# a = arr[newarr]
# print(a)



import numpy as np
arr = np.array([23, 5, 6, 8, 90, 45])
arr_fillter = arr%2 == 0
a = arr[arr_fillter]
print(a)