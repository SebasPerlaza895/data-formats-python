import xml.etree.ElementTree as ET
arbol = ET.parse("inventario.xml")
raiz = arbol.getroot()
for producto in raiz.findall("producto"):
    print(producto.find("nombre").text)
    print(producto.find("precio").text)

