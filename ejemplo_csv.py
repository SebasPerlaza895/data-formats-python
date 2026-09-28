import csv

with open('inventario.csv','r',encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)

    for producto in lector:
        print(producto['nombre'], producto['categoria'])