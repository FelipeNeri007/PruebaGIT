import time

def waiting_response():
    print("Esperando respuesta...")
    time.sleep(5)  
    print("Respuesta recibida.")

c = "C:\\Users\\Colibecas\\Documents\\Plantillas personalizadas de Office\\" 
e = "Archivo1.txt"
s = "Archivo2.txt"

e2 = open(c + e, "r")
s2 = open(c + s, "w")

t = e2.read()
t2 = t
s2.write(t2)

e2.close()
s2.close()

with open(c+s,"r") as archivo:
    texto=archivo.read()
palabra = input("Escribe la palabra que buscas:")
print(texto)

if palabra in texto:
    print("Encontre la Palabra")
else:
    print("Esa palabra no existe")