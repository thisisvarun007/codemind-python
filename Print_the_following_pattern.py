a=int(input())
temp=a
for i in range(a):
    for j in range(a):
        if i==j:
            print(temp,end=" ")
        elif i+j==a-1:
            print(temp,end=" ")
        else:
            print("",end=" ")
    temp-=1
    print(""),