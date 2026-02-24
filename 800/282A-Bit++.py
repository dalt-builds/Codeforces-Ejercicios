x = 0
n = int(input())


for i in range(n):
    operacion = input()
    if operacion == "++X" or operacion == "X++":
        x += 1
    else:
        x -= 1
print(x)