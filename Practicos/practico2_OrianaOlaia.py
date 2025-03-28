#### TRABAJO PRACTICO 2 ####
### Ejercicio 1 ###
palabra = "Mordor"
pal1 = palabra[1]
pal2 = palabra[3]
print(pal1,pal2)

### Ejercicio 2 ###
frase = input("Ingrese una frase: ")
letra = frase[0]
print(letra.upper())

### Ejercicio 3 ###
frase1 = input("Ingrese una frase: ")
if len(frase1) > 5:
    print("Los primeros tres caracteres son: ", frase1[:3])
else:
    print("Debe tener más de 5 caracteres")

### Ejercicio 4 ###
listas = ["Chocolate", "Huevos", "Manteca", "Crema de leche", "Frutilas"]
for lista in listas:
    print(lista)
    
listas[-1] = "Canela de Polvo"

print("Lista corregida:")
for lista in listas:
    print(lista)

### Ejercicio 5 ###
numero = int(input("Ingrese un numero mayor a 1 y menor a 50: "))
if numero > 1 and numero < 50:
    for i in range(1, numero + 1):
        print(i)
else:
    print("El número debe ser mayor que 1 y menor a 50.")

### Ejercicio 6 ###
