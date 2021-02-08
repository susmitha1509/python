fibonacci series
n=int(input('enter a range'))
a=0
b=1
print(a,b,end=" ")
for i in range(3,n+1):
    s=a+b
    print(s,end=" ")
    a=b
    b=s
    

n=int(input('enter a range'))
a=0
b=1
print(a,b,end=" ")
count=3
while(count<=n):
    s=a+b
    print(s,end=" ")
    a=b
    b=s
    count+=1



