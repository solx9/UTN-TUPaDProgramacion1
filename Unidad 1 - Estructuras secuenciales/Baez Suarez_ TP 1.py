#EJERCICIO 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#EJERCICIO 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingresá tu nombre: ")
print(f"Hola {nombre}!")

#EJERCICIO 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#EJERCICIO 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

pi = 3.14
radio = float(input("Ingrese el radio del círculo: "))

area = pi * (radio ** 2)
perimetro = 2 * pi * radio

print(f"El área del círculo es {area}")
print(f"El perímetro del círculo es {perimetro}")

#EJERCICIO 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print (f"{segundos} equivalen a {horas} horas")

#EJERCICIO 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

num = int(input("Ingrese el número: "))
tabla1 = num * 1
tabla2 = num * 2
tabla3 = num * 3
tabla4 = num * 4
tabla5 = num * 5
tabla6 = num * 6
tabla7 = num * 7
tabla8 = num * 8
tabla9 = num * 9
tabla10 = num * 10

print(f"La tabla del 1 al 10 del número {num} es la siguiente: ")
print(tabla1)
print(tabla2)
print(tabla3)
print(tabla4)
print(tabla5)
print(tabla6)
print(tabla7)
print(tabla8)
print(tabla9)
print(tabla10)

#EJERCICIO 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingresá un número entero (distinto de 0): "))
num2 = int(input("Ingresá otro número entero (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f"El resultado de la suma entre ambos números es {suma}")
print(f"El resultado de la resta entre ambos números es {resta}")
print(f"El resultado de la multiplicación entre ambos números es {mult}")
print(f"El resultado de la división entre ambos números es {div}")

#EJERCICIO 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo: IMC = peso en kg / (altura en metros) ** 2

altura = float(input("Ingresá tu altura en metros. Separá los decimales con un punto: "))
peso = float(input("Ingresá tu peso en KG: "))
imc = peso / (altura ** 2)

print(f"Tu indice de masa corporal es {imc}")

#EJERCICIO 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# temp en farenheit = 9/5 * temp en celsius + 32

tempcelsius = float(input("Ingresá una temperatura en Celsius: "))

tempfarenheit = 9/5 * tempcelsius + 32

print(f"La temperatura {tempcelsius} equivale a {tempfarenheit} grados Farenheit")

#EJERCICIO 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

print("Ingrese 3 números para calcular el promedio.")
num1 = int(input("Ingrese el 1er número: "))
num2 = int(input("Ingrese el 2do número: "))
num3 = int(input("Ingrese el 3er número: "))
promedio = (num1 + num2 + num3) / 3

print("El promedio entre los 3 números es", promedio)

