
archivo_nombre = "Texto12.txt"
with open(archivo_nombre,"r") as archivo:
    linea_lista = archivo.readlines()
print(linea_lista)