'''
theief cant be rob in consequitve gold in houses

in: [13,9,4,10,5,7]
out:
 30
'''
def findmax(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return max(l)
    le=l[0]+findmax(l[2:])
    ri=l[1]+findmax(l[3:])
    return max(le,ri)
l=list(map(int,input().split()))
print(findmax(l))