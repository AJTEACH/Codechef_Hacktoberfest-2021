t=int(input())
for tt in range(t):
    a=list(map(int,input().split()))
    x=0
    y=0
    for i in a:
        if i==0:
            x+=1
            y+=1
        elif i==1:
            x+=2
        else:
            y+=2
    if x==y:
        print("DRAW")
    elif x>y:
        print("INDIA")
    else:
        print("ENGLAND")
