import csv

def crear_csv_nom_ap(p_lista_personas):
    with open('nombre_apellidos.csv','w',newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(p_lista_personas)

def validar_texto(texto):
    while True:
        valor =str(input(f'Ingrese {texto}: '))
        if len(valor.strip()) >= 3:
            break
        else:
            print(f'ERROR! debe ingresar {texto} con 3 letras minimo!')