#1)Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

maximo = 100

for i in range (101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("Ingrese un número: "))
cant_digitos = len(str(numero))

if numero < 0:
    cant_digitos = cant_digitos - 1 #Le resto 1 para no contar el signo negativo, que la función len() cuenta

if cant_digitos == 1:
    print(f"El número que ingresaste, {numero}, tiene {cant_digitos} dígito.")
else:
    print(f"El número que ingresaste, {numero}, tiene {cant_digitos} dígitos.")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

primer_valor = int(input("Ingrese el primer valor: "))
segundo_valor = int(input("Ingrese el segundo valor: "))
suma = 0

if primer_valor < segundo_valor:
    for i in range ((primer_valor + 1), segundo_valor):  #sumo 1 al primer_valor para no contarlo
        suma = suma + i
else:
    for i in range((primer_valor - 1), segundo_valor, -1): #resto 1 al primer_valor para no contarlo
        suma = suma + i

print(f"La suma de los valores tiene un resultado de {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma = 0
control = True

while control:
    numero = int(input("Ingrese un número: "))
    print(numero)
    suma = suma + numero
    if numero == 0:
        control = False

print(f"El acumulado es {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_aleatorio = random.randint(0,9)
print(f"PARA CONTROLAR, EL NUMERO ALEATORIO ES {num_aleatorio}")

intentos = 0
control = True

while control:
    num_usuario = int(input("Ingresá un número entre 0 y 9: "))
    if num_usuario < 0 or num_usuario > 9:
        print("ERROR, no cumpliste. No ingresaste un número entre 0 y 9.")
        continue #salto todo lo que sigue y vuelvo al while para pedir otro número. No se suma como intento.
    intentos += 1 #si el número cumplió con las condiciones, sumo un intento.
    if num_usuario == num_aleatorio:
        control = False #apago el control para cortar el bucle.
    else:
        print("No adivinaste. Ingresá otro número.")

print(f"¡Muy bien! Adivinaste el número, lo hiciste en {intentos} intentos :)")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for i in range (98, 0, -2): #pongo 98 para no contar el 100
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

#El ej no especifica, pero incluyo en la suma el valor que ingresa el usuarip

tope = int(input("Ingresá un número mayor a 0: "))
suma = 0

if tope >= 0: #si es mayor a 0, voy de forma ascendente
    for i in range(0, (tope + 1)):
        suma += i
else:
    for i in range(0, (tope - 1), -1): #si es menor a 0, agrego -1 como tercer valor para ir de forma descendente
        suma += i

print(f"La suma de los números entre 0 y el número ingresado es {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

tope = 100 #Para probarlo, cambiar "tope" a 10.
control = True
cont_par = 0
cont_impar = 0
cont_neg = 0
cont_pos = 0

while control:
    numero = int(input("Debes ingresar un total de 100 números. Ingresá un número: "))
    print(f"Ingresaste {numero}")

    tope -= 1
    if numero % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
    if numero >= 0:
        cont_pos += 1
    else:
        cont_neg += 1
    
    if tope <= 0:
        control = False


print("-----------------------------")
print(f"Cantidad de números pares: {cont_par}")
print(f"Cantidad de números impares: {cont_impar}")
print(f"Cantidad de números positivos: {cont_pos}")
print(f"Cantidad de números negativos: {cont_neg}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

tope = 100
contador = 0
suma = 0

while contador < tope:
    numero = int(input("Debes ingresar un total de 100 números. Ingresá un número: "))
    print(f"Ingresaste {numero}")
    contador += 1
    suma += numero

media = suma / tope

print(f"La media de los valores ingresados es {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingresá un número: "))
invertido = 0
print(f"Ingresaste {numero}")

while numero > 0:
    ult_digito = numero % 10
    invertido = invertido * 10 + ult_digito #multiplico por 10 el número invertido para correr los dígitos en
    numero = numero // 10                   #cada vuelta hacia la izquierda

print(f"El número invertido es {invertido}")




