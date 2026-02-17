n = int(input())
colores =  input()
contador = 0

for i in range(n):
    if colores[-i-1] == colores[n-i-2] and n-i-2 >=0 :
        contador += 1
print(contador)

