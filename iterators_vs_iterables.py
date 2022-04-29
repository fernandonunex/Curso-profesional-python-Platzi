# 1. Both iterables and iterators can be iterated using for loop.
# Code from https://medium.com/analytics-vidhya/iterable-vs-iterator-in-python-eda1295a815e

# l1 = [1, 2, 3, 4, 5]
# l2 = iter(l1)
# print(l2)  # Output:<list_iterator object at 0x0164E658>
# # Iterating through iterable(l1) using for loop.
# for i in l1:
#     print(i, end=" ")  # Output:1 2 3 4 5

# print(" ")

# # Iterating through iterator(l2) using for loop.
# for i in l2:
#     print(i, end=" ")  # Output:1 2 3 4 5

# 2. Iterables supports only iter() function.But iterators supports both iter() and next() function.

# l1 = [1,2,3]
# print(dir(l1))
# l2 = iter(l1)
# print(dir(l2))

# 3.Iterators are also iterables.

# l1=[1,2,3,4,5]
# returns an iterator

# l2=iter(l1)
# print (l2)#Output:<list_iterator object at 0x00EAE658>

# #calling  iter() function on iterator itself.
# l3=iter(l2)
# print (l3)#Output:<list_iterator object at 0x00EAE658>

# print (l2==l3)#Output:True

# Data types that support iterators

# _________________________Strings______________________________

# a="Welcome to Python"
# #Converting string(iterable) to iterator using iter() function
# b=iter(a)
# print (b)#Output:<str_iterator object at 0x0084E658>
# print (type(b))#Output:<class 'str_iterator'>


# #Applying next() over the iterator.
# #Returns one element at a time.
# print (next(b))#Output:w
# print (next(b))#Output:e

# ___________________________List_______________________________________
# a=[1,2,3,4,5]
# #Converting iterable(list) to iterator object using iter() function
# b=iter(a)
# print (b)#Output:<list_iterator object at 0x00C8E658>
# print (type(b))#Output:<class 'list_iterator'>

# #Applying next() over the iterator.
# #Returns one element at a time.
# print (next(b))#Output:1
# print (next(b))#Output:2

# ____________________________Tuple_______________________________________
# a = (1, 2, 3, 4, 5)
# # Converting tuple(iterable) into iterator object using iter() function.
# b = iter(a)
# print(b)  # Output:<tuple_iterator object at 0x015DE610>
# print(type(b))  # Output:<class 'tuple_iterator'>


# # Applying next() over the iterator.
# # Returns one element at a time.
# print(next(b))  # Output:1
# print(next(b))  # Output:2

# ________________________________dictionary_________________________________
# a={'a':1,'b':2,'c':3}
# #Converting dictionary(iterable) into iterator object using iter() function.
# b=iter(a)
# print (b)#Output:<dict_keyiterator object at 0x005F3BE0>
# print (type(b))#Output:<class 'dict_keyiterator'>


# #Applying next() over the iterator.
# #Returns one element(key) at a time.
# #loops over the keys in the dictionary
# print (next(b))#Output:a
# print (next(b))#Output:b

# ________________________________iterators to tuple or dic_____________________
l1=[1,2,3,4,5]
#Converting to iterator object
l2=iter(l1)
#Converting iterator(l2) to tuple using tuple() constructor
t1=tuple(l2)
print (t1)#Output:(1, 2, 3, 4, 5)

t2 = tuple(l1)
print(t2)


d1=[(1,'a'),(2,'b'),(3,'c')]
#Converting to itertaor object
d2=iter(d1)
#Converting iterator(d2) to dictionary using dict() constructor.
d3=dict(d2)
print (d3)#Output:{1: 'a', 2: 'b', 3: 'c'}