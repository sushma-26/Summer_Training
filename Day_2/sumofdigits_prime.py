'''
add digits in number to get single digit and check if it is prime or not
m='4232'
n=sum(list(map(int,m)))
print(sum of digits='n')


def single(m):
    while m >= 10:
        sum = 0
        while m > 0:
            sum += m % 10
            m //= 10
        m = sum
    return m

def is_prime(n):
    if n in [2, 3, 5, 7]:
        return True
    else:
        return False

def next_prime(m):
    while True:
        sum1 = single(m)
        if is_prime(sum1):
            return m
        m += 1
'''
def single(m):
    while m >= 10:
        sum = 0
        while m > 0:
            sum += m % 10
            m //= 10
        m = sum
    return m

def is_prime(x,n):
    if n in [2, 3, 5, 7]:
        return x
    else:
        return x+1
    
m = int(input())
while True:
    sum1=m
    if m>10:
        sum1 = single(m)
    r=is_prime(m,sum1)
    if r==m:
        print(r)
        break
    else:
        m=r
