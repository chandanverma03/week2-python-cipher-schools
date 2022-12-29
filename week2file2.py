#default parameter
# a = input("Enter Your First Name : ")
# b = input("Enter Your Last Name :")
# c = int(input("Enter Your age :"))
# def user_info(first_name, last_name, age = None):
#     print(f"Your full name is {first_name} {last_name}")
#     print(f"Your age is {age} ")
# user_info(a,b,c)

# we can only make last paramter default    None, 'Unknow'

# Scope 
# x = 5            #global variable
# def func():
#     global x
#     x = 7
#     return x
# print(x)
# print(func())

#list :=> we can store anything in lists int, float,string
#how to add items in lists
#most common thing that you can do with you list

# fruits = ['apple','graphes']
# fruits.append('mango')   #append add items at the last in the list
# print(fruits)

# fruits = []
# fruits.append('mango')
# fruits.append('apple')
# print(fruits)

#more methods to add data in the list
# fruits = ['mango','oranges','apple']
# fruits.insert(1, 'lichi')
# print(fruits)

# a = ['graphes', 'apple']  #how to add(contatinate ) two lists
# b = ['carrot', 'onion']
# vegetables = a + b
# print(vegetables)

# a = ['graphes', 'apple']
# b = ['carrot', 'onion']
# a.extend(b)
# print(a)
# print(b)

#how to delete data from the list
# fruits=['orange','apple','banana','grapes']
# fruits.pop()  #which data we want to remove just add the number of that list
# print(fruits)

# for adding data in list we use append , extend , insert
# for removing data in list we use pop , remove , delete

#in keyword with list
# fruits=['orange','apple','banana','grapes']
# if 'apple' in fruits:
#     print("Aplle is present in list")
# else:
#     print("not present")

# fruits=['orange','apple','banana','grapes']
# print(fruits.count('apple'))
# fruits=['orange','apple','banana','grapes']
# fruits.sort()
# print(fruits)

# num = [1,2,3,5,6,9,3,21,2]
# num.sort()
# print(num)

# num = [1,2,3,5,6,9,3,21,2]
# print(sorted(num))

# num = [1,2,3,5,6,9,3,21,2]
# num.clear()
# print(num)

# num = [1,2,3,5,6,9,3,21,2]
# numbers = num.copy()
# print(numbers)

# num = [1,2,3,5,6,9,3,21,2]
# fruits=['orange','apple','banana','grapes']
# fruit=['orange','apple','banana','grapes']
# print(fruits == fruit)
# print(fruits is fruit)
 
#split method  :=> convert string to list
# user_info = "chandan,18".split(",")
# print(user_info)
# user_info = ['chandan', '24']
# print(','.join(user_info))      #converting list into string


# list vs string
# list are mutable(Changeable) and string are inmutable(non changeable)

#loops in lists
# fruits=['orange','apple','banana','grapes']
# for i in fruits:
#     print(i)

# fruits=['orange','apple','banana','grapes']
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i = i+1

#list inside list
# matrix = [[1,2,3], [4,5,6], [7,8,9]]  #3 items  list inside list is 2d list
# for i in matrix:
#     for a in i:
#         print(a)

# s = 'string'
# print(type(s))
# num = list(range(1,10))  #generate list with range functions
# print(num)
# num = list(range(1,11))
# num.pop()
# print(num)
#for fining the element from the list we use insert funtion
# num = [1,2,3,4,5,6,3,1,2,5,3,7,8]
# # print(num.index(3, 3))
# def func(l):           #for printing negative values of the list
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative
# print(func(num))

# def func(l):              #for printing the square of the lists items
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square
# l = list(range(1,11))
# print(func(l))

# def reverse_list(l):  #for reversing the string
#     l.reverse()
#     return l
# l = list(range(1,11))
# print(reverse_list(l))

# def reverse_list(l):    #another method for reversing the list 
#     r_list = []
#     for i in range(len(l)):
#         popped_items=l.pop()
#         r_list.append(popped_items)
#     return r_list
# l = list(range(1,11))
# print(reverse_list(l))

# def reverse_elements(l):     #for reversing the elements in the string
#     elements = []
#     for i in l:
#         elements.append(i[::-1])
#     return elements
# words = ['abc','kri','cha']
# print(reverse_elements(words))

# def odd_even(l):
#     listss = []
#     lst = []
#     for i in l:
#         if i%2 == 0:
#             listss.append(i)
        
            

# import datetime
# a=datetime.datetime.now()
# print("Current date and time : ")
# print(a.strtime("%Y-%m-%d %H:%M:%S"))
# import datetime
# a = datetime.datetime.now()
# print ("Current date and time : ")
# print (a.strftime("%Y-%m-%d %H:%M:%S"))

# def odd_even_seperate(l):
#     odd_nums = []
#     even_nums = []
#     for i in l:
#         if i % 2 == 0:
#             even_nums.append(i)
#         else:
#             odd_nums.append(i)
#         output = [odd_nums, even_nums]         #or we can directly write 
#     return output                                  #return [odd_nums, even_nums]
# nums = [1,2,3,4,5,6,7]
# print(odd_even_seperate(nums))

# def common_ele(l1, l2):               #finding common elements in list
#     output = []
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output
# print(common_ele([1,3,6,7,4], [1,3,4,2]))

# min and max functions
# numbers = [6,30,4]
# print(min(numbers))
# print(max(numbers))
# def greatest_diff(l):
#     return max(l)-min(l)
# print(greatest_diff(numbers))

# def funtion_list(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count 
# l = [1,2,3,[1,2],[1,3,4]]
# print(funtion_list(l))
    














