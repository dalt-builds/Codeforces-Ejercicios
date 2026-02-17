n, k = list(map(int, input().split()))
puntos = list(map(int, input().split()))
participante_k = puntos[k-1]
contador = 0

for i in range(n):
    if puntos[i] >= participante_k and puntos[i] > 0:
        contador += 1
print(contador)