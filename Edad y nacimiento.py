import os
os.system("cls")

nombre = input("Ingrese el nombre: ")
año = int(input("Ingrese el año de nacimiento: "))
edad = 2024 - año

if edad >=0 and edad <=1:
    observacion="Es un Bebe"
if edad == 2:
    observacion="Es un Infante"
if edad >=3 and edad <=13:
    observacion = "Es un Niño"
if edad >=14 and edad <=17:
    observacion="Es un Adolescente"
if edad >=18:
    observacion="Es un Adulto"

print( f"Nombre: {nombre}")
print( f"Año de Nacimiento: {año}")
print( f"Edad: {edad}")
print(f"Observacion: {observacion}")
