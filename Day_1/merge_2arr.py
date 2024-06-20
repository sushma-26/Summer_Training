'''
in: 2 5 7 9
    1 3 6 7 10 13
out :
   1 2 3 5 6 7 7 9 10 13
can sort with some len also like c.sort(len=5)** 
'''
#m=list(map(int,input().split()))
left=[2,5,7,9]
right=[1,3,6,7,10,13]
'''c=a1+a2
c.sort()
print(c)'''
i,j=0,0
l=[]
while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        l.append(left[i])
        i += 1
    else:
        l.append(right[j])
        j += 1

while i < len(left):
    l.append(left[i])
    i += 1
#if(i<len(left):
#    l.extend(left[i:])

while j < len(right):
    l.append(right[j])
    j += 1
#if(i<len(right):
#l.extend(right[j:])


print(l)