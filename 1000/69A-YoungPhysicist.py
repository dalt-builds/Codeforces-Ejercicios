n = int(input())
sx = 0
sy = 0
sz = 0

for i in range(n):
    x, y, z =  list(map(int, input().split()))
    sx += x
    sy += y
    sz += z

if sx == sy == sz == 0:
    print("YES") 
else:
    print("NO")

    