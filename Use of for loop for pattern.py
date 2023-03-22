for j in range(1,6):
    for i in range(1,11):
        print(i,end=" ")
    print()



for j in range(1,6):
    for i in range(5,0,-1):
        print(i,end=" ")
    print()



for j in range(1,6):
    for i in range(1,6):
        print(i,end=" ")
    print()


for j in range(1,6):
    for i in range(5,j-1,-1):
        print(i,end=" ")
    print()


for j in range(5,0,-1):
    for i in range(1,j+1):
        print(j,end=" ")
    print()


n=int(input("Enter the number of rows:"))

for i in range(n):
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()


n=5
for i in range(n):
    for j in range(i):
        print(' ',end=" ")
    for j in range(i,n):
        if(i%2==0):
            print('Z',end=' ')
        else:
            print('0',end=' ')
    print()


s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(s[p],end=' ')
    p+=1
    print()


s="Yash"
n=len(s)
for i in range(n):
    p=0
    for j in range(i+1):
        print(s[p],end='')
        p+=1
    print()