user = input()
SinRepetirLetras = ""

for letra in user:
    if letra not in SinRepetirLetras:
        SinRepetirLetras += letra

if len(SinRepetirLetras) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")


