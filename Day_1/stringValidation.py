'''
password should be upper lower digits special 8len
ip:
'''
s="ab"
upper,lower,digits,special,=1,1,1,1
if 8-len(s)>4:
        print(8-len(s))
else:
    for i in s:
        if i.isalpha() and i.isupper():
            upper=0
        elif i.isalpha() and i.islower():
            lower=0
        elif not i.isalnum():
            special=0
        elif i.isdigit():
            digits=0
    sum=upper+lower+digits+special
    if sum>0:
        print(sum)
    else:
        print(-1)
