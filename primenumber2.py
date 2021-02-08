program to print prime number in a given range
a=int(input('enter starting range'))
b=int(input('enter ending range'))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,'is  a prime number')

        
##program to print before prime number
a=int(input('enter a starting range'))      
for j in range(a-1,1,-1):#4
    for i in range(2,j):
        if j%i==0:
            break
    else:
        print(j,end=" ")
        break


program to print after prime number
a=int(input('enter a starting range'))
k=a
while True:
    for i in range(2,k):
        if(k%i==0):
            break
    else:
        print(k,end=" ")
        break
    k+=1

nearest prime
a=int(input('enter a starting range'))
for j in range(a-1,1,-1):#4
    for i in range(2,j):
        if j%i==0:
            break
    else:
        bp=j
        print(j)
        break
    
k=a
for k in range(a+1,100000):
    for i in range(2,k):
        if(k%i==0):
            break
    else:
        ap=k
        print(k)
        break
    k+=1

if (abs(a-ap)>abs(a-bp)):
    print('nearest prime is ',bp)
elif (abs(a-ap)==abs(a-bp)):
    print('nearest prime is ',ap,bp)
else:
    print('nearest prime is',ap)
        
