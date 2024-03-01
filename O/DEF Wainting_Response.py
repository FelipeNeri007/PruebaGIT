import time

def waiting_response():
    print("Esperando respuesta...")
    time.sleep(5)  
    print("Respuesta recibida.")

c = "C:\\Users\\Colibecas\\Documents\\Plantillas personalizadas de Office\\" 
e = "Archivo1.txt"
s = "Archivo2.txt"

waiting_response()
e2 = open(c + e, "r")
s2 = open(c + s, "w")

t = e2.read()
t2 = t
s2.write(t2)

e2.close()
s2.close()

s3=open(c+s,"r")
print(s3.read())
s3.close()