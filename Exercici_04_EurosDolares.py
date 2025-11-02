# Constante
VALOR_DOLAR = 1.11

# Pedir datos al usuario
euros = float(input("Dime la cantidad en euros: "))

# Realizar la conversión
dolares = euros * VALOR_DOLAR

# Mostrar el resultado
print(f"{euros}€ = {dolares}$")
