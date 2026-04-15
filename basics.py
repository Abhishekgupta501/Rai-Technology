# name=input("enter your name: ")
# age=int(input("enter your age: "))      
# print("your name is: ",name)
# print("your age is: ",age)
# print("your name is: ",name,"and your age is: ",age)




# Class_Student=["Chandan","Satvik","Aman"]
# Class_Student[0]="Chandan Kumar"
# print(Class_Student[0])
# print("the students in the class are: ",Class_Student)
# print(len(Class_Student))                 #total number of element nikaal sakte hai list me 
# reversed_Class_Student=Class_Student[::-1]
# print("the students in the class in reverse order are: ",reversed_Class_Student)


# --------------------------------------------------------------------------------
a=[1,2,3,4,5]
b=a
a=a+[4]
# a.append(4)

print(b)
print(a)


# --------------------------------------------------------------------------------

# age=16
# if age>=18 or "student":
#     print("you are eligible to vote")
# else:  
#      print("you are not eligible to vote")


# -----------------------------------------------------------------------------


# string is immutable in python, so we cannot change the value of string but we can change the value of list because list is mutable
# food="pizza"
# food=food.replace("z","s")   # replace method does not change the original string because string is immutable
# print(food)

# ----------------------------------------------------------------------------------


# if 10 ==10.0:                  # isme 10 aur 10.0 dono same value hai but data type different hai, isliye ye condition true hoga
#     print("the value is equal") 
# else:    print("the value is not equal")


#---------------------------------------------------------------------------------
# x=[10,20,30,40,50]
# x.extend([60,70,80])   # extend method adds the elements of the list to the end of the list and increases the length of the list by the number of elements added
# print(len(x))   # append method adds the element at the end of the list and increases the length of the list by 1
# append method adds the element at the end of the list and increases the length of the list by 1
# extend method adds the elements of the list to the end of the list and increases the length of the list by the number of elements added

#---------------------------------------------------------------------------------

# x=5
# if x>3:
#     if x<5:
#         print ("Messi")
#     elif x==5:
#         pass #pass statement is used to skip the execution of the block of code, it does nothing and is used as a placeholder for future code basically koi output nahi deta
#     else:
#         print("Neymar")
# else:
#     print("Mbappe")