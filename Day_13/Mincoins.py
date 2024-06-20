'''
ip:[1,2,3,5]
 rs=15
 op:3 
'''
l=[1,3,4,5]
rs=17
d=[0]*(rs+1)
dp=[]
n=len(l)
for i in range(n+1):
    dp.append(d)
for i in range(rs+1):
    dp[0][i]=i//l[0]
for i in range(1,n):
    for j in range(1,rs+1):
        if l[i]>j:
            dp[i][j]=dp[i-1][j]
        elif l[i]<=j:
            dp[i][j]=min(dp[i][j-l[i]]+1,dp[i-1][j])
print(dp)
print(dp[n-1][rs-1])
print(dp[i][j])

