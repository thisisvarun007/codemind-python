t=int(input())
for i in range(t):
    a=int(input())
    res=[]
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    for j in range(1,len(arr)):
        if arr[j] not in res:
            res.append(arr[j])
    for j in range(1,len(brr)):
        if brr[j] not in res:
            res.append(arr[j])
    if len(res)>=a:
        print("YES")
    else:
        print("NO")