import os
os.system("cls")

titulo = """
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    +  -----    FEDERACION COLOMBIANA DE BETPLAY WOOOOOO      -----   +
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

# tabla = """
#     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     |  -----              TABLA DE INFORMACION                -----   |
#     |                                                                 |
#     |                                                                 |
#     |                                                                 |
#     |                                                                 |
#     |                                                                 |
#     |                                                                 |
#     |                                                                 |
#     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# """

opciones = "1. Agregar equipo\n2. Ordenar Partidos\n3. Reportes\n4. Salir"
isActivate = True
equipo = []

while isActivate:
    os.system("cls")
    print (titulo)
    print(opciones)
    op = int(input(":) : "))
    if (op == 1):
        id = str(len(equipo)).zfill(5)
        nombre = input("Ingrese el nombre del equipo, por favor : ")
        equipo.append([nombre.upper(),0,0,0,0,0,0,0])
    elif (op == 2):
        local = str(input("ingrese cual es local : "))
        visit = str(input("ingrese  cual es visitante : "))
        

        for i,item in enumerate(equipo):
            if (local.upper() in item):
                    item [1] +=1
                    print = ("El equipo se ha registrado correctamente como local.")
            elif(visit.upper() in item):
                    print = ("El equipo se ha registrado correctamente como visitante.")
                    item [1] +=1

            ### MARCADORES ###
                    
        marcadorl = int(input("Ingrese el numero de goles del equipo local : "))
        marcadorv = int(input("Ingrese el numero de goles del equipo visitante : "))
        
            ### MARCADORES ###

for i,item in enumerate(equipo):
    if ((local.upper() in item) or (visit.upper() in item)):
        if (item[0] == local.upper()):
            item [5] += marcadorl
            item [6] += marcadorv

        elif (item[0] == visit.upper()):
                item [6] += marcadorl
                item [5] += marcadorv

        if ((marcadorl > marcadorv)and(item[0] == local.upper())):
                item [2] += 1
                item [7] += 3

        elif ((marcadorv > marcadorl)and(item[0] == visit.upper()) ):
                item [3] += 1
                item [7] += 3
        
        if (marcadorl == marcadorv):
                item [4] += 1



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