import xml.etree.ElementTree as ET


ruta = input("Ingresa una ruta:")
archivo = ET.parse(ruta)

raiz = archivo.getroot()

for hijo in raiz:
    print(hijo)