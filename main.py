import csv
import xml.etree.ElementTree as ET
import yaml

#CVS

def leer_csv():
    estudiantes = []

    with open("estudiantes.csv","r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            fila["nota"] = float(fila["nota"])

            estudiantes.append(fila)
    
    return estudiantes

def mostrar_estudiantes():
    estudiantes= leer_csv()

    print("\n----LISTA DE ESTUDIANTES----\n")
    for estudiante in estudiantes:
        print("-----------------")
        print("Código : ", estudiante["codigo"])
        print("Nombre : ", estudiante["nombre"])
        print("Nota : ", estudiante["nota"])

def buscar_codigo():
    estudiantes= leer_csv()
    codigo = input("Ingrese el codigo del estudiante: ")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante["codigo"] == codigo:
            print("\n ESTUDIANTE ENCONTRADO")
            print("Código : ", estudiante["codigo"])
            print("Nombre : ", estudiante["nombre"])
            print("Nota : ", estudiante["nota"])
            encontrado = True
            break
    if not encontrado:
        print("No existe el estudiante")

def estadisticas():
    estudiantes= leer_csv()

    suma = 0
    aprobados=0
    mayor = estudiantes[0]
    menor = estudiantes[0]

    for estudiante in estudiantes:
        suma += estudiante["nota"]

        if estudiante["nota"] >= 3:
            aprobados += 1

        if estudiante["nota"] > mayor["nota"]:
            mayor = estudiante
        
        if estudiante["nota"] < menor["nota"]:
            menor = estudiante
    
    promedio = suma/len(estudiantes)

    print("\n---------ESTADISTICAS-------\n")
    print("Cantidad de estudiantes: ", len(estudiantes))
    print("Promedio: ",round(promedio,2))
    print("Mayor Nota: ", mayor["nombre"], mayor["nota"])
    print("Menor Nota: ", menor["nombre"], menor["nota"])
    print("Aprobados: ", aprobados)
    print("Reprobados: ",len(estudiantes)-aprobados)

#LEER XML

def mostrar_xml():
    arbol = ET.parse("estudiantes.xml")
    raiz = arbol.getroot()

    for estudiante in raiz.findall("estudiante"):
            print("-------------------------")
            print("Codigo: ", estudiante.find("codigo").text)
            print("Nombre: ", estudiante.find("nombre").text)
            print("Programa: ", estudiante.find("programa").text)
            print("Semestre: ", estudiante.find("semestre").text)
            print("Correo: ", estudiante.find("correo").text)

def buscar_programa():
    arbol = ET.parse("estudiantes.xml")
    raiz = arbol.getroot()

    programa = input("Ingrese programa").lower()
    encontrado = False

    for estudiante in raiz.findall("estudiante"):
        if programa in estudiante.find("programa").text.lower():
            encontrado= True
            print("-------------------------")
            print("Nombre: ", estudiante.find("nombre").text)
            print("Programa: ", estudiante.find("programa").text)
            print("Semestre: ", estudiante.find("semestre").text)
        if not encontrado:
            print("No se encontro estudiantes")

#leer yaml
def leer_yaml():
    with open("configuracion.yaml","r",encoding="utf-8") as archivo:
        datos = yaml.safe_load(archivo)

    print("\n---------CONFIGURACION-------\n")
    print("Entidad Educativa")
    print("Nombre: ", datos["universidad"]["nombre"])
    print("Sede: ", datos["universidad"]["sede"])
    print("Ciudad: ", datos["universidad"]["ciudad"])

    print("Sistema")
    print("Version: ", datos["sistema"]["version"])
    print("Administrador: ", datos["sistema"]["administrador"])
    print("Idioma: ", datos["sistema"]["idioma"])

    print("Bases de datos")
    print("Motor: ", datos["base_datos"]["motor"])
    print("Servidor: ", datos["base_datos"]["servidor"])
    print("Puerto: ", datos["base_datos"]["puerto"])

#Menu

while True:
    print("\n=================================")
    print("SISTEMA ACADEMICO")
    print("=================================")
    print("1. Mostrar estudiantes (csv)")
    print("2. Buscar estudiantes (csv)")
    print("3. Estadisticas de notas estudiantes (csv)")
    print("4. Mostrar detalle (XML)")
    print("5. Buscar estudiante programa (XML)")
    print("6. Ver configuracion de sistema (YAML)")
    print("7. Salir")

    opcion = input("\nSelecione opcion: ")

    if opcion == "1":
        mostrar_estudiantes()
    elif opcion == "2":
        buscar_codigo()
    elif opcion == "3":
        estadisticas()
    elif opcion == "4":
        mostrar_xml()
    elif opcion == "5":
        buscar_programa()
    elif opcion == "6":
        leer_yaml()
    elif opcion == "7":
        print("✋- Saliendo del Sistema....")
        break
    else:
        print("Opcion no valida")