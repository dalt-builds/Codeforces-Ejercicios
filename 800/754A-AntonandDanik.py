n = int(input())
letras = list(input())
contadorA = 0
contadorD = 0

for i in range(n):
    if letras[i] == "A":
        contadorA += 1
    elif letras[i] == "D":
        contadorD += 1

if contadorA > contadorD:
    print("Anton")
elif contadorD > contadorA:
    print("Danik")
elif contadorD == contadorA:
    print("Friendship")