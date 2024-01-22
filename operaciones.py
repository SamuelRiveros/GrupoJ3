import os
os.system("cls")

from tabulate import tabulate

titulo = """
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    +           FEDERACION COLOMBIANA DE BETPLAY WOOOOOO              +
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

opciones = "1. Agregar equipo\n2. Ordenar Partidos\n3. Reportes\n4. Reportes Finales\n5. Salir"
jijijaja = True
equipo = []

totalgoles = 0
totalpartidos = 0

while jijijaja:
    os.system("cls")
    
    print(titulo)
    print(opciones)
    op = int(input(":) : "))
    if (op == 1):
        id = str(len(equipo)).zfill(5)
        nombre = input("Ingrese el nombre del equipo, por favor : ")
        equipo.append([nombre.upper(),0,0,0,0,0,0,0])
    elif (op == 2):
        local = str(input("ingrese cual es local : "))
        visit = str(input("ingrese  cual es visitante : "))
        
        if (local.upper() == visit.upper()):
            print("ingrese dos equipos diferentes")
        else:        
            marcadorl = int(input("Ingrese el numero de goles del equipo local : "))
            marcadorv = int(input("Ingrese el numero de goles del equipo visitante : "))
            totalgoles += marcadorl + marcadorv
            totalpartidos +=2

            for i,item in enumerate(equipo):
                if ((local.upper() in item) or (visit.upper() in item)):
                    if (item[0] == local.upper()):
                        item[1] +=1
                        item [5] += marcadorl
                        item [6] += marcadorv
                        if ((marcadorl > marcadorv)):
                            item [2] += 1
                            item [7] += 3
                        elif ((marcadorv < marcadorl)):
                            item [3] += 1
                        
                    elif (item[0] == visit.upper()):
                        item[1] +=1
                        item [6] += marcadorl
                        item [5] += marcadorv
                        if ((marcadorl < marcadorv)):
                            item [2] += 1
                            item [7] += 3
                        elif ((marcadorv < marcadorl)):
                            item [3] += 1
                    elif (marcadorl == marcadorv):
                            item [4] += 1
                        

    elif (op == 3):
        print(tabulate(equipo,headers=["Nombre","PJ","PG","PP","PE","GF","GC","TP"]))
        os.system("pause")

    elif (op == 4):
        print("Reportes")
        equipomasgoles= max(equipo, key=lambda n:n[5])
        print(f"El equipo con mas goles es : {equipomasgoles[0]}")
        equiposconmaspuntos= max(equipo, key=lambda n:n[7])
        print(f"El equipo con mas puntos es: {equiposconmaspuntos[0]}")
        equipomasvictorias=max(equipo, key=lambda n:n[2])
        print(f"El equipo con mas victorias es: {equipomasvictorias[0]}")
        print(f"El total de goles en el torneo es: {totalgoles}")
        print(f"El promedio de goles es : {totalgoles/totalpartidos}")
        

        os.system("pause")
    elif (op == 5):
        jijijaja = False
        print("Gracias por utilizar el programa.")
        os.system("pause")
        
    else:
        os.system("cls")
        print("La opcion ingresada no es valida")
        os.system("pause")