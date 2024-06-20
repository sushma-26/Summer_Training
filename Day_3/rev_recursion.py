def rev(n,s):
    if n == 0:
        return s
    s = s * 10 + (n % 10)
    return rev(n//10, s)

n=123
s=0
print(rev(n,s))
