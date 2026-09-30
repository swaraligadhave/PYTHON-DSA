#program to print pattern reverse
n = int(input("Enter the value of n:"))
for i in range(n,0,-1):
    for j in range (i,0,-1):
        print(j,end=" ")
    print()

