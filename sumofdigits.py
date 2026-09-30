num=int(input("Enter digits: "))
sum = 0
n = num

while(n>0):
    sum = sum+(num%10)
    num = num//10

print("Sum of digits:",sum)

