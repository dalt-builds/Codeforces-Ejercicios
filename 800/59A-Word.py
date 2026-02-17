n = list(input())
contador_mayuscula = 0
contador_minuscula = 0

for i in range(len(n)):
    if n[i].isupper():
        contador_mayuscula +=1 
    else:
        contador_minuscula += 1

if contador_mayuscula > contador_minuscula:
    print("".join(n).upper())
else:
    print("".join(n).lower())
