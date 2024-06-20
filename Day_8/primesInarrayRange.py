'''
in: given a list of non prime numbers
l[4,8,14,22,36,68]
from range 4,8 find largest prime and add to next range 8,14....
7 4,8
13 8,14
19 14,22
31 22,36
67 36,68
add everything and print

'''
def isprime(n):
    if n==1 or n==2:
        return 1
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return 1
def greatPrime(a,b):
    for i in range(b-1,a,-1):#b+1 is becoz given elements in array are not prime
        if isprime(i):
            return i
    return 0
l=[14,16,20,22]
n=len(l)
s=0
for i in range(n-1):
    s+=greatPrime(l[i],l[i+1])
print(s)