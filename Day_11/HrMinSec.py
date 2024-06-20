'''
ip:7262
op:2h:1m:2

ip:500
op:0h:8m:20
'''
n=int(input())
s=n//3600
n-=s*3600
m=n//60
n=n-(m*60)
print(s,':h   ',m,':m  ',n,':s')
