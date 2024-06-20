'''in:
 aaaabbddd
out
 a3b2d3
 #sliding window doesnt go out of range so run less than length
'''
s = input("Enter a string: ")
r = ""
c = 1  

for i in range(len(s)-1):  
    if s[i] == s[i + 1]:
        c += 1
    else:
        r+=s[i] + str(c)
        c = 1  

r+=(s[-1] + str(c))
print(r)


    
    