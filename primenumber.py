program to check whether the number is prime or not(1 and the given num are factors of given num so we exclude 1 and the given num)
n=int(input('enter a number'))
for i in range(2,n):
    if n%i==0:
        print(n,'is not a prime number')
        break
else:
    print(n,'is  a prime number')
