t=int(input())
for tt in range(t):
    x,y=map(int,input().split())
    d=abs(x-y)
    if x==y:
        print(0)
    elif x>y:
        print(d)
    else:
        if d%2==0:
            print(d//2)
        else:
            print((d//2)+2)
