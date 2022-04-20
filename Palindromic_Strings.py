def reverse(a):
    return a[::-1]
t=int(input())
for k in range(t):
    a=input()
    b=input()
    if a+b==reverse(a+b):
        print("YES")
    elif b+a==reverse(b+a):
        print("YES")
    else:
        print("NO")