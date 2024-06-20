'''
in : 2
 polikujmnhytgbvfredcxswqaz
 they give abcd
 we should return in given alphabetical oder: bdca is answer

'''
n=int(input())
for i in range(n):
    s=input()
    x=input()
    r=''
    for i in range(26):
        if s[i] in x:
            n=x.count(s[i])
            r+=s[i]*n
    print(r)
