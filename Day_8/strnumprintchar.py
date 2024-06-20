'''ip:
"hello:5438,car:214,book:8799,apple:2199"
op:oaxp===len(str)in number print a[len(a)] if not there next num in number print that one if nothing available then print x
s=list(map(int,'21345'))
print(s)
[2, 1, 3, 4, 5]'''
s=input().split(",")
x=[]
for i in s:
    x.append(i.split(':'))
print(x)
s=''
for i in x:
    r=i[0]
    n=len(r)
    if str(n) in i[1]:
        s+=r[-1]
    else:
        while n>=0:
            n=n-1
            if str(n) in i[1]:
                s+=r[n-1]
                break
        else:
            s+='x'
print(s)

