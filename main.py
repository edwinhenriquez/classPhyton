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
palabras = ["Gato","Ventana","Murcielago"]
for p in palabras:
    print (p,len(p))
