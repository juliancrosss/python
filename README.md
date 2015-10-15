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

#La libreria datetime

*from datetime import datetime

#Obteniendo la actual hora y dia

*from datetime import datetime

*now = datetime.now()

*print now

#Extrayendo informacion

*from datetime import datetime

*now = datetime.now()

*current_year = now.year

*current_month = now.month

*current_day = now.day

*Segundo Ejemplo*

from datetime import datetime

now = datetime.now()

print now

print now.year

print now.month

print now.day

#Imprimiendo Dia en formato legible 

*from datetime import datetime

*now = datetime.now()

*print '%s-%s-%s' % (now.year, now.month, now.day)

*Resultado 2014-02-19*

##Ejemplo 2

from datetime import datetime

now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)

#Hora Grandiosa

*from datetime import datetime

*now = datetime.now()

*print now.hour

*print now.minute

*print now.second

##Segundo Ejemplo

*from datetime import datetime

*now = datetime.now()

*print '%s:%s:%s' % (now.hour, now.minute, now.second)

*Resultado 5:48:57*

*from datetime import datetime

*now = datetime.now()

*print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

#Condicionales y Control de Flujo

*def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

#Comparaciones

##Hay seis comparaciones:

Igual  (==)

Diferente (!=)

Menor que (<)

Menor que o igual que  (<=)

Mayor que (>)

Mayor que o igual que (>=)


#Para ser  and/or o no ser

##Hay tres operadores booleanos:

and, lo que comprueba si las dos afirmaciones son ciertas;

or, lo que comprueba si al menos una de las afirmaciones es verdadera;

not, lo que da lo opuesto a la declaración.

##Ejemplo 

     Boolean Operators
------------------------ 
      AND
  ------------------------

*True and True is True

*True and False is False

*False and True is False

*False and False is False

      OR
 ---------------------

*True or True is True

*True or False is True

*False or True is True

*False or False is False

      NOT
 -------------------

*Not True is False

*Not False is True

#Orden de operaciones

*Operadores booleanos no sólo se evalúan de izquierda a derecha. Al igual que con los operadores aritméticos, hay una orden de operaciones para los operadores booleanos:*

*not* se evalúa primero;

*and* se evalúa siguiente;

*or* se evalúa como ultimo.

#Conditional Statement Syntax

    if 8 < 9:*

    *print "Eight is less than nine!"*


#Else

if 8 > 9:

    print "I don't printed!"
else:

    print "I get printed!"
    
#Else if 

if 8 > 9:

    print "I don't get printed!"
elif 8 < 9:

    print "I get printed!"
else:

    print "I also don't get printed!"
    
#Resumen

##Comparaciones

3 < 4

5 >= 5

10 == 10

12 != 13
##Boolean operaciones

True or False 

(3 < 4) and (5 >= 5)

this() and not that()

##Condicionales

if this_might_be_true():

    print "This really is true."
elif that_might_be_true():

    print "That is true."
else:

    print "None of the above."
#Input

nombre = raw_input("Cual es tu nombre?")

print nombre

#isalpha()

valida solo el abecedario


pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1: len(new_word)]
    print new_word
    print original
else:
    print 'empty'
    
    
    
#Function

*Functions are defined with three components:*
*1 The header, which includes the def keyword, the name of the function, and any parameters the function requires.*
*def hello_world(): // There are no parameters

*2 An optional comment that explains what the function does.*
"""Prints 'Hello World!' to the console."""
*3 The body, which describes the procedures the function carries out. The body is indented, just like for conditional statements.*

print "Hello World!"



*Example*

Here's the full function pieced together:

def hello_world():
    """Prints 'Hello World!' to the console."""
    print "Hello World!"
    
    
    
  def spam():
    """This function print "Eggs"""
    print("Eggs!")
    
# Llamando la fuction     
    def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)



#Parameters and Arguments

def square(n):
n is a parameter of square


def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!


#Functions Calling Functions

def fun_one(n):
    return n * 5

def fun_two(m):
    return fun_one(m) + 7
    
    
    
def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2









import math # importa un modulo 

print math.sqrt(25)

##Importa solamente una fuction 

from math import sqrt

from module import function

#Universal Imports

from module import *

from math import *

#Improtar solamente lo necesario 

import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

def shut_down(s):
    if (s =="yes"):
        s = "Shutting down"
    elif(s == "no"):
        s = "Shutdown aborted"
    else:
        s ="Sorry"
    return s
    
print shut_down("no")


from math import sqrt

print math.sqrt(13689)






