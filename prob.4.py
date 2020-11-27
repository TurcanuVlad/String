a=str(input("Un sir de caractere: "))
b=str(input("Un sir de caractere: "))
c=str(input("Un sir de caractere: "))
d=str(input("Un sir de caractere: "))
s=''
if (len(a) > 2) and (len(b) > 2) and (len(c) > 2) and (len(d) > 2):
    s=a[:2] + b[:1] + c[:3] + d[:len(d) // 2]
else:
    print("Siruri incorecte, refaceti!")
print(s)