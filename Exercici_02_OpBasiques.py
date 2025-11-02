# a) Inicialización de variables
x = 144
y = 999
res = 0.0

# b) Leer datos del usuario
x = int(input("Introducir valor de A: "))
y = int(input("Introducir valor de B: "))

print("x =", x)
print("y =", y)

# Realizar los cálculos
res = x + y
print("La suma es:", res)

res = x - y
print("La resta es:", res)

res = x * y
print("La multiplicación es:", res)

res = x / y  # Conversión automática a float
print("La división es:", res)

res = x // y
print("La división entera es:", res)

res = x % y
print("El resto de la división entera es:", res)
