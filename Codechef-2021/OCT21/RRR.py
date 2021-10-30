t=int(input())
for tt in range(t):
    n,k=map(int,input().split())
    print(2*(n-k+((k-1)//2)))
