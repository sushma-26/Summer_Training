'''
next prime num from input
'''
'''f=0
n=int(input())
for i in range(2,int(n/2)):
    if n % i ==0:
        f=1
        break
if(f==1):
    while(True):
        n=n+1
        f=0
        for i in range(2,int(n/2)):
            if n % i ==0:
                f=1
                break
        if(f==0):
            print(n)
            break
else:
    print("prime",n)
'''
n=int(input())
while(True):
    f=0
    for i in range(2,int(n/2)):
        if n % i ==0:
            f=1
            break
    if(f==0):
        print(n)
        break
    else:
        n=n+1