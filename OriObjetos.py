class Perro:

#molde de obejetos
	def __init__(self, nombre, raza, color, edad):

		self.nombre = nombre
		self.raza = raza
		self.color = color
		self.edad = edad
		self.otro = otra_persona

#metodos
	def saludar(self):

		print('Hola {nombre}, cómo estás? '.format(nombre=self.nombre))

	def saludar_a_otra_persona(self):
		print('Hola {nombre}! muy bien y tú {otro} ? '.format(nombre=self.nombre, otro=self.otra_persona.nombre))

#OBJETOS
Lua = Perro('Lua', 'chihuahua', 'beige', 3)
Lazaro = Perro('Lazaro', 'labrador', 'miel', 5)

"""
Lua.saludar()
Lazaro.saludar_a_otra_persona()
"""

Lua.saludar_a_otra_persona(Lazaro)
Lazaro.saludar_a_otra_persona(Lua)