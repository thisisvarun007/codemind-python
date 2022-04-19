import math
x,y,m=map(int,input().split())
print("{:.0f}".format(math.pow(x,y)%m))