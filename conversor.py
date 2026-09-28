import csv
import json
csv_file_path = "inventario.csv"
json_file_path = "inventario_convert.json"
data=[]
with open(csv_file_path, "r", encoding="utf-8") as archivo:
    csv_reader = csv.DictReader(archivo)
    for fila in csv_reader:
        fila["cantidad"] = int(fila["cantidad"])
        fila["precio"] = int(fila["precio"])
        data.append(fila)
with open(json_file_path,"w",encoding="utf-8") as json_file:
    json.dump(data,json_file, indent=4)
print("json generado correctamente")
