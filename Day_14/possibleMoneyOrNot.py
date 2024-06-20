l=[2,3,5,6]
ll=len(l)
rs=7
s=0
d=[0]*(rs+1)
dp=[]
for i in range(ll+1):
    dp.append(d)
for i in range(ll+1):
    dp[i][0]=1
for i in range(1,ll+1):
    for j in range(1,rs+1):
        if dp[i-1][j]==1:
            dp[i][j]=dp[i-1][j]
        elif l[i-1]<=j:
            dp[i][j]=dp[i][j-l[i-1]]
        elif l[i-1]>j:
            dp[i][j]=dp[i-1][j]
print(dp)
if dp[-1][-1]==1:
    print("yes")
else:
    print("no")        
