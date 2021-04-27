
n,m=map(int,input().split(" "))
map1=[]
minmap=0
for i in range(n):
  a=[int(x) for x in input().split(" ")]
  map1.append(a)
  ans = min(a)
  if ans<minmap:
    minmap=ans

print(minmap)
dp=[[ans-1]*(m+3) for i in range(n+3)]
for i in range(3,n+3):
  for j in range(3,m+3):
    if i==3 and j==3:
      dp[i][j]=map1[i-3][j-3]
    else:
      dp[i][j]=map1[i-3][j-3]+max(dp[i][j-1],dp[i][j-2],dp[i][j-3],dp[i-1][j],dp[i-1][j-1],dp[i-1][j-2],dp[i-2][j],dp[i-2][j-1],dp[i-2][j-2],dp[i-3][j]);
print(dp[-1][-1],dp)



