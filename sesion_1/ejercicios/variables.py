'''
Es un espacio en memoria en el cual cambiara su valor 
en tiempo de ejecucion, es el nombre que se le asigna a una valor
'''

'''
Tipos de Datos

int -> 15 , float -> 14.5 long 23L

bool -> True , False

str -> "Hola"

list [1,3,5]
tuple = (3,5,65) # inmutables
dict = {'nombre':'Alfredo','activo':True}

'''


# 2 = a # Esto no esta permitido en python
# x + 3 = 5 # Al lado izquierdo no pueden existir operadores

# Forma comun de declarar una variable
a = 1
b = 2
c = a + b

# Asignacion multiple
x,y = 1,2

z = x + y

print(z) # Simple Adicion

# Asignacion Simple
nombre, edad = "Usuario", 22

# Asignacion simple
paterno = "ap_paterno"
materno = "ap_materno"

# imprimir variables por consola
print("Nombre ",  nombre , "Edad:", edad)
# imprimir variables por consola de forma dinamica con la funcion format()
print("Nombre {} mi edad {}".format(nombre,edad))
# imprimir variables por consola de forma dinamica con el paso de parametros %s
print("nombre %s mi edad %s" %(nombre , edad))
# agregando mas campos a la impresion
print("Nombre {} mi edad {} paterno {} materno {}".format(nombre,edad, paterno, materno))

#imprimiendo la variable paterno
print(paterno)

#Eliminando la variable paterno
del paterno


# Try catch lo utilizaremos para silenciar el error de querer imprimir una variable que no existe
try:
	print(paterno)
except Exception:
	print("no Existe")

# Podemos declarar una variable con una _ al comienzo
_paterno = "Volvemos a crear un variable paracida a paterno"
variable1 = 20
variable_numero1 = 10
# 1variable = 12  Declarando de esta forma nos dara un error

# for = 120  Esta prohibido el uso de palabras reservadas

# Python hace diferencias entre variables con minusculas o mayusculas
nombre_paterno_materno = "Juan Garcia Mendez"

NOMBRE_PATERNO_MATERNO = "Juan Garcia Mendez"

print(nombre_paterno_materno.upper())
print(NOMBRE_PATERNO_MATERNO.lower())

# Tipado dinamico 
x = "Curso Python"
print(type(x)) # Imprimimos para saber que tipo de variable es 
x = 24 # Asignamos otro valor a la variable
print(type(x)) # Imprimimos para saber que tipo de variable es 


a = b = 10
print(a,b)
# modificar el valor 
a,b = 2,4
x , y ,z = "Python", 10, True
print(x,y,z)

