'''
if num is palidrome print it if not print next nearest palindrome
ip:221
222
ip:2431
2442
ip:122
   131
ip:1234
   1331
ip:24
   33
ip:25642
  25752
'''
n='1234'
s=str(n)
l=len(s)
if l%2!=0:
    f = s[:l//2 + 1]
    l_part = s[(l//2) + 1:]
    x = s[:l//2]
    if int(l_part) >= int(x):
        f = str(int(f) + 1)
        f = f + f[:l//2][::-1]
        print(f)
    else:
        f = f + f[:l//2][::-1]
        print(f)
else:
    f = s[:l//2]
    l_part = s[l//2:]
    if int(f[::-1]) > int(l_part):
        f = f + f[::-1]
        print(f)
    else:
        while True:
            f = str(int(f[-1]) + 1)
            if int(f[::-1]) > int(l_part):
                f = f + f[::-1]
                print(f)
                break


            



