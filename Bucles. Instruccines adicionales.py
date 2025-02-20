email = input("Dame tu correo: ")

for i in email:
    if email=="@":
        arroba = True
        break
else:
    arroba = False
print(arroba)