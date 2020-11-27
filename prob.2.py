n = str(input("Sir de caractere= "))
a=0
b=0
c=0
for i in range (0, len(n)):
    if 90 >= ord(n[i]) >= 65:
        a += 1
    if 57 >= ord(n[i]) >= 48:
        b += 1
    if((ord(n[i])>=33)and(ord(n[i])<=47))or((ord(n[i])>=58)and(ord(n[i])<=64))or((ord(n[i])>=91)and(ord(n[i])<=96))or((ord(n[i])>=123)and(ord(n[i])<=127)):
            c += 1
print(f'Numarul de litere majuscule este', a)
print(f'Numarul de cifre este', b)
print(f'Numarul de caractere speciale este', c)