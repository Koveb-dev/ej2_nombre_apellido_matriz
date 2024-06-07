from funciones import *


personas = []


for x in range(3):
    lista_usuario =[]
    nombres = validar_texto('nombre')
    lista_usuario.append(nombres)
    apellidos = validar_texto('apellido')
    lista_usuario.append(apellidos)
    personas.append(lista_usuario)

crear_csv_nom_ap(personas)


