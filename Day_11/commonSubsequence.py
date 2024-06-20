'''
print longest subsequence in 2 strings
'''
s1='abcd'
s2='axbd'
m=[]
n=len(s1)+1
for i in range(n):
    l=[0]*n
    m.append(l)
for i in range(1,n):
    for j in range(1,n):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i-1][j],m[i][j-1])
print(m[len(s1)][len(s2)])
c=''
i=n-1
j=n-1
while i!=0 and j!=0:
        if s1[i-1]==s2[j-1]:
            c+=s1[i-1]
            i=i-1
            j=j-1
        else:
            if m[i][j]==m[i-1][j]:
                i=i-1
            else:
                j=j-1
print(c[::-1])


    
