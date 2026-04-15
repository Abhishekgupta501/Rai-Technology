# x=10
# y="Nityashree"
# z="Arati"
# print(x)
# print(y)
# print(z)
#--------------------------------------------------
#what is the variable?
# x,y,z- 3 variables
# ----------------------------------------------
z=[10, "Nityashree", "Arati"]  # list is a collection of different data types
print(z[2])
# what is 2 in z[2]?
# 2 is the index of the element "Arati" in the list z. In python, the index of the first element in a list is 0, so the index of "Arati" is 2 because it is the third element in the list.
#0 is starting index
print(z[1])

#list is mutable in python, so we can change the value of list but we cannot change the value of string because string is immutable
#this is the advantage of list that we can store different data types in a list but in tuple we cannot store different data types because tuple is immutable and list is mutable

# a=[1,2,3,4,5]
# a[0]=10
# print(a)
# list is mutable in python, so we can change the value of list but we cannot change the value of string because string is immutable

a=(1,2,3,4,5)
a(0)=10
print(a)