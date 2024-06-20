'''
if input=10
from 1 to 10 add all even numbers
'''
def ev(x):
    if x==0:
        return 0
    return x+ev(x-2)
a=int(input())
if a%2==1:
    a=a-1
print(ev(a))
