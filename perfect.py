perfect number
n=int(input('enter a number'))#6
sum=0
a=n
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
if sum==a:
    print(a,'is a perfect number')
else:
    print(a,'is not a perfect number')

n=int(input('enter a number'))
sum=0
a=n
i=1
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if sum==a:
    print(a,'is a perfect number')
else:
    print(a,'is not a perfect number')
