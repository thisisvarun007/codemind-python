a,b=map(int,input().split())
arr=list(map(int,input().split()))
p=0
for i in arr:
    if i+b<=5:
        p+=1
print(p//3)