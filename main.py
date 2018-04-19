el_mundo_es_plano = True
if el_mundo_es_plano:
    print ("Tené cuidado de no caerte")
    

# este es el primer comentario

spam = 1                 # y este es el segundo comentario
                         # ... y ahora un tercero!
text = "# Este no es un comentario, es un String"

print (spam)
print (text)

print ("Como calculadora")
print ("Sumar")
valor1 = 6
valor2 = 3
print (valor1)
 
print ("+")
print (valor2)
suma = valor1 + valor2
print ("Igual")
print (suma)
print ("Por 2")
multiplicacion = suma * 2
print (multiplicacion)
resta = (multiplicacion - 5)
print ("menos 5")
print (resta)
division = round((resta / 3) ,2)
print ("entre 3")
print (division)
print ("***** Metodos para String")
nombre = 'alex'
print (nombre)
ininombre = (nombre[0])
print (ininombre)
print (nombre.upper())
print (nombre.lower())
print (nombre.title())

# Captura de datos con If
# x = input('Ingresa un entero, por favor: ')
x = 15
if x < 0:
    x = 0 
    print ('Negativo cambiado a cero')
elif x == 0:
    print ("Cero")
elif x == 1:
    print ("Simple")
else:
    print ("Mas")
    
# sentencia For, contando cadenas de texto
print ("***** Almacena cadenas")
palabras = ["Gato","Ventana","Murcielago"]
for p in palabras:
    print (p,len(p))

nombres = [
  "Pablo",
  "Juan",
  "Luis",
  "Bruno",
  "Maria"
]
print(nombres[4]) # Maria

print ("***** Agregar elementos a list")
libro = []
libro.append("Programacion")
libro.append("Computacion")
print(libro[0]) # Programacion
print(libro[1]) # Computacion

# loop e iteracion
print ("***** Loop e Iteracion")
num = 1
while num <= 10:
    print(num)
    num += 1
    
print ("***** Estructura de datos Clave, Valor")
Diccionario = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}

diccionario = {
  "nombre": "Pablo",
  "apodo": "Paul",
  "nacionalidad": "Mexicana"
}
print("Mi nombre es %s" %(diccionario["nombre"])) # Mi nombre es Pedro
print("Pero puedes llamarme %s" %(diccionario["apodo"])) # Pero puedes llamarme Paul
print("Mi nacionalidad es %s" %(diccionario["nacionalidad"])) # Mi nacionalidad es Mexicana

print ("***** Class")

class vehiculo:
    def __init__(self, numero_de_ruedas, tipo_de_tanque, numero_de_asientos, velocidad_maxima):
        self.numero_de_ruedas = numero_de_ruedas
        self.tipo_de_tanque = tipo_de_tanque
        self.numero_de_asientos = numero_de_asientos
        self.velocidad_maxima = velocidad_maxima
  
#Adicionar datos a la clase        
tesla_model_s = vehiculo(4, 'Electrico', 5, 250)

print ("Numero de ruedas: %s" % (tesla_model_s.numero_de_ruedas))
print ("Tipo de tanque: %s" % (tesla_model_s.tipo_de_tanque))
print ("Numero de asientos: %s" % (tesla_model_s.numero_de_asientos))
print ("Velocidad maxima (k/h): %s" % (tesla_model_s.velocidad_maxima))
