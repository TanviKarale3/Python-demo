#To create upper triange pattern
i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1


#To create a Traingle Pattern

for j in range(1,6):
    for k in range(9-j,1,-1):
        print(end=" ")
    for i in range(1,j+1):
        print("*",end=" ")
    print()


#To Craete lower triangular pattern

n=5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()


#To create a diamond

for i in range(1,5):
    for j in range(4-i):
        print(end=" ")
    for j in range(1,i*2):
        print("*",end="")
    print()
for i in range(3,0,-1):
    for j in range(4-i):
        print(end=" ")
    for j in range(1,i*2):
        print("*",end="")
    print()


#To craeate a square 

num=int(input("enter the number of rows and coloumn:"))

for i in range(num):
    for j in range(num):
        if i==0 or i==num-1 or j==0 or j==num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#To create a lower triangle

for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")