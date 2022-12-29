# tuple data structure 
# tuple can store any data type 
# most important tuples are immutable, once tuple created we can't change 
# data inside tuple

# no append, no insert , no pop , no remove
# days = ('monday', 'tuesday')
# tuple are faster than lists 

# methods 
# count, index
# len funtion
# slicing 

# mixed = (1,2,4,5,6)
# for i in mixed:
#     print(i)


#single tuple can be written in (1,) this form 

#tuple unpacking 
# fruits = 'apple','mango','banana'
# a, b, c = (fruits)
# print(a)

#some funcitons which are used in tuple
# min(), max , sum
# def func(int1, int2):
#     add = int1+int2
#     multiply = int1*int2
#     return add, multiply
# # print(func(2,3))
# add, multiply = func(2,3)
# print(add)
# print(multiply)

# for creating tuple 
# nums = tuple(range(1,11))   it will take the values from 1 to 10
# same for list also 


#dictionaries intro 
#dictionaries are unordered collection of data in key value pair
#how to create dicitionaries  :=> {}
# user = {'name': 'chandan', 'age': 19}
# print(user)
# # or 
# user1 = dict(name = 'chandan' , age= 19)
## print(user1)  both will give same output 

#we can store dictionary inside dictionare
#we can add key values pair
# user_info = {}
# user_info['name'] = 'chandan'
# user_info['age']= 19
# print(user_info),

# user_info = {
#     'name' : 'chandan',
#     'age' : 19,
#     'fav_movie' : ['coco','kimi no na wa'],
# }
# if 'name' in user_info:
#     print('present')
# else:
#     print('none')
# for i in user_info:       #it will give all the key value as output
#     print(i)
# for i in user_info.values():  #it will give values of key as output
#     print(i)

#fromkeys methods
# d = {name : 'unknown', age : 'unknown',}
# d = dict.fromkeys(['name','age','height'], 'unknown')
# a = dict.fromkeys((range(1,11)),'unknown')
# print(d)
# print(a)

#get method (it is very useful)
# d = {'name': 'chandan', 'age': 19}
# print(d.get('nerve'))
# if 'name' in d:
#     print('present')
# else:
#     print('not presnt')

# if d.get('name'):
#     print('yes')
# else:
#     print('no')

# user = {'name': 'chandan', 'age': 19}
# print(user.get('fave', 'notfound'))