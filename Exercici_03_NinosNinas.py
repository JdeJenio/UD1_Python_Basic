# Leer datos del usuario
ninos = int(input("Introducir el número de niños: "))
ninas = int(input("Introducir el número de niñas: "))

# Calcular y mostrar resultados
total = ninos + ninas

porcentaje_ninos = (ninos * 100) / total
porcentaje_ninas = (ninas * 100) / total

print("El porcentaje de niños es:", porcentaje_ninos, "%")
print("El porcentaje de niñas es:", porcentaje_ninas, "%")
