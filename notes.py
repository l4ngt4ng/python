

p y t h o n 
___________

visual code usefull shorcuts:
    
comentar y descomentar de golpe:
    ctrl k comentar ctrl c
    ctrl k descomentar ctrl u
modo zen 
    ctrl k z ( activar y desactivar)
mover varias lineas de codigo arriba abajo.
    select and alt flecha up y down 
Tabular Izquierda: 
select and shift tab 
Tabular derecha
select and tab  

Quitar espacios blancos o tabs del final de linea: 
    Ctrl e ctrl º

    
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  p y t h o n V 2 / V 3  &  P i p 2 / P i p 3  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


¿como saber si el script esta escrito para python 2 o 3 ? 

p y t h o n v2 / v3
___________________


si al abrir un script observas :
print "loquesea" ---> python v2
print ("lo que sea") ---> python v3

python2 emplea ASCII
python 2 division entera only  python2 y en el interprete >>> 5/3  regresa 1 
y pones type (5/3)  regresa type int 

python3 emplea Unicode 
python 3 puede regresa float  >>> 5/3   regresa 1.666666666666666667
y pones type (5/3)  --> regresa class float 

P I P pip installs packages
___________________________
pip2

pip3 intall pwntools

---

A TENER EN CUENTA CON PYTHON3 -c ''

lo que dentro del interprete era:
>>> variablea=True
>>> type(variablea)
<class 'bool'> 
>>> if variablea:
...     print ("verdadero!!!!")
... 
verdadero!!!!

fuera: 

python3 -c 'variablea=True; print ("verdadero!!!!") if variablea else None'

~ ❯ python3 -c 'variablea=True; print ("verdadero!!!!") if variablea else None'
verdadero!!!!


____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  S h e b a n g  &  M o d u l e s  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________



s h e b a n g :
#!/usr/bin/python3      
#!/usr/bin/env python3  <--- mejor este por si no estuviese el binario de python3 en esa ruta y de esta forma 
                             la va a buscar de env ( del path que este definido en environment )

---

m o d u l e / main module 
_________________________

[moduloPrincipal.py]

#!/usr/bin/env python3

if __name__ == '__main__':
	print ("soy el modulo principal")
else: 
	print ("NO soy el modulo principal")


[moduloLlamante.py]
import moduloPrincipal

Si ejecutas los dos : 

python moduloPrincipal.py ---> regresa: soy el modulo principal
python moduloLlamente.py  ---> regresa: NO soy el modulo principal

dado que en python dentro del mismo directorio haces un import sin especificar extension y puedes usar ese mod 


____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  C o n v e n c i o n e s  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


l o w e r  c a m e l  c a s e : funciones 
_____________________________

funciones nombres convenio: minusculasMayusculacapitalizado()
def ejemploNombreCapitalizado()

s n a k e  c a s e minusculas
__________________

def comprobar_estado_api():  <--- todo minusculas y separado con _ en P Y T H O N se suele ve esto

s c r e a m i n g  s n a k e  c a s e MAYUSCULAS
_____________________________________ 

constantes

VERSION_API = 1.0.0
URL_API = "https://hack4u.io"  

u p p er  c a m el  c a s e ::: aplica sobre clases generalmente
___________________________

class NombreDeLaClase  


EXCEPCIONES:

cuando quieres declarar una variable / metodos protegidos :
_protegido ="estoy protegido una barra baja"
cuando quieres declarar una variable / metodos privados :
__privado ="estoy privado dos barras bajas"




____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  C a s t i n g   * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

c a s t i n g 

cadena_numero = "30"

print(type(cadena_numero)) ---> str 

cadena_numero = int(30)    ---> int
                str
numero_float_a_entero =int(4.0)
                float...
                       
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  E s t r u c t u r a s   d e  d a t o s  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

RESUMEN
lista = [1, "dos", False, [1, 4]]   --- type list. Adminten diferentes tipos de datos
diccionario = {'manzanas': 1, 'peras': 5} --- type: dict. Almacenan pares de clave valor / no indice / SI MUTABLE
tupla = (1, "dos", True, [1, 2, 3]) --- type: tuple. Como listas pero NO se pueden modificar, util evitar cagadas en el codigo
conjunto = {1, 2, 3}                --- type: set.  No se acceden por indice, no hay elementos iguales, existe Union Interseccion Diferrence ... 
                                                    utiles para depurar listas eliminar duplicados ... con un "casting"
                                                    no importa el orden
---                                        

/////////
L i s t a  no_repeticiones = list(set(my_lista_repetida)) 
/////////


se define con [] ---> se referencia con ()

        22 80 443 ... 
        ^  ^  ^
        |  |  |
indice  0  1  2   ---


my_ports = []

my_ports.append(22) 
my_ports.append(80)
my_ports.append(443)


otra opcion : my_ports +=[11, 22]

print(my_ports[0]) ---> 22 
      my_ports[2]  ---> 443




Otra opcion : : :
for port in my_ports:
    print("Puerto: "+ str(port))
    otra opcion
    print(f"Puerto " {port}")
#-->fuera del bucle ya Sin tabular
print (f"\n[+] La lista tiene un total de {len(my_ports)} elementos")

La lista puede predefinirse por medo de : 
my_ports = [22, 80, 443, 8080, 445, 445]  <--- Lista contempla repeticiones

Ordenar: my_ports = sorted(my_ports)
         my_ports.sort() 
Borrar: 
    Para borrar por indice: del my_ports[0]
    Para borrar por elemento: my_ports.remove(22)
    Para borrar el ultimo elemento my_ports.pop()
    Para borrar un elemento concreto my_ports.pop(1)
    Para borrar todos elementos: my_ports.clear() ---> print(len(my_ports)) == 0 

Insertar:
    my_ports[2] = "334" inserta en la posicion 2 pero elimina el elemento que había 
    my_ports.insert(2, "334") este no, lo mete en la 2 y el que había en la 2 pasa al tres

Copiar listas:
    copia_lista = list(original_lista)
    copia_lista = original_lista[:]
    
Concatenar listas
lista1 = ["uno", "dos"]
lista2 = ["tres", "cuatro"]
lista1.extend(lista2)

---> uno dos tres cuatro
        
Reverse list: ---> <---- cambia de orden la lista 
        lista.reverse()

Rangos: my_ports[0:3] elementos desde indice 0 al 3 [22, 80, 443, 8080, 445, 445]
                                                     ^   ^   ^    ^
                                                     |   |   |    |
                                                     0   1   2    3
        my_ports[:3] ---> 22   80  443 
        my_ports[3:] ---> 8080 445 445
        my_ports[:2] ---> 22   80  443 
        my_ports[-1] ---> 445  es el último elemento
        my_ports[2:4] --> 443 8080 445
Indice: my_ports.index(443) ---> regresara 2 pero si hay repetidos regresa la primera ocurrencia

I t e r a r:
(enumerate recibe indice valor)
for i,port in enumerate(my_ports): 
    print(f"{i} ::: {port}")  

indice valor 
0      22
1      80
2      443
...    ---

while i < len(my_pots):
    print(my_ports[i])
    i += 1

mayusculas 
attacks = ["Phising", "DDoS", "SQL Injection", "Man in the middle", "Cross-Site Scripting"]
attacks_uppercase = [attack.upper{} for attack in attacks]
alterar valor
minusculas 
attacks_uppercase = [attack.lower{} for attack in attacks]

z i p  ( aplica una combinatoria )
names = ["Manolo", "Pedro","Ramón"]
edades = [27, 25, 23]

for name, edad in zip(names, edades):
    print(f"{name} tiene {edad} años")
    
---> Manolo tiene 27 años
---> Pedro tiene 25 años 
---> ...

---


 
Esto crea una nueva lista con las posiciones del elemento valor == 445 en este caso 4,5 
[22, 80, 443, 8080, 445, 445]
                      ^    ^
                      |    |
                      4    5

indices_valor_445 = [x for x,y in enumerate(my_ports) if y == 445 ] 
print(indices_valor_445)
[4,5]

Contar elementos: my_ports.count(445) ---> regresa 2 porque hay dos elementos = a 445

Eliminar duplicados: 
1.- ordena my_ports = sorted(my_ports)
2.- lo cambia a set(my_ports)
    la cambia de tipo a SET y como en set no puede haber elementos duplicados ya estaría.
3.- type(set(my_ports)) ---> <class 'set'>
Conclusion: my_ports = list(set(my_ports)) ---> ese list lo vuelve a dejar en lista pero sin duplicados 


Operaciones - + / * media 

+ sum(my_ports)
media=sum(my_ports)/len(my_ports) <--- len numero de elementos
para quitar decimales que solo muestre 3 : round(sum(my_ports) / len(my_ports), 3)

#funciones
juegos = ["Super Mario Bros", "Zelda: Breath of the Wild", "Cyberpunk 2077"]


////////////

T U P L A S NO SE PUEDEN MODIFICAR POR ESO EXISTEN ---> Para modificarla hay que crear una nueva 

////////////

example = (1, "test", 3, True, [1, 2, 3], 4) <--- puede contener diferentes tipos de datos como las listas
print(example[0])  <--- va como en una lista 
              -1   <--- ultimo elemento 
             [1:3] <--- rangos ...
No puedes modificar la tupla : example[1] = 8 <--- INMUTABLE no permite insert(), exetend(), remove(), append()

mi_tupla1 = (1, 2, 3, 4)
a, b, c, d = mi_tupla

print(a) ---> 1
print(b) ---> 2

print(len(mi_tupla1)) ---> longitud 

mi_tupla2 = mi_tupla1*2 ---> aumenta la tupla al doble de valores 
mi_tupla3 = mi_tupla1 + mi_tupla2

numeros_pares = tuple(i for i in my_tupla1 if i % 2 == 0)
                      ^     ^
                      |_____|
print(numeros_pares)



////////////
S E T        No esta ordenado no tiene indice y no admite duplicados 
////////////
mi_conjunto = {1, 2, 3}
print(type(my_conjunto)) ---> type: set

a d d :: insertar un elemento: mi_conjunto.add(8) ---> {8, 1, 2, 3} no esta ordenado 
u p d a t e :: insertar multiples elementos : mi_conjunto.update({4, 5, 6}) ---> {1, 2, 3, 4, 5, 6}

borrar elemento : mi_conjunto.remove(3) ---> borra el elemento que vale 3
                             .discard como remove pero si no existe no peta
                             .clear() ---> elimina todos elementos del conjunto
intersection
c1 = {1, 2, 3, 4, 5}
c2 = {3, 4, 5, 6, 7}
cfinal = c1.intersection(c2) ---> 3 4 5 


union ( sin repetidos / no esta permitido)
cfinal =c1.union(c2) ---> {1, 2, 3, 4, 5, 6, 7}  <--- ordenado de casualidad

Subconjunto?
c1 = {1, 2, 3}
c2 = {1, 2, 3, 4, 5}
print( c1.issubset(c2)) ---> True / False

Differences ( elementos fuera de la interseccion) cfinal = c1.difference(c2)

U S O S sobre listas 
1.- no repetidos en una lista usamos set 
mi_lista = [1, 2, 3, 4, 5, 1, 2, 3]

no_repeat= set(mi_lista)
print(no_repeat) ---> {1, 2, 3, 4, 5}

Y otra vez a lista : no_repeat = list(set(mi_lista)) ---> ya esta en lista y sin elementos duplicados

2.- Es más óptimo/eficiente buscar en un conjunto que en una lista.
mi_conjunto = set(range(10000))
print(1234 in mi_conjunto)  ---> esto es mucho mas eficiente que recorrer una lista


 
///////////////////////
D I C C I O N A R I O S almacenan pares de clave valor / no indice / SI MUTABLE
///////////////////////

midicc = {"nombre": "abr", "edad": 28, "isla": "Tenerife"}
print(midicc["nombre"]) ---> abr

for key, value in midicc.items():
    print(f"La clave : {key} tiene el valor {value}")
print(f"La longitud del dicc es: {len(midicc)}")

#limpiar contenido 
midicc.clear()



update : midicc["nombre"] = "alberto"
insert : midicc["profesion"] = "musico" <--- como no existe no modifica sino que inserta
delete: del midicc["edad"]

ver si un elemento existe: 
if "nombre" in midicc:
   print("existe")
   

cuadrados ={x: x**2 for i in range(6)}
print(cuadrados)    ---> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(cuadrados[5]) ---> 25

#g e t 
print(midicc.get("Nomber", "No encontrado"))
                    ^
                    \_ esta clave no existe te imprime lo que hay a la derecha 
#u p d a t e 
midicc1 = {"nombre": "abr", "edad": 28, "isla": "Tenerife"}
midicc2 = {"nombre": "alberto", "edad": 47, "isla": "Menorca"}
midicc1.update(midicc2) ---> concatena, adiciona elementos del dicc2 al dicc1

#complex dicc

my_dict = {
        "nombre": "albert",
        "hobbies": {"primero": "bajo electrico", "segundo": "musica electronica"},
        "edad": 28 
}

len vale 3 elementos 
print(my_dict["edad"]) ---> 28
print(my_dict["hobbies"]["primero"]) ---> musica

#only keys
for element in my_dict.keys: --- Es lo mismo
for element in my_dict:      --- claves
    print(element) ---> nombre hobbies edad

#only values
for element in my_dict.values():
    print(element) ---> albert  {"primero": "bajo electrico", "segundo": "musica electronica"}  28

#Los dos clave valor 

for key, value in my_dict.items():
    print(f"clave: {key} valor: {value}")
    
#formas de representar 
clientes = {
        "Super Mario Bros": {"Marcelo", "Marcela"},
        "Final Fantasy VII": {"Lucía", "Manolo"}
}
MiJuego="Final Fantasy VII"
#j o i n ---> para representar con un separador concreto en este caso una coma
print(f"\t[+] CLientes que han adquirido el juego: {', '.join(clientes["MiJuego"])}")
---> Lucía, Manolo
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  O p e r a d o r e s  &  O p e r a c i o n e s  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

NUMEROS
#!/usr/bin/env python3 
numero1 = 2
numero2 = 3
resultado = numero1 + numero2 
print (numero1 + numero2)
print (resultado) 

- * / print (round(resultado, 2)) muestra dos decimales
% el resto de la división
potencias con ** 
numero1 ** numero2  esto es dos elevado a 3 = 8 

CADENAS 
primera="Hola"
segunda=" "
tercera="Mundo"

print (primera + segunda + tercera) ---> Hola Mundo
print(primera*3)                    ---> HolaHolaHola
print(primera[0]*3)                 ---> HHH 
print(primera[1]*2)                 ---> oo
print(tercera[0:3]*2)               ---> MundMund

LISTAS
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8]
result = odd_numbers + even_numbers ---> [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
Sumar los valores: 
ZIP hace tuplas por indices de lista, el primer elemento de la lista 1 con el primero de la lista 2... 
si las listas son desiguales en numero de elementos, forma tuplas hasta que puede, en este caso 
el 9 no formaria tupla:
(1, 2)
(3, 4)
(5, 6)
(7, 8)

result = zip(odd_numbers, even_numbers) 
for element in result:
    print(element)
    #print(type(element)) ---> class tuple

(1, 2)
alterar valor
(3, 4)
(5, 6)
(7, 8)

Para finalmente sumar las tuplas entre sí : Map

result = map(sum, zip(odd_numbers, even_numbers))
que lo meta en una nueva lista :
result = list(map(sum, zip(odd_numbers, even_numbers)))

____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  S t r i n g  F o r m a t i n g  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


formatear el resultado : un numero ? 35000000 35 millones para leerlo mejor 35.000.000 --->
print("{:,}".format(resultado)) no permite . 35,000,000
         ^                                 ^
         |                                 |
          \________________________________/
          
print("{:,}".format(resultado).replace(",", "."))  ---> 35.000.000
                                          ^
                                          |
                                          separar

#!/usr/bin/env python3

name="A"
surname="BenRod"
age=47 

dos cadenas :
print("My name is %s and my surname is %s" % (name, surname )) ---> My name is A and my surname is BenRod
Una cadena y un numero: 
print("My name is %s and my age is %d" % (name, age )) ---> My name is A and my age is 47
                                   ^
                                   si no lo especificas y pones un %s es como un str pero no es conveniente
                                   ya que es un int
Sin tipo de dato: 
print("Hola, soy {}! y tengo {} años".format(name,edad))
Con indices:
print("Hola, soy {0}! y tengo {1} años. Mi nombre es {0}".format(name, edad))
                  ^            ^                                   ^
                  A            47                                  A
Sin Format ni tipo:
print(f"Hola, soy {name} y tengo {age} años")
      ^
      necesario indicar f strings 

######################################### String formating advanced ##
suma enteros 
a = 5
b = 7 
print(f"La suma de {a} + {b} es {a + b}")

---
#strip
cadena = "    hola con espacios   \n\t"
print(cadena.strip()) <--- elimina espacios a las dos direcciones, saltos de linea, tabs ...

#lower upper replace
cadena = "Hola mUndo!!"
print(cadena.lower())
print(cadena.upper())
print(cadena.replace('o', 'x')) #donde haya o escribes x

#split
cadena = "Hola Mundo test"
nueva_cadena = cadena.split()
print(nueva_cadena) ---> ['Hola', 'Mundo', 'test'] ---> crea una lista con delimitador espacio por defecto 

cadena = "Hola:Mundo,test"
nueva_cadena = cadena.split(':')
print(nueva_cadena) ---> ['Hola', 'Mundo,test'] ---> delimitador : 

print(nueva_cadena[0])


#startswith/endswith 
s = "hola mundo"
print(s.startswith('h')) ---> True
        endswith
#capitalize
print(s.capitalize()) ---> Hola mundo 
                           ^
#tittle
print(s.title()) ---> Hola Mundo 
                      ^    ^
#swapcase
s = "HolA MundO"
print(s.swapcasee()) ---> hOLa mUNDo"

#isalpha ( compuesta por caracteres del alfabeto)
s = "HolA MundO"
print(s.isalpha()) ---> True

#isdigit 
print(s.isdigit()) ---> False

#isspace islower istitle... 

#find
print(s.find("Mundo")) ---> 5 donde comienza la cadena error es -1 ( si no existe lo que buscas )

#index devuelve una excepcion si no existe por ejemplo 
print(s.index("ggg"))

#count 
s = "Esto es una prueba para contar el total de caractere e que hay en la frase"
print(f"\n[+] Total de veces ue sale el caracter 'e': {s.count('e')}")

#join 
# lista de cadenas
lista_cadena = ["Hola", "Mundo"]
print (' '.join(lista_cadena)) --->Hola Mundo

nombres = ["Laura", "Gema", "Manolo"]
print(f"\n[+] Los nombres son: {'# '.join(nombres)}") ---> Laura# Gema# Manolo#


#replace 
c = "eliminando, comas, de la cadena"
print(c.replace(',',''))

#maketrans() y translate() para reemplazo avanzado 

s = "Vamos a trabnsformar una cadena"
tabla = str.maketrans('aeu', 'zpX') ---> Vzmos z trzbnsformzr Xnz czdpnz 
nueva_cadena = s.translate(tabla)
print(nueva_cadena)



____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  D a t e T i m e  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


#!/usr/bin/env python3

import datetime 

fecha = datetime.date(2024, 5, 7)
print(fecha) ---> 2024-05-07 ( se ve como una fecha )

hora = datetime.time(14, 15, 15) ---> 14:15:15
fecha_hora = datetime.datetime(2024, 5, 7, 14, 15, 15) ---> 2024-05-07 14:15:15

now = datetime.datetime.now()
print(now) ---> 2024-01-09 07:59:17.833097

año = now.year
.        .month
.        .day 
.        .hour
.        .minute
.        .second











____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  R e g u l a r  E x p r e s i o n s  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


import re 
text = "fecha 10/10/2023 y otra fecha 11/10/2023"
matches = re.findall("\d{2}\/\d{2}\/\d{4}", text)
                         ^ escapa las barras 
                         numero de digitos \d en este caso 
print(matches) ---> ['10/10/2023', '11/10/2023']

#pretendes encontrar los dos correos dentro de la cadena
text = "Los usuarios pueden contactar a soporte mediante soporte@loquesea.com o a info@loquesea2.loquesea"

matches = re.findall("(cadena)@(cadena)", text )
                         v        v
matches = re.findall("(\w+)@(\w+\.\w{2,})", text)
                                      ^dos de minimo .io .es pero pueden ser muchos .com  .loquesea
                                      
print(atches) ---> [('soporte','loquesea.com', ('info', 'loquesea2.loquesea'))]
                    dos tuplas               |



































____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  B U C L E S  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

for i in range(5): <--- 0 .. 4  
    print (i)
names = ["rosa","violeta","leonor"]
for name in names:
    print(name)
for indice,nombre in enumerate(nombres): <--- enumerate regresa 0 rosa 1 violeta ... 
    print(f"Nombre [{indice+1}]: {nombre}") 
#Diccionario
frutas = {"manzanas": 1, "platanos": 5, "kiwis": 3}
for fruta,cantidad in frutas.items: <--- para iterar un Diccionario
    print (f"Hay {cantidad} unidades de la fruta {fruta}")


#bucles anidados
my_List = [[1, 4, 5], [2, 6, 8], [1, 2, 3]] <--- Lista de listas
for element in my_list:
    print(f"Sublista: {element}\n")
    for subelement in element:
        print(subelements)

#bucles de compresion (for)
odd_list = [1, 3, 5, 7, 9]
#quiero una lista que contenga el cuadrado de cada elemento de la anterior [1, 9, 25, 49, 81]
cuadrado = [i ** 2 for i in odd_list]

---

#b r e a k 0 1 2 3 4 5
for i in range(10):
    print(i)
    if i == 5:
        break
        
#c o n t i n u e 0 1 2 3 4 6 7 8 9 
for i in range(10):

    if i == 5:
       continue  <----
                     |
    print(i)     <---- no va a imprimir el 5 continua con la siguiente iteracion

#e l s e  en bucles CHIVATO DE QUE EL BUCLE HA IDO BIEN
for i in range(10):

    if i == 10:
        break
else: #<--- este else es del bucle no del if de arriba que seria tabulado
    print("Bucle concluido exitosamente")

como el rango es de 0 1 2 ... 9  <--- nunca llega al 10 pero termina ok 

en cambio range(11) <--- aqui no termina ok 

#w h i l e 
---

i=0
while i <10:
    if i == 10:
      break
    i += 1
else:
    print("El bucle terminó normalmente") # este llega a 10 incremanta evalua y sale pero imprime el else No pasa por el break
# i < 16:  hace el break no imprime el else

---

#I F 
# if raro dentro de una cadena
edad=17
mensaje = "Eres mayor de edad" if edad =18 else "Eres menor de edad"
print(mensaje) # imprime Eres menor de edad


#AND /OR
edad = 20
nacionalidad = canaria 

if edad >=18 and nacionalidad == "canaria":
    print ("Puedes votar en Canarias")
else:
    print ("no Eres canario cabrón!")
    
#condicional anidado
if edad>= 18:
  if nacionalidad == "canaria":
    pass # <--- esto es no hace nada pero pasa continua 


---

____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  F U N C I O N E S  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

#parametros
def saludo(nombre):
    print(f"\nHola {nombre}")

saludo("Manu!")

#retorno de valor 
def suma (x, y):
    return x + y
print (f"\n[+] La suma de ambos valores es {suma(9, 3)}")

#ambito de bariables
las variables dentro de las funciones son locales a las funciones
las variables fuera de las funciones son globales por lo que su valor 
puede ser consumido / modificado FUERA de las funciones

variable = "soy global"
def cambioelvalor():
    variable ="soy local"  #<--- ESTA NO ES LA VARIABLE GLOBAL 
    print (variable)

cambioelvalor()
print(variable)

---> soy local 
---> soy global

#PERO SI CAMBIAS EL AMBITO ...

variable = "soy global"
def cambioelvalor():
    global variable ="soy local"  #<--- ESTA SI ES LA VARIABLE GLOBAL 
    print (variable)

cambioelvalor()
print(variable)

---> soy local 
---> soy global

---

____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  F U N C I O N E S  L A M B D A   * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

cuadrado = lambda x: x**2
print(cuadrado(7)) ---> 49


suma = lambda x, y: x + y
print(suma(1, 2)) ---> 3


En estructura de datos, hay que pensar qué regresa la estructura de datos,

numeros = [1, 2, 3, 4, 5] ---> regresa un elemento x  


M A P 
#map tiene dos argumentos una funcon y luego un iterable
#numeros es un objeto iterable porque es una lista
numeros = [1, 2, 3, 4, 5]
           lo enlista finalmente
            |     regresa un iterable por eso se usa mucho en funciones lambda
            |     |
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados) ---> [1, 4, 9, 16, 25]


F I L T E R 
#filter primer argumento una funcion segundo un iterable
#filter en funcion de si es true/false realiza la accion
numeros = [1, 2, 3, 4, 5]
cuadrados = list(filter(lambda x: x % 2 == 0, numeros)) <--- PARES 
print(cuadrados) ---> [2, 4]
IMPARES serían != 0

R E D U C E 
#multiplicar todos entre ellos
#reduce igual que map y filter tiene dos argumentos una funcion y un iterable
from functools import reduce 

numeros = [1, 2, 3, 4, 5]
resultado = (lambda x, y:  x+y, numeros) 
print(resultado) ---> 15 #suma de todos los elementos

primera vuelta x=1 y=2
segunda vuelta x=3 y=3
tercera vuelta x=6 y=4 ...

#lambda sobre diccionario con valor tuplas 
ventas_y_stock = {     ventas stock ( tupla (clave,valor))     
    "nombre juego 1": (400, 100),
    "nombre juego 2": (50, 20)
}                      ^   ^
                       |   |____ el valor no me interesa por eso se representa como _
                    ventas                  ^
                                            |
ventas_totales = lambda: sum(ventas for ventas, _ in ventas_y_stock.values())
                               |
                                \___> 400 + 50 en este caso 
                                
para imprimirlo: print(f"El total de ventas {ventas_totales()}")
                                                            ^
                                                            | imprescindible
                                         
                                         



Hace un sumatorio de las ventas de todos aquellos juegos que se hayan vendido mas de 50 unidades.
En este caso devolveria 400 porque 50 no es > que 50 ( del segundo juego , solo tengo dos juegos en ventas_y_stock)
tope = 50
                 lambda: ventas for loqetedevuelve
                                    en este caso 
                                    un dic con 
                                    clave y valor = tupla
                                        |                 |
                                        | e l e m e n t os|                   
                                        |                 | |  condiciones   
                                        clave tupla 2 elem| |                                           primer elem
                                        |      |          | |                                                  |
                                        v      v          | |                                                  v
ventas_totales = lambda: sum(ventas for juego, (ventas, _)  in ventas_y_stock.items() if ventas_y_stock[juego][0]>tope)
                                        ^               ^
                                        |               no interesa el valor  ( es el stock ) 
                                        nombre del juego del dic ventas_y_stock sería la clave "nombre juego 1"  
                                        porque el valor es una tupla por eje (400, 100)
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  E X C E P C I O N E S  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


try:
    num = 5/0 --------------------------------------
except ZeroDivisionError                            |
    print("No se puede dividir entre 0") <----------           
except TypeError                                    
    print("Solo numeros nada de strings ...") 


try:
    num = "hola"/0 ---------------------------------
except ZeroDivisionError                            |
    print("No se puede dividir entre 0")            |
except TypeError                                    |
    print("Solo numeros nada de strings ...") <-----

#e l s e ( cuando va benne y no entra en las excepciones)

try:
    num = 7/2
except ZeroDivisionError                            
    print("No se puede dividir entre 0")            
except TypeError                                    
    print("Solo numeros nada de strings ...") 
else:
    print(f"El resultado de la division es {num}")
    
#f i n a l l y ( SIEMPRE SE VA A EJECUTAR )

try:
    num = 7/2
except ZeroDivisionError                            
    print("No se puede dividir entre 0")            
except TypeError                                    
    print("Solo numeros nada de strings ...") 
else:
    print(f"El resultado de la division es {num}")
finally:
    print("ESTO SIEMPRE SE VA A EJECUTAR Y TIENE QUE IR COMO LA ULTIMA CLAUSULA DEL TRY CATCH")

#r a i s e  lanzar excepciones
x = -5
if x < 0:
    raise Exception("No se puede usar numeros negativos!")

peta y regresa la exception : "no se pueden utilizar numeros negativos" 





____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  M O D U L O   * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

Archivo de python que contiene definiciones de clases, variables y funciones, pueden ser importados. 
Librerías / packages ... 

#1 modulo de archivo que te has generado 
import unarchivodepythonconfunciones <--- sin el .py importa todas 
print(unarchivodepythonconfunciones.suma(3,2))
5

from unarchivodepythonconfunciones suma, resta, multiplicacion division <--- sin el .py y lo busca en el mismo directorio 
print ()

---

#2 modulo incorporado

import math 
print(dir(math)) ---> regresa propiedades tipo : pi pow prod radians ... 

y si solo necesitas importar una de ellas : 
from math import pow

---
para ver todos los modulos incorporados al propio interprete en python :
 
import sys 
print(sys.builtin_module_names)

por ejemplo hashlib  no viene has de importarlo si lo requieres
            _______

#3 modulo no incorporado, necesario descargar 
import hashlib 
hashlib.md5(b"cadenaconlabdeformatobitsdelante").hexdigest()
            ^
print(hashlib.__file__) ---> /usr/lib/python3.9/hashlib.py  <--- por si necesitas ampliar conocimiento de algun metodo y demas
                                                                 puedes abrirlo y revisarlo 
                                                                                                                             


---
I M P O R T A C I O N E S 
---

import math as m 
print(m.sqrt(49)) ---> 7 

from math import sqrt as raiz
print(raiz(49)) ---> 7

Python library Hijacking 
cuando en el interprete de python >>>> haces import sys

>>> import hashlib
>>> import sys 
>>> print(sys.path)  <--- esta es la cadena de sistios por los que busca cada import por primera vez ) 
['', '/usr/lib64/python311.zip', '/usr/lib64/python3.11', '/usr/lib64/python3.11/lib-dynload', '/home/abenito/.local/lib/python3.11/site-packages', '/usr/lib64/python3.11/site-packages', '/usr/lib/python3.11/site-packages']
  ^
  | esta es la clave intenta buscar el modulo primero en el dir de trabajo 
  por lo que puedes crearte uno con el nombre de hashlib u otro que sepas que se 
  importa y cuando vaya a usarlo usara el tuyo es una suplantacion 
  y si en el tuyo tiras de import  os ojo que esto te permite 
  ejecutar con root


>>> print(hashlib.__file__) -------------- ^
/usr/lib64/python3.11/hashlib.py --------- /
 

puedes montarte tu propio archivo : hashlib.py 






____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * *  P a c k a g e   * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


Objetivo, crear un paackage propio y subirlo a :
Pypi ( python package index )

pip3 install pwntools <--- viene de https://pypi.org 

hay que crear una cuenta vincular el movil 

touch /root/.pypirc 
    [pypi]
        username= __token__
        password = pypi-Agecsdvqdckp´dmcomtarç+delesepovcmeqfpovfeqveqwq <--- generado en la pagina perfil > account settings > api tokens 

---

abrpackage

mkdir abrpackage 

touch README.md setup.py

# cada paquete un directorio y dentro un __init__.py 
cd abrpackage


touch __init__.py <--- from .modulo1 import *  ESTO ES ARA QUE LUEGO PUEDAS HACER import modulo1 y pista 
                       from lodulo2 import * 
vi modulo1.py
   def list_courses():
   .
   .
   .

vi modulo2.py


con lo que has puesto en __init__ puedes hacer:
from abrpackage import list_courses() y puedes instanciarlo INSTEAD OF from abrpackage.modulo1 import list_courses()
list_courses()
 

tree 
|__ abrpackage 
|   |
|   |--- modulo1.py
|   |--- __init__.py
|   --- modulo2.py
|---Readme.md
|__ setup.py

para subir el package a pypi hay que incluir info en el setup.py 


from setuptools import setup, find_packages

# Leer el contanido del archuvo READE.md

with open("Readme.mc", "r", encoding="utf-8") as fh:
    long_description = fh.redad()
    
setup(
    name="abrpackage",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    author="ABR",
    description="lo que sea",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://abrpackage.io",
)

python3 -m build 

esto genera un dir nuevo llamado dist 

luego para subirla: twine upload dist/* --verbose 


pip3 cache purge ( es un comando para limpiar la cache ) 





____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * * I n p u t / O u t p u t * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


name = input("\n[+] Give me a name : ")
print(f"\n[+] Your name is : {name}")
      ^
      para que interprete la variable name como tal {}

typecating to numbers:

age = int(input("\n[+] Give your age :"))
print(f"\n[+] your next birthay will be {age+1} years")


try:
    age = int(input("\n[+] Give your age :"))
    print(f"\n[+] your next birthay will be {age+1} years")
    break
except ValueError:
    print(f"\n[+] The input data type is not correct")


Para ocultar el output 
     se importa como un modulo pero es un script realmente del interprete <----
        ^                                                                      |
from getpass import getpass <--- parece una function pero es una var           |
     ---------------------------------------------------------------------------                                                           
    |
python3 

>>> import getpass 
>>> print(getpass,__file__)
/usr/lib/python3.9/getpass.py
>>>

puedes hacerle cat y ves como funciona 

---

from getpass import getpass
password = getpass(input("\n[+] Give your password :"))
print(f"\n[+] The password is {password}")


____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

                                  * * * R e a d  / W r i t e  FILE * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________


f = open("/etc/hosts", "r") ---> Readme
f = open("/etc/hosts", "a") ---> Write append añade a lo que ya exista 
f = open("/etc/hosts", "w") ---> Write y no conserva el contenid previo 

f.write("Hi!\n")
f.close()

ya no podrias seguir usandolo sin hacer un open : f.write("writing!\n")

#write
with open("example.txt","w") as f:   <--- es más óptimo python se ocupa de cerrarlo y evitar errores
    f.write("Hi!")    
    
tambien se puede con el print : 
    print("Hi!", file=f)

Para escribir desde una lista en un archivo: 

lista = ["Primera linea\n", "Segunda Linea\n", "Tercera linea\n"]

with open("example.txt", "w") as f:
    f.writelines(lista)




#read 
with open("example.txt","r") as f:   <--- es más óptimo python se ocupa de cerrarlo y evitar errores
    file_content = f.read()    
print(file_content)


#read
si quieres ir leyendo linea por linea y que muestre el contenido, es un objeto iterable:
#read line in f NO crga en memoria el archivo entero, es muy óptimo
with open("example.txt","r") as f:   <--- es más óptimo python se ocupa de cerrarlo y evitar errores
    for line in f:    
        print(line.strip()) <--- strip para quitar \n de cada linea 
        
"r" = read pero si el archivo contiene binario o caracteres que se dan de ostias ocn unicode mejor "rb" raw binary


#read Con readlines() carga en memoria el archivo entero CUIDADO
with open("example.txt","rb") as f:   <--- es más óptimo python se ocupa de cerrarlo y evitar errores
    for line in f.readlines(): <----------------     
        print(line.strip())  
        
Es util para leer la Primera linea: en lugar de readlines() usar readline()


#b i n a r i o s 
with open("/ruta/foto.png","rb") as f_in, open("image.png", "wb") as f_out:
    file_content = f_in.read()   # todo el contenido del archivo lo mete en file_content
    f_out.write(file_content)    # lo guardo en image.png que es el f_out 

































b a c k l o g 
____________________________________________________________________________________________________________________________________

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
____________________________________________________________________________________________________________________________________

                                  * * *  O r i e n t a c i o n  O b j e t o s  * * *
____________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________

Concepto: Self hace referencia al objeto ( objalb en este caso ) que le llega a la clase.


                                                            ___ esto no esta pero esta es el self
class Persona:                                             /
    #constructor qu no deja de ser un metodo               v
    def __init__(self, nombre, edad=21): # Persona.__init__(objalb,nombre, edad)
                                    ^
        self.nombre = nombre        |___ si no le llega nada del objeto por defecto valdra 21 
        sef.edad = edad 
    
    def saludo(self): #Persona.saludo(objalb) <--- el objeto que le llega de la instanciacion
        return f"Hola,soy {self.nombre} y tengo {self.edad} años!"
    
---    
    
objAlb = Persona("Alb", 39) #<--- objeto de la clase
objEva = Persona("Eva")
print(objAlb.saludo()) ---> Hola, soy Alb y tengo 39 años!
print(objEva.saludo()) ---> Hola, soy Eva y tengo 21 años!
 


Concepto: Comprender como actualizar valores del objeto :

class CuentaBancaria:
    def __init__(self, cuenta, nombre, dinero=0):
        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero
        
    def depositar_dinero(self, dinero):
        self.dinero += dinero
        return f"\n[+] Se han depositado {dinero}" euros, el balance actual de la cuenta es {self.dinero} euros."
    
    def retirar.dinero(self, dinero):
        if dinero > self.dinero:
            return f"\n[+] Operación no permitida, no dispone de fondos suficientes."
        
        self.dinero -= dinero
        return f"\n[+] Se han extraido {dinero} eurs d ela cuenta, y el balance actual es {self.dinero}"

---
objAlb = CuentaBancaria("1229802383", "alb y eva account", 1000)
print(objAlb.depositar_dinero(500)) ---> Se han depositado 500 euros, el balance actual de la cuenta es 500 euros.
print(objAlb.retirar_dinero(2000))  ---> Operación no permitida, no dispone de fondos suficientes.
print(objAlb.retirar_dinero(200))   ---> Se han extraido 200 euros de la cuenta, y el balance actual es de 300 euros.


Concepto: Decoradores y métodos específicos.

class Rectangulo: 
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    @property #<-------- rect1.area 
    def area(self) # le llega el objeto que ha definido en el constructor ancho y largo sobre self
        return self.ancho * self.alto 

    def __str__(self):
        return f"\n[+] Propiedades del rectángulo: [Ancho: {self.ancho}][Alto: {self.alto}]"
    def __eq__(self, otro):
        return self.ancho = otro.ancho and self.alto = otro.alto
         
---

rect1 = Rectangulo(10, 20)
rect2 = Rectangulo(5, 5)



printf(f"\n[+] el área es {rect1.area()}") ---> El área es 1600 

#d e c o r a d o r                                      ^
#si le plantas el decorador @property no hace falta ()
printf(f"\n[+] el área es {rect1.area}") ---> El área es 1600  
#permite acceder al valor de retorno del metodo 
#ese es el concepto de @property como tal
                                    ^

#m e t o d o s  e s p e c i a l e s
__str__
print(rect1) #con __str__ definimos lo que ha de mostrar en caso de tratar de imprimir un objeto ( si no lo defines imprime obj type ...)
__eq__ 
print(f"\n[+] ¿Son iguales los dos rectángulos? -> {rect1 ==rect2}")# esto hace magia, al estar definido __eq__ regresa true o false 



concepto: metodos normales self : operaciones que deben realizarse en la instancia 
funcionalidad dependiente de la instancia concreta.
__________________________________________________ 

class Persona: 
    total_personas = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print("Hola", self.nombre) #necesitas instanciar para saludar a cada uno personalmente, hola juan hola pepe 
    def presentacion(self):
        print(f"Hola soy {self.nombre}")   
        

alb = Persona("alberto")
alb.presentacion() ---> Hola soy alberto
 ^
 |
objeto 

Más de self : 
    class Calculadora:
        def __ini__(self, numero): #CAlculadora.__init__(calc, numero)
            self.numero = numero # calc.numero = 5
           
concepto: metodo de clase cls : operaciones que deben realizarse en la clase DEPENDEN DE LA CLASE LLAMANTE EN HERENCIA
funcionalidad dependiente de atributos de clase.
________________________________________________

class Persona: 
    total_personas = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.total_personas + 1
    
    @classmethod
    def contar_personas(cls): # si llamas a este metodo de clase se crea una instancia de clase y se incrementa el contador total personas
        return f"+ 1 persona"

concepto: metodo estático : son llamados sin crear una instancia, se llaman directamente desde la clase MiClase.metodo_estatico()
funcionalidad NO dependiente de instancia ni de Atributos de clase.
___________________________________________________________________ 

class MiClase:
    variable_clase ="A"
    
    @staticmethod
    def metodo_estatico():
        return variable_clase + variable_clase ---> AA

---

Más ejemplos:
    
class Libro:
    IVA = 0.21
    
    def __init__(self, titulo autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio 
        
    @staticmethod
    def es_bestseller(total_ventas): #Libro.es_bestseller(mi_libro, total_ventas)
        return total_ventas > 5000
    
    @classmethod
    def precio_con_iva(cls, precio):
        return precio + precio * cls.IVA

class LibroDigital(Libro): # <--- hereda de Libro
      #otro iva para los libros digitales
      IVA = 0.1


mi_Libro = Libro("El quijote", "Cervantes", 100)
print(f"\n[+] El precio del libro con IVA es de {Libro,precio:con_iva(mi_libro.precio)}")

#para el ejemplo de digital 
mi_libro_digital = Libro("El quijote2", "Cervantes", 100)
print(f"\n[+] El precio del libro con IVA es de {LibroDigital,precio:con_iva(mi_libro_digital.precio)}")
#SI EN LUGAR DE @classmethod HUBIERA SIDO @staticmethod  el IVA sobre el digital no se hubiera aplicado
#PARA ESO ES UN CLASSMETHOD PARA QUE DEPENDA DE LA CLASE LLAMANTE AQUI EN HERENCIA SE VE MEJOR QUE ANTES

---

Concepto: refuerzo metodos estaticos.

class Calculadora:
    
    @staticmethod
    def suma(num1, num2):
        return num1 + num2
    @staticmethod
    def resta(num1, num2):
        return num1 - num2
    @staticmethod
    def multiplicacion(num1, num2):
        return num1 * num2
    @staticmethod
    def dividir(num1, num2):
        return num1 / num2 if num2 !0 0 else "\n[!] Error: No se puede dividir un número entre cero\n"

print(Calculadora.suma(2, 8))
print(Calculadora.resta(2, 8))
print(Calculadora.multiplicacion(2, 8))
print(Calculadora.dividir(2, 8))

Concepto: refuerzo metodos de clase y estaticos:

class Estudiantes:
    
    #VARIABLE DE CLASE
    estudiantes = []
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Estudiantes.estudiantes.append(self)
    
    #no necesita self no trabaja sobre la instancia
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18
    
    #esto genera un estudiante y no inserta en la lista de estudiantes con append
    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if cls.es_mayor_de_edad(edad):
            return cls(nombre, edad)
        else:
            print(f"\n[!] Error: El estudiante {nombre} es menor de edad\n")
    
    @staticmethod
    def mostrar_estudiante(): #iterar por estudiantes
        for i, estudiante in enumerate(Estudiantes.estudiantes):
            print(f"\t[+] estudiante número [{i+1}]: {estudiante.nombre}")


Estudiantes.crear_estudiante("primerEstudiante", 43)
Estudiantes.crear_estudiante("segundoEstudiante", 15)
Estudiantes.crear_estudiante("tercerEstudiante", 12)

Estudiantes.mostrar_estudiantes()


FALTAN PROPIEDADES DECORADORES ... 

---
