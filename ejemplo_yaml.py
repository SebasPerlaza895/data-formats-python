import yaml
with open("inventario.yaml","r",encoding="utf-8") as archivo:
    data = yaml.safe_load(archivo)
for producto in data:
    print(producto["nombre"], producto["precio"])