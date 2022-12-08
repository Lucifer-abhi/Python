from re import I


n=int(input())
if(1<=n<=1000000):
    for i in range(1,n+1):
        print(i,end=" ")
        if(i==15):
            break