# Operadores aritmeticos en python

a = 10
b = 2

# a = a + 5 para simplicar esta operacion podemos realizarlo de la siguiente manera:
a += 5

print(a) # imprimimos el resultado


''' 
	Equivalencias 
	a += b	------------ a = a + b
	a -= b	------------ a = a - b
	a *= b	------------ a = a * b
	a /= b	------------ a = a / b
	a **= b	------------ a = a ** b
	a //= b	------------ a = a // b
	a %= b	------------ a = a % b
'''

a = 20
b = 3

print("Suma ", a + b) # Suma
print("Resta ", a - b) # Resta
print("Multiplicacion", a * b) # Multiplicacion
print("Division", a / b) # Division
print("Division Entera ", a // b )# Division Entera
print("Modulo ", a % b )# Modulo
print("Exponencial ", a ** b) # Exponencial


# Tipos de datos Numericos

x = 4
_x = int(x)
_xl = long(x)
_xf = float(x)
_complejo = (4, .2)

print(type(x))
print(type(_x))
print(type(_xl))
print(type(_xf))
print(type(_complejo))


'''
== , evalua como verdadero si 2 variables son iguales
!= ,evalua como verdadero si 2 variables son diferentes
<> , lo mismo que !=
> , verdadero si el operador a la izquierda es mayor que el de la derecha
< , verdadero si el operador a la izquierda es menor que el de la derecha
>= verdadero si el operador a la izquierda es mayor o igual al de la derecha
<= verdadero si el operador a la izquierda es menor o igual al de la derecha
'''


print(5<10)
print(5>=10)
print(144!=5)
print("Python" == "python")