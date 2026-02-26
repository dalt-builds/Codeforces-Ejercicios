n = int(input())

for i in range(n):
    a, b = list(map(int, input().split()))

    if a % b !=0 and a > b:
        numero_magico = (a+b) // b
        numero_magico = (b * numero_magico) - a
        print(numero_magico)
    elif a < b:
        numero_magico = b-a
        print(numero_magico)
    else:
        print(0)
