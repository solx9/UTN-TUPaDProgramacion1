#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingresá tu edad: "))

if edad >= 18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = float(input("Ingresá tu nota: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un número: "))
par = False

if numero % 2 == 0:
    par = True
else:
    pass

if par:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a.")
elif (edad >= 12) and (edad < 18):
    print("Adolescente.")
elif (edad >= 18) and (edad < 30):
    print("Adulto/a joven.")
else:
    print("Adulto/a.")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contra = input("Ingrese su contraseña, debe tener entre 8 y 14 caracteres: ")
long_contra = len(contra)

if (long_contra >= 8) and (long_contra <= 14):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y 
# las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

mode_na = mode(numeros_aleatorios)
median_na = median(numeros_aleatorios)
mean_na = mean(numeros_aleatorios)

if (mean_na > median_na) and (median_na > mode_na):
    print("Hay sesgo positivo.")
elif (mean_na < median_na) and (median_na < mode_na):
    print("Hay sesgo negativo.") 
elif (mean_na == median_na == mode_na):
    print("Sin sesgo.")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

texto = str(input("Ingrese una frase o palabra: ")).lower()
ultletra = texto[-1] #guarda el ultimo caracter de la palabra

if (ultletra == "a") or (ultletra == "e") or (ultletra == "i") or (ultletra == "o") or (ultletra == "u"):
    print(texto + "!")
else:
    print(texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str(input("Ingrese su nombre: "))
opcion = int(input("Ingrese una opción (1, 2 o 3)"))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:
#● Desde el 21 de diciembre hasta el 20 de marzo (incluidos). Estación en el hemisferio norte INVIERNO. Estación en el
#hemisferio sur VERANO
#● Desde el 21 de marzo hasta el 20 de junio (incluidos). Estación en el hemisferio norte PRIMAVERA. Estación en el
#hemisferio sur OTOÑO
#● Desde el 21 de junio hasta el 20 de septiembre (incluidos). Estación en el hemisferio norte VERANO. Estación en el
#hemisferio sur INVIERNO
#● Desde el 21 de septiembre hasta el 20 de diciembre (incluidos). Estación en el hemisferio norte OTOÑO. Estación en el
#hemisferio sur PRIMAVERA

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = str(input("Ingrese en qué hemisferio se encuentra (N/S)")).upper()
mes = int(input("Ingrese el mes (1 al 12): "))
dia = int(input("Ingrese el día (1 al 31): "))

if hemisferio == "N":
    if (mes == 7) or (mes == 8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        print("Es verano.")
    elif (mes == 10) or (mes == 11) or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
        print("Es otoño.")
    elif (mes == 4) or (mes == 5) or (mes == 3 and dia > 20) or (mes == 6 and dia <= 20):
        print("Es primavera.")
    else:
        print("Es invierno.")

if hemisferio == "S":
    if (mes == 7) or (mes == 8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
        print("Es invierno.")
    elif (mes == 10) or (mes == 11) or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
        print("Es primavera.")
    elif (mes == 4) or (mes == 5) or (mes == 3 and dia > 20) or (mes == 6 and dia <= 20):
        print("Es otoño.")
    else:
        print("Es verano.")

