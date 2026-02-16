n = int(input())
contador = 0
array=[]

for i in range(n):
    lineas = list(map(int, input().split()))
    array.append(lineas)
    suma = sum(array[i])
    if suma >= 2:
        contador+=1
    
print(contador)
    