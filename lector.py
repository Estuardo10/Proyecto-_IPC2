import xml.etree.ElementTree as ET

def lectura_xml():
    ruta = input("Ingresa una ruta:")
    archivo = ET.parse(ruta)

    raiz = archivo.getroot()

    for hijo in raiz:
        print(hijo)

def menu():
    print("====== Menú =====")
    print("1. Cargar Archivo")
    print("2. Seleccionar paciente")
    print("3. Salir")
    entrada = input("Ingresa una opción del menú")

    if entrada == "1":
       lectura_xml() 
    elif entrada == "2":
       print("acá método para paciente")

menu()
