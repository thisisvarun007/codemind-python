def sd(a):
    su=0
    while a>0:
        rem=a%10
        su+=rem
        a//=10
    return su
a=int(input())
su=sd(a)
if a%su==0:
    print("True")
else:
    print("False")