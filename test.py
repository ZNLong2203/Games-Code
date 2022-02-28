import sys
input = lambda:sys.stdin.readline().rstrip("\r\n")

dp=[[0]*20]*200001
for i in range(200001):
    check,idx=i,0
    while check:
        dp[i][idx]+=(check%2)
        idx+=1
        check>>=1
    for j in range(20):
        dp[i][j]+=dp[i-1][j]
def solve():
    l,r=map(int,input().split())
    high=0
    for i in range(20):
        high = max(high,dp[r][i]-dp[l-1][i])
    printf(r-l+1-high)
def main():
    tcs=1
    tcs=int(input())
    for tc in range(tcs):
        solve()
