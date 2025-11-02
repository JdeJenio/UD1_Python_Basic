# Leer datos del usuario
a = int(input("Introducir valor de A: "))
b = int(input("Introducir valor de B: "))

# Solución 1: con variable auxiliar
aux = a
a = b
b = aux

# Solución 2: sin variable auxiliar (sólo para enteros)
a = a + b
b = a - b
a = a - b

# Mostrar resultados
print(f"El valor de A es {a}")
print(f"El valor de B es {b}")
