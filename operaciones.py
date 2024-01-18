import os
os.system("cls")

titulo = """
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    +  -----    FEDERACION COLOMBIANA DE BETPLAY WOOOOOO      -----   +
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

tabla = """
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    |  -----              TABLA DE INFORMACION                -----   |
    |                                                                 |
    |                                                                 |
    |                                                                 |
    |                                                                 |
    |                                                                 |
    |                                                                 |
    |                                                                 |
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
opciones = "1. Agregar equipo\n2. Ordenar Partidos\n3. Reportes\n4. Salir\n5. Salir"
isActivate = True
equipo = []

# PARTIDOS JUGADOS #
PJ = 0

# PARTIDOS GANADOS #
PG = 0

# PARTIDOS PERDIDOS #
PP = 0

# PARTIDOS EMPATADOS #
PE = 0

# GOLES A FAVOR #
GF = 0
# GOLES EN CONTRA #
GC = 0

# TOTAL DE PUNTOS #
TP = 0

while isActivate:
    os.system("cls")
    print(titulo)
    print(opciones)
    op = int(input(":) : "))
    if (op == 1):
        id = str(len(equipo)).zfill(5)
        nombre = input("Ingrese el nombre del equipo, por favor : ")
        equipo.append([id,nombre,PJ,PE,PG,PP,GF,GC,TP])
    elif (op == 2):
        local = input("Deme un numero para escoger el equipo local, por favor : ")
        visit = input("Deme un numero para escoger el equipo visitante, por favor : ")
        marcadorl = int(input("Ingrese el numero de goles del equipo local : "))
        marcadorv = int(input("Ingrese el numero de goles del equipo visitante : "))
        for i,item in enumerate(equipo):
            if (local in item):
                equipo[i][3]+marcador1
                equipo[i][3]+marcador2
                if (marcador1>marcador2):
                    for item in equipo:
                        if (local in item):
                            item
    elif (op == 3):
        print("---- Aquí está la lista de Todos los Datos ----")
        for i,item in enumerate(equipo):
                print(f"Numero :  {equipo[i]}")
                os.system("pause")
    elif (op == 4):
        isActivate = False
        print("Gracias por utilizar el programa.")
        os.system("pause")
    elif (op == 5):
        pass
    else:
        os.system("cls")
        print("La opcion ingresada no es valida")
        os.system("pause")