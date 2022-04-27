t=int(input())
for k in range(t):
    n,a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    f=0
    for i in range(n):
        if arr[i]+a==brr[i] or brr[i]-b==arr[i]:
            f=1
        else:
            f=0
            break
    if f==1:
        print("Yes")
    else:
        print("No")