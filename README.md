# python


#Comienzo con Python 
##imprimir con python 
* print"Hola Mundo"
* print "Monty Python"

##Imprimiendo Variables

*the_machine_goes = "Ping!"

*print the_machine_goes


#Variables
entero = 4

float = 1.23

string = "Julian"

print(entero)

#Boleanos
bool = True

bool2 = Flase

#Reasignacion
int = 2

##Reasignando

int = 3

print int

#Identacion de bloques 

|def numero()
|
|-- numero = 3
|
|-- return numero
  
print numero

#Interpretacion

verdad = True

falso = False

print verdad, falso

#Comentarios de una sola linea 

 #Esto es un comentario  empieza con numeral "#"
 
#Comentarios en varias lineas
"""esto es un 

comentario en varias lineas """

#Matematicas con python 
adicion = 72 + 23

resta = 72 - 23

multiplicacion = 108 * 0.5

division = 108 / 9

#Exponenciación
ocho = 2 ** 3

cien = 10 ** 2

#Modulo
Modulo devuelve el resto de una división. Así, si escribe 3% 2, devolverá 1, 2, porque entra en 3 de manera uniforme una vez, con 1 sobra.

modulo = 12%11

print modulo

modulo = 3%2

##Resumen

*Variables, que almacenan los valores para su uso posterior

*Los tipos de datos, tales como números y booleanos

*El espacio en blanco, que separa los estados

*Comentarios, que hacen que su código sea más fácil de leer

*Las operaciones aritméticas, incluyendo +, -, *, /, **, y el%

#String

nombre = "Julian"

edad = "23"

comida = "queso"

#Escapando de los  caracteres

*Hay algunos caracteres que causen problemas. Por ejemplo:

*'There's a snake in my boot!'

*Este código se rompe porque Python cree que el apóstrofe en 'There's' termina la cadena. Podemos utilizar la barra invertida para solucionar el problema, así:*

*'There\'s a snake in my boot!'

*'This isn\'t flying, this is falling with style!'

#Acceso por Index en Strings

*Cada carácter en una cadena se le asigna un número. Este número se llama el índice.*

g = "gatos" [0]

n = "Ryan" [3]

#String metodos 

*len()*

*lower()*

*upper()*

*str()*
 

*len() Ayuda obtener la cantidad de caracteres de un string*

*nombre = Julian

*print len(nombre)

*lower() combierte los caracteres en minuscula*

*nombre = Julian

*nombre.lower()

*print nombre.lower()

*upper() combierte los caracteres en mayuscula*

*nombre = Julian

*nombre.upper()

*print nombre.upper()

*str() combierte a los no-string a datos string*

*pi = 3.14

*print str(pi)

#Dot Notation// Notacion de puntos

*len(string) y str(objeto), pero la notación de puntos (como "String".upper()) para el resto.*

*león = "rugido"

*len(león)

*lion.upper()

*Los métodos que utilizan la notación de puntos sólo funcionan con cadenas.Por otro lado, len() y str() puede trabajar en otros tipos de datos.*

*ministry = "The Ministry of Silly Walks"

*print len(ministry)

*print ministry.upper()

#Concatenación de cadenas

*print "Julian " + "Andres " + "Cruz."


#Conversion Explicita a String

*print "I have " + str(2) + " coconuts!"

*print "The value of pi is around " + str(3.14)

#Formatiando String  con %

*name = "Mike"

*print "Hello %s" % (name)

*Resultado "Hello Mike"*

*Segundo ejemplo*

*string_1 = "Camelot"
*string_2 = "place"

*print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

*Resultado Let's not go to Camelot. 'Tis a silly place.*

##Segunda forma 

*print "The %s who %s %s!" % ("Knights", "say", "Ni")
*Resultado This will print "The Knights who say Ni!"*

*Segudo ejemplo*

*name = raw_input("What is your name?")
*quest = raw_input("What is your quest?")
*color = raw_input("What is your favorite color?")

*print "Ah, so your name is %s, your quest is %s, " \"and your favorite color is %s." % (name, quest, color)*








