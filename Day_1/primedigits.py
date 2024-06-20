c=0
n=7566
while(n):
    if n%10 in [2,3,5,7]:
        c+=1
    n=n//10
print(c)