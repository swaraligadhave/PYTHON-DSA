# program to find out the largest,smallest , second largest and second smallest no. from array
arr = [10,12,32,77,86,21,9,30,45]
max=min=arr[0]
smax=smin=arr[0]
for num in arr:
    if num>max:
        smax=max
        max=num
    elif(num > smax and num!=max):
        smax = num 

    if num<min:
        smin=min
        min = num

    elif(num<smin and num!=min):
        smin = num

print("Max is :",max)
print("Min is :",min)
print("Second Max is :",smax)
print("Second Min is :",smin)



