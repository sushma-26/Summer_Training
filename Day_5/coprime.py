'''
in: 2 numbers
check weather they are coprimes
'''
n=13
m=14
if n>m:
    l=m
else:
    l=n
l=l//2
for i in range(2,l+1):
    if n%i==0 and m%i==0:
        print("not coprime")
        break
else:
    print("coprime")
