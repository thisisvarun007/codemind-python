a=int(input())
arr=list(map(int,input().split()))
pro=ma=0
for i in range(a):
    for j in range(a):
        if i!=j:
            pro=(arr[i]-1)*(arr[j]-1)
            if pro>ma:
                ma=pro
print(ma)