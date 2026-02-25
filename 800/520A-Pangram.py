n = int(input())
palabra = input()

if len(set(palabra.lower())) == 26:
    print("YES")
else:
    print("NO")


