import math
from math import sqrt

while True:

	print("************************Calculadora de funcionalidades**************************")
	print('*********Menú***********')

	print('Selecciona una opción')

	print('1. Tu número es positivo o no')
	print('2. Tu número esta entre en rango de -5 y 5')
	print('3. División')
	print('4. Cuadrado perfecto')
	print('5. Año bisiesto')
	print('6. Salir')


	eleccion = int(input('opción: '))

	
	
	if eleccion == 1:
		num1 = int(input("Ingresa un número real: "))
		if num1 > 0:
			print("El número " + str(num1) + " es real y positivo")
		else:
			print("El número " + str(num1) + " es real y negativo")


	if eleccion == 2:
		num = int(input("Ingresa un número: "))
		if num >-5 and num <5:
			print("El número " + str(num) + " esta en el rango entre -5 y 5")
		else:
			print("El número " + str(num) + " no esta en el rango entre -5 y 5")

	if eleccion == 3:
		num3 = int(input("Ingresa un número: "))
		num4 = int(input("Ingresa un número: "))
		print('La division entre los dos numeros es: ', num3/num4)

	if eleccion == 4:
		cua = int(input('Ingresa un número: '))
		raiz = math.sqrt(cua)
		print('La raiz cuadrada de tu numero es:',raiz)

	if eleccion == 5:

		bisiesto = int(input('Ingresa un número: '))
		if (bisiesto % 4 == 0) and (bisiesto % 100 != 0) or (bisiesto % 400 == 0):
			print('El año ' + str(bisiesto) + ' es un año bisiesto')
		else:
			print('El año ' + str(bisiesto) + ' no es un año bisiesto')


	elif eleccion == 6:
		print("Hasta luego!!")
		break

	else:
		print("Digite otra opción: ")




