# sum using for loop
# n = int(input("Enter any number : "))  #printing sum of total number using for loop
# total = 0
# for i in range(1,n+1):
#     total += i
# print(total)

# n = int(input("Enter any number: "))    #printing sum of total number using while loop 
# total = 0
# i = 0
# while i <= n:
#     total += i
#     i+= 1
# print(total)

# n = input("Enter any number :")   #printing total sum of numbers in given number
# total = 0
# # a = 0
# for i in range(0,len(n)):
#     total += int(n[i])
# print(total)

# a = input("Enter your name : ")
# temp_var = ""
# for i in range(0,len(a)):
#     if a[i] not in temp_var:
#         print(f"{a[i]} : {a.count(a[i])}")
#         temp_var += a[i]

#break and continue keyword
#break keyword :=>
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
#continue keyword :=>
# n = int(input("Enter any number :"))
# for i in range(1,n+1):
#     if i == 6:
#         continue
#     print(i)

#exercise
# import random
# b = random.randint(1, 100)
# guess = 1
# a = int(input("Enter any number: "))
# game_over = False
# while not game_over:
#     if a == b:
#         print(f"you win, you guessed this {guess} times")
#         game_over = True
#     else:
#         if a < b:
#             print("too low")
#             guess += 1
#             a = int(input("Guess again :"))
#         else:
#             print("too high")
#             guess += 1
#             a = int(input("Guess again :"))

# import random
# b = random.randint(1, 100)
# guess = 1
# a = int(input("Enter any number: "))
# game_over = False
# while not game_over:
#     if a == b:
#         print(f"you win, you guessed this {guess} times")
#         game_over = True
#     else:
#         if a < b:
#             print("too low")
#         else:
#             print("too high")

#         guess += 1
#         a = int(input("Guess again :"))      DRY principle :=> don't repleat Yourself

# step argument is range funtion
# for i in range(0,11,2):        # 2 is for step arguemnt 
#     print(i)                 
# for i in range(10,0,-1):
#     print(i)

#for loops and string in python
# name = "Chandan"
# for i in range(len(name)):
#     print(name[i])

# name = "Chandan"
# for i in name:            #mostly used in python
#     print(i)

# num = input("Enter any number: ")
# total = 0
# for i in num:
#     total += int(i)
# print(total)