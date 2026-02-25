palabra = input()
palabra = palabra.lower()
palabra_nueva = ""

for i in range(len(palabra)):
    if palabra[i] not in "aeyuoi":
        palabra_nueva += "."
        palabra_nueva += palabra[i]

print(palabra_nueva)