x=[1,2,3,4,5,6,7,8,9,10]   #list me ham ek se ja ke numbers daal diye hai
i=0
while i < len(x):       
    if x[i] % 2 == 0:  #loop ke andar if condition lagayi hai ki agar x[i] ka remainder 2 se 0 aata hai to wo even number hai
        print(x[i])
    else:        pass
    i += 1
