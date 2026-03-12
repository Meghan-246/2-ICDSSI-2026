"""
Nombre : Meghan Lopez Peña
Grupo : 2I
Fecha : 12/03/2026
"""

# Menu de la pasteleria
menu = []

# Reservaciones
reservacion = []

# Ordenes
ordenes = []

# Agregar pasteles al menu
menu.append({"nombre": "Una rebanada de pastel de vainilla", "precio": 120})
menu.append({"nombre": "Pastel de Fresa", "precio": 420})
menu.append({"nombre": "Pastel de Tres Leches", "precio": 570})
menu.append({"nombre": "Caffe con leche deslactosada light", "precio": 50})
menu.append({"nombre": "Un vaso de leche", "precio": 25})
opcion=0 
while opcion !=7:
    # Menu de opciones
    print("\n1. Agregar platillo")
    print("2. Ver ordenes")
    print("3. Ver reservaciones")
    print("4. Hacer reservacion")
    print("5. Hacer orden")
    print("6. Mostrar menu")
    print("7. Salir")

    opcion = int(input("Selecciona una de las opciones: "))

    # 1 Agregar platillo
    if opcion == 1:
        nombre = input("Como se llama lo que desea agregar al menu: ")
        precio = int(input("Cuanto va a costar: "))
        menu.append({"nombre": nombre, "precio": precio})
        print("Platillo agregado correctamente")

    # 2 Ver ordenes
    elif opcion == 2:
        print("\n--- ORDENES ---")
        for o in ordenes:
            print("Cliente:", o["cliente"], "| Pastel:", o["pastel"])

    # 3 Ver reservaciones
    elif opcion == 3:
        print("\n--- RESERVACIONES ---")
        for r in reservacion:
            print("Cliente:", r["cliente"], "| Pastel:", r["pastel"])

    # 4 Hacer reservacion
    elif opcion == 4:
        cliente = input("Nombre del cliente: ")
        pastel = input("Que pastel desea: ")
        reservacion.append({"cliente": cliente, "pastel": pastel})
        print("Reservacion hecha correctamente")

    # 5 Hacer orden
    elif opcion == 5:
        cliente = input("Nombre del cliente: ")
        pastel = input("Que pastel desea: ")
        ordenes.append({"cliente": cliente, "pastel": pastel})
        print("Orden registrada")

    # 6 Mostrar menu
    elif opcion == 6:
        print("\n--- MENU DE PASTELES ---")
        for pastel in menu:
            print(pastel["nombre"], "-", "$", pastel["precio"])