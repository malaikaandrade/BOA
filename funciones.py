import math

def mi_funcion():
	print("Hola mundo")

mi_funcion()



def suma(a, b):
	resultado = a + b
	print('La suma de a + b es: ', resultado)
	return resultado
	
suma(248,16)



"""
el *datos significa que
la función espere una lista fija de parámetros, 
pero que éstos, en vez de estar disponibles de forma separada, 
se encuentren contenidos en una lista o tupla. 
En este caso, el signo asterisco (*) deberá preceder al nombre de la lista o tupla que es pasada
como parámetro durante la llamada a la función:
"""

def sumacuadrados(*datos):
	total = 0
	for d in datos:
		total = total + d**2
		print('la suma de cuadrados es: ',total)

	return total

sumacuadrados(4,5,6)


def calcular(importe, descuento):
	return importe - (importe * descuento/100)

datos = [1500, 10]
print ('Originalmente cuesta $1500 ya con el descuento del 10% le queda en: ', calcular(*datos))

"""
El mismo caso puede darse cuando los valores a ser pasados como parámetros a una función,
se encuentren disponibles en un diccionario. 
Aquí, deberán pasarse a la función, precedidos de dos asteriscos (**):
"""

def promocion(importe, descuento):
	return importe - (importe * descuento/100)

datos = {'descuento': 70, 'importe': 2999.99}
print ('Originalmente cuesta $2999.99 ya con el descuento del 30% le queda en: ',promocion(**datos))


#Funciones anonimas/lambda son aquellas que se definen sin que sea necesario declararlas
#las funciones normales se define con la palabra resevervada def y las anonimas se definen con la palabra lambdaLambda
cuadrado = lambda x: x**2
#las lambdas tambien se la pondemos asignarselas a una variable

print('El cuadrado de x es: ',cuadrado(8))


doble = lambda x: x*2

print(doble(2))


from functools import reduce

data = [1,2,3,4,5,6,7,8,9,10]


"""
MAP()

La función map() en Python aplica una función a cada uno de los elementos de una lista.
Por ejemplo, para que a partir de una lista de enteros se obtenga una nueva lista 
con el cuadrado de cada uno de ellos 

transforma los datos originales en otros a se a por operaciones aritmetcas o por otra cosa
"""
mapped_data = list(map(lambda x: x*2, data))

print(mapped_data)

enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))

print(cuadrados)

"""
FILTER()

La función filter() filtra una lista de elementos para los que una función devuelve True.
por ejemplo, si le pedimos que solo multipliqu los numeros *2 si dan true a ser mayores que 8


"""
filtered_data = list(filter(lambda x: (x*2>8), data))

print(filtered_data)


"""
REDUCE()

Esta función se utiliza principalmente para llevar a cabo un cálculo acumulativo sobre una
lista de valores y devolver el resultado.

acumula los datos en listas 
"""

reduced_data = reduce(lambda x, y: x+y, data)
print(reduced_data)