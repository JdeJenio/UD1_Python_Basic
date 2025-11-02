# Pedir datos al usuario
primer_examen = float(input("Introduïx la nota del primer examen: "))
nota_final = float(input("¿Quina nota vols tindre este trimestre? "))

# Calcular la nota necesaria en el segundo examen
segundo_examen = (nota_final - 0.4 * primer_examen) / 0.6

# Mostrar el resultado
print(f"Per a obtindre un {nota_final} en el trimestre necessites un {segundo_examen} en el segon examen.")
