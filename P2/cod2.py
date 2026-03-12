"""
Nombre :Meghan lopez peña
Grupo  :2I
Fecha  :11/04/2026
"""

#-------------------------------------------------------------------------#
def evaluar_grado(porcentaje):
    if porcentaje > 90:
        print("Grado: A")
    elif porcentaje > 80 and porcentaje <= 90:
        print("Grado: B")
    elif porcentaje >= 60 and porcentaje <= 80:
        print("Grado: C")
    else:
        print("Grado: D")

#-------------------------------------------------------------------------#
def impuesto_bicicleta(precio):
    if precio > 100000:
        impuesto = precio * 0.15
    elif precio > 50000 and precio <= 100000:
        impuesto = precio * 0.10
    else:
        impuesto = precio * 0.05

    print("Impuesto a pagar:", impuesto)

#-------------------------------------------------------------------------#
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")

#-------------------------------------------------------------------------#
def dia_semana(numero):
    dias = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
    
    if numero >= 1 and numero <= 7:
        print(dias[numero-1])
    else:
        print("Numero invalido")

#-------------------------------------------------------------------------#
def mes_y_dias(numero):
    meses = [
        ("Enero",31),("Febrero",28),("Marzo",31),("Abril",30),
        ("Mayo",31),("Junio",30),("Julio",31),("Agosto",31),
        ("Septiembre",30),("Octubre",31),("Noviembre",30),("Diciembre",31)
    ]

    if numero >= 1 and numero <= 12:
        mes, dias = meses[numero-1]
        print(mes,"tiene",dias,"dias")
    else:
        print("Numero invalido")

#-------------------------------------------------------------------------#
def primeros_naturales():
    for i in range(1,11):
        print(i)

#-------------------------------------------------------------------------#
def primeros_impares():
    for i in range(1,20,2):
        print(i)

#-------------------------------------------------------------------------#
def naturales_descendentes():
    for i in range(10,0,-1):
        print(i)

#-------------------------------------------------------------------------#
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero,"x",i,"=",numero*i)

#-------------------------------------------------------------------------#
def producto_digitos(numero):
    producto = 1
    for digito in str(numero):
        producto *= int(digito)
    print("Producto:",producto)

#====================== PROGRAMA PRINCIPAL ======================#

porcentaje = float(input("Ingresa el porcentaje del alumno: "))
evaluar_grado(porcentaje)

precio = float(input("Ingresa el precio de la bicicleta: "))
impuesto_bicicleta(precio)

anio = int(input("Ingresa un año: "))
es_bisiesto(anio)

dia = int(input("Ingresa un numero del 1 al 7: "))
dia_semana(dia)

mes = int(input("Ingresa un numero del 1 al 12: "))
mes_y_dias(mes)

print("Primeros 10 numeros naturales:")
primeros_naturales()

print("Primeros 10 numeros impares:")
primeros_impares()

print("Naturales descendentes:")
naturales_descendentes()

num = int(input("Numero para tabla de multiplicar: "))
tabla_multiplicar(num)

num2 = int(input("Numero para producto de digitos: "))
producto_digitos(num2)