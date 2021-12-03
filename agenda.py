agenda = {}

consultando = True

while consultando:
    print()
    print("Mi agenda telefónica")
    print("-"*15)
    print("1-Añadir contacto")
    print("2-Buscar contacto")
    print("3-Cerrar agenda")

    opcion = ""
    while opcion not in ("1", "2", "3"):
        print("")
        opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        if nombre in agenda:
            print("Ese nombre ya existe")
        else:
            telf = int(input("Teléfono: "))
            agenda[nombre] = telf
            print("El telefono se ha añadido correctamente")

    elif opcion == "2":
        print("Buscar contacto")
        print("-"*15)
        nombre = input("Nombre: ")
        if nombre not in agenda:
            print("Ese nombre no existe")
        else:
            telf = agenda[nombre]
            print(nombre, ":", telf)

    elif opcion == "3":
        print("Saliendo de agenda...")
        break
    