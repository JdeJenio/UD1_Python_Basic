cont = 10
limite = 20

# a)
condicion = (cont == 0) and (limite < 20)
print("a)", condicion)

# b)
condicion = (limite >= 20) or (cont < 5)
print("b)", condicion)

# c)
# condicion = ((limite / (cont - 10)) > 7) or (limite < 20)
# print("c)", condicion)

# d)
condicion = (limite <= 20) or ((limite / (cont - 10)) > 7)
print("d)", condicion)

# e)
# condicion = ((limite / (cont - 10)) > 7) and (limite < 0)
# print("e)", condicion)

# f)
condicion = (limite < 0) and ((limite / (cont - 10)) > 7)
print("f)", condicion)
