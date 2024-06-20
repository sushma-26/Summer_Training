'''
find missing number
'''
a=[0,1,2,4,5,6]
n=len(a)
p=n*(n+1)//2
s=sum(a)
print(p,s,"==",(p-s))

