'''
in:
khoor
3
then go three steps back then you get
hello
'''
s=input()
n=int(input())
n=n%26
r=[]
for i in s:
    s = ord(i) - n
    if s < ord('a'):
        s += 26
        r.append(chr(s))
    else:
        r.append(chr(s)) 
print(''.join(r))