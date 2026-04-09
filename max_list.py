#TO find the maximum number in the list
x=[10,20,50,40,30,100]
max=x[0]
i=0
while i < len(x):
    if x[i] > max:
        max = x[i]
    i += 1
print("the maximum number in the list is: ",max)
