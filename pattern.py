patterns:

n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=" ")
    print()


n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()



n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print('*',end=" ")
    print()





n=int(input('enter a number'))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,n+1):
        print('*',end=" ")
    print()



def pattern(n):
    for i in range(0,n):
        for k in range(n,i,-1):
            print(" ",end=" ")
        for j in range(0,n):
            print('*',end=" ")
        print()
n=int(input('enter a number'))
pattern(n)


n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 or i==n or j==1 or j==n):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()



n=int(input('enter a number'))
for i in range(1,n+1):
    for k in range(n-i,0,-1):
        print(' ',end=" ")
    for j in range(1,n+1):
        if (i==1 or i==n or j==1 or j==n):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()

n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(65,65+n):
        print(chr(j),end=" ")
    print()



n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(n-i,0,-1):
        print('*',end=" ")
    print()
