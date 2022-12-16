#string 
# collection of characters inside single quotes or double quotes

# first_name = "Chandan "
# last_name = "Verma"
# full_name = first_name + last_name
# print(full_name)

# we can't add string with any number 
# print(first_naem + 3)  error
# print(first_name + "3")  no error
# print(first_name+ str(3)) no error


#user input 
# for taking input from user we can use input funtion

# name = input("Enter Your name :")
# print("Hello "+ name)

# input always take user's input in  the form of string

# number_one = int(input("Enter first number :"))
# number_two = float(input("Enter second number :"))
# total = number_one + number_two
# print("Total of two number is :"+ str(total))

# number1 = int(4)
# number2 = float(3)
# number3 = int(4)
# total = number1 + number2 + number3
# print(total)

# variables in python
# name , age = "Chandan" , 18
# print("Hello " + name + " your age is " + str(age))

# two or more in one line in python
# name, age = input("enter your name and age ").split("_")  (_seperated by that symbol which is inside the funtion split)
# print(name)
# print(age)

# # string formatting 
# name= "chandan"
# age = 24
# # print("hello {} Your age is {}".format(name,age))
# print(f"hello {name} your age is {age}")
# {} => is known as place holder

# exersice question 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = a+b+c
# g = d/3
# print(f"Total sum of given three number is {d} and average numbers is {g}")

#string indexing

# language = "python"
# print(language[2])
#  indexing start from 0 (starting)
#  indexing start from end to (-1)

#slicing /selecting sub sequences
# lang = "python"
# print(lang[-3:6])     #syntax => [start argument : stor argument]

#step argument 
# print("Chandan"[0:5:2])  #how much you want to give 

#exercise
# a = input("Enter Your name: ")
# print(a[-1::-1])

#string methods

# len() it count the total no. of elements in the string
# name ="Chandan verma"
# print(len(name))
#lower() method => it converts all the letters of the string into lowre
# print(name.lower())
#upper() it converts all the letters into upper case
#title() method it covert first letter of the string into the capital leter and other letters into small
#count() method it count the specific letter in the string 
# print(name.count('a'))

#exercise

# name, single_Character = input("Enter Your name and a single character (seperate by comma)").split(",")
# print(name)
# print(single_Character)
# print(f"total letters in your name is {len(name)}")
# print(f"{single_Character} character repeats in your name {name.count(single_Character)} times")

#strip method 
# lstrip() is used for removing left space
# name = "      chandan       "
# dots = ".............."
# print(name+dots)
# print(name.lstrip()+dots)
# print(name.rstrip()+dots)  #used for removing space from right
# print(name.strip()+dots)    # used for removing space from both sides
# print(name.replace(" ","")+dots) #" " that element which we want to replace and after that we have to 
#                                      # write ""in that format which we replace by new element

#find and replace method in python 
# string = "she is beautiful and she is good dancer"
# print(string.replace(" ","_"))
# print(string.replace("is","was"))
# print(string.replace("is","was",1))
# print(string.find("is"))

#center method in python
# name = "chandan"
# print(name.center(13,'*'))

# name = input("Enter your name: ")
# print(name.center(len(name)+8, "*"))

#strings are immutable: We can't change the string(in python)

# name = "chand"
# name = name + "an"  #name += (we can also use it if we want to plus anything )
# print(name)

# age = 45
# age += 3
# print(age)








