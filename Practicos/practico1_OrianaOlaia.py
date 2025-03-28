import random
import math
##### TRABAJO PRACTICO 1 #####

### Ejercicio 1 ###
print("hola mundo")

### Ejercicio 2 ###

n = 4

print(n)

### Ejercicio 3 ###

a = 7
##   print(A)   #no ocurre nada, solo va a salir un error de que esa variable no está declarada y no existe, no tiene valor guardado#

### Ejercicio 4 ###
a = 1
b = 2
n = 3
x = 4
y = 5

#a)#
print("a/ ",(5+a)+(10+b))
#b)#
print("b/ ", b^2)
#c)#
print("c/ ", (2.n)-1/(2.n)+1)
#d)#
print("d/ ", 1 . math.sqrt(n))
#e)#
print("e/ ", (2.x)-y)
#f)#
print("f/ ", (x-y)/(x+y))


### Ejercicio 5 ###
repetir = input("Ingresa una palabra: ")
print("Palabra ingresada: ", repetir)

### Ejercicio 6 ###
a = int(input("Ingrese el primer numero:"))
b = int(input("Ingrese el segundo numero:"))
print("Se ingresaron los valores ",a," y ",b)

### Ejercicio 7 ###
nu = int(input("INgrese un valor numerico:"))
print(nu + 1)

### Ejercicio 8 ###
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
print("Suma: ", num1 + num2)
print("Resta: ", num1 - num2)
print("Multiplicacion: ", num1 * num2)
print("División: ", num1 / num2)

### Ejercicio 9 ###
real1 = float(input("Ingrese un valor real: "))
real2 = float(input("Ingrese otro valor real: "))
resultado = real1 / real2
print("Resultado de los dos valores reales: ", real1, " + ", real2, " = ", resultado )

### Ejercicio 10 ###
palabra = input("Ingrese una palabra: ")
print("La palabra ingresada tiene: ",len(palabra))

### Ejercicio 11 ###
c = input("Ingrese el primer valor: ")
d = input("Ingrese el segundo valor: ")

if c == d:
    print("Son iguales")

### Ejercicio 12 ###

if c == d:
    print("Son iguales")
else:
    print("No son iguales")

### Ejercicio 13 ###
e = int(input("Ingrese el primer numero"))
f = int(input("Ingrese el segundo numero"))

if e > f:
    print("el valor mayor es: ", e)
else:
    print("el valor mayor es: ", f)

### Ejercicio 14 ###
usd = int(input("Ingrese el monto de dolares: "))
resu = (usd*1063)/4
print("Resultado del monto en pesos argentinos: ", resu)

### Ejercicio 15 ###
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
if n1 > n2:
    print(n1)
elif n1 < n2:
    print(n2)
else:
    print("Los numeros son iguales")

### Ejercicio 16 ###
nreal = float(input("Ingrese un numero real: "))
if nreal >= 0:
    print("Es mayor o igual")
else:
    print("Es menor")

### Ejercicio 17 ###
pal1 = input("Ingrese la primera palabra: ")
pal2 = input("INgrese la segunda palabra: ")
palabra1 = len(pal1)
palabra2 = len(pal2)

if palabra1 == palabra2:
    print("Tiene la misma longitud")
elif palabra1 > palabra2:
    print("La primera palabra tiene más longitud")
else:
    print("La segunda palabra tiene más longitud")

### Ejercicio 18 ###
numer = int(input("Ingrese un numero: "))
if numer > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")

### Ejercicio 19 ###
ne1 = input("Ingresa un numero: ")
ne2 = input("Ingresa otro numero: ")
nument = [ne1, ne2]
nument.sort()
print("Ordenando los numeros de menor a mayor", nument)

### Ejercicio 20 ###
dado = [1, 2, 3, 4, 5, 6]
dado.sort()
print("El resultado de la tirada de dado es: ", dado)

### Ejercicio 21 ###

numran = random(1,100)
if numran > 50:
    print("Es mayor de 50")
elif numran == 50:
    print("Es igual a 50")
else:
    print("Es menor de 50")

### Ejercicio 22 ###
realran = random.uniform(0.0, 1.0)
if realran < 0.5:
    print("El numero real obtenido menor")
else:
    print("El numero real no es menor")

### Ejercicio 23 ###
dadito = [1,2,3,4,5,6]
dadito.sort()
adivinar = int(input("Adivina que resultado va a salir el dado: "))
if adivinar == dadito:
    print("ADIVINASTE!")
else:
    print("Que mal, no adivinaste el numero correcto, salió: ", dadito)

### Ejercicio 24 ###
numero = 57
numero = numero % 2
if numero > 0:
    print("El numero es impar")
else:
    print("El numero es par")

### Ejercicio 25 ###

numero = int(input("Ingresa cualquier numero: "))
numero = numero % 2
if numero > 0:
    print("El numero es impar")
else:
    print("El numero es par")