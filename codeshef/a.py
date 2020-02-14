t=int(input())
for i in range(t):
    p,q,r,s=map(int,input().split())
    if p>=q+r+s:
        print(1)
    elif p<q+r+s and p>=q+r :
        print(2)
    elif p<q+r+s and p>=r+s:
        print(2)
    else:
        print(3)