listas = [10, 105, 20, 14, 25, 36, 200, 106, 6, 26, 87, 54, 74, 84, 18]

print(max(listas))
print(min(listas))

sumar=0

for lista in listas:
    sumar  += lista

print(sumar)

cantidad = len(listas)
lista_media = sumar/cantidad
print(f"{lista_media:.2f}")