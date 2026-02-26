s = input()
i = 0 
lista_s = ["h", "e", "l", "l", "o"]
j = 0

for i in range(len(s)):
    if s[i] == lista_s[j]:
        j += 1
        if j == 5:
            break

if j == 5:
    print("YES")
else:
    print("NO")
