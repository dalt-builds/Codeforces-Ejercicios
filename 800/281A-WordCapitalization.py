palabra = input()

if palabra[0].islower:
    print(palabra[0].upper()+palabra[1:])
else:
    print(palabra)
