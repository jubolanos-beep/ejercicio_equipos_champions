import csv
dic_resultados={}
def contar_puntos(diccionario):
    for equipo in diccionario:
        diccionario[equipo]["puntos"]=diccionario[equipo]["ganados"]*3
        diccionario[equipo]["puntos"]=diccionario[equipo]["puntos"]+diccionario[equipo]["empatados"]
        diccionario[equipo]["diferencia_goles"]=diccionario[equipo]["goles_favor"]-diccionario[equipo]["goles_contra"]
        print("equipo, ganados, empatados, perdidos, goles_favor, goles_contra, puntos, diferencia_goles")
        print(equipo,",",diccionario[equipo]["ganados"],",",diccionario[equipo]["empatados"],",",diccionario[equipo]["perdidos"],",",diccionario[equipo]["goles_favor"],",",diccionario[equipo]["goles_contra"],",",diccionario[equipo]["puntos"],",",diccionario[equipo]["diferencia_goles"])
def lider_tabla(diccionario):
    mayor=0
    lider=""
    for equipos in diccionario:
        if diccionario[equipos]["puntos"]>mayor:
            mayor=diccionario[equipos]["puntos"]
            lider=diccionario[equipos]["nombre"]
    print("el lider es: ",lider)
    print("partidos ganados: ")
    print( diccionario[lider]["ganados"])
    print ("partidos empatados: ")
    print(diccionario[lider]["empatados"])
    print("partidos perdidos: ")
    print(diccionario[lider]["perdidos"])

def exportar_archivo(diccionario):
    with open ("salida.txt", "w") as output:
        titulos="equipo, ganados, empatados, perdidos, goles_favor, goles_contra, puntos, diferencia_goles \n"
        output.write(titulos)
        for equipo in diccionario:
            contenido=equipo+","+str(diccionario[equipo]["ganados"])+","+str(diccionario[equipo]["empatados"])+","+str(diccionario[equipo]["perdidos"])+","+str(diccionario[equipo]["goles_favor"])+","+str(diccionario[equipo]["goles_contra"])+","+str(diccionario[equipo]["puntos"])+","+str(diccionario[equipo]["diferencia_goles"])
            output.write(contenido)
            output.write("\n")

with open ("input/equiposChampions.csv", "r") as archivo_input:
    contenido = csv.DictReader(archivo_input)
    for fila in contenido:
        dic_resultados[fila["equipo"]]={
            "nombre": str(fila["equipo"]),
            "ganados": int(fila["ganados"]),
            "empatados": int(fila["empatados"]),
            "perdidos": int(fila["perdidos"]),
            "goles_favor": int(fila["goles_favor"]),
            "goles_contra": int(fila["goles_contra"])
        }
    contar_puntos(dic_resultados)
    lider_tabla(dic_resultados)
    exportar_archivo(dic_resultados)
    
