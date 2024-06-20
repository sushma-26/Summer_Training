'''
timings:[(1,3)(2,5)(4,6)(6,7)(5,8)(7,9)]
money:[5,6,5,4,11,2]
output:17 highest paid job with given schedule
'''
l=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
m=[5,    6,     5,     4,    11,   2]
'''l=[(1,3),(2,5),(3,10),(4,6),(6,9)]
m=[20,    20,     100,     70,    60]'''
mc=m.copy()
n=len(l)
for i in range(1,n):
    for j in range(0,i):
        if l[i][0]>=l[j][1]:
            if mc[i]<mc[j]+m[i]:
                mc[i]=mc[j]+m[i]
print(max(mc))
