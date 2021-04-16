# Expresiones regulares: son patrones de coincidencia de texto descritos con una sintaxis formal. Los patrones se interpretan como un conjunto de instrucciones, que luego se ejecutan con una cadena como entrada para producir una subconjunto de coincidencia o una versión modificada del original.
print("Expresiones regulares")

# Importaremos las librerías necesarias
import re

# Métodos de las expresines regulares
print("\n- Métodos de las expresiones regulares")

print()
# re.search(patrón,string): busca un patrón en una cadena
print("\nre.search()")

# Creación del string1 para el ejemplo
string1 = "Cada día es una nueva oportunidad para cambiar tu vida"
print("\nLa frase 1 es: ", string1)

# Uso del método search para encontrar la palabra 'oportunidad' en la frase del string1
search1 = re.search("oportunidad", string1)

# Con un condicional verificamos si la palabra está o no en la frase 1
if search1:
  print("\nEncontramos la palabra 'oportunidad' en la frase 1: \n",search1)
else:
  print("\nNo encontramos la palabra 'opotunidad' en la frase 1")

# start(), end(), span(): En orden respectivo: posición donde empieza la coincidencia (match), posición donde termina la coincidencia, tupla con posiciones donde empieza y termina la coincidencia

# start()
print("\nPosición donde empieza el match de 'oportunidad' en la frase 1: \n", search1.start())

# end()
print("\nPosición donde termina el match de 'oportunidad' en la frase 1: \n", search1.end())

# span()
print("\nPosiciones en las que empieza y termina el match de 'oportunidad' en la frase 1: \n", search1.span())

print()
# re.match(patrón,string): busca un patrón al principio de una cadena
print("\nre.match()")

# Creación del string2 para el ejemplo
string2 = "Ningún mar en calma hizo experto a un marinero"
print("\nLa frase 2 es: ", string2)

# Uso del método match para ver si 'mar' está al principio de  la cadena
match1 = re.match("mar", string2)

# Con un condicional verificamos si la palabra está o no al inicio de la frase 2
if match1:
  print("\nEncontramos la palabra 'mar' al principio de la frase 2: \n",match1)
else:
  print("\nNo encontramos la palabra 'mar' al principio de la frase 2")

print()
# re.split(pattern, string, [maxsplit=0]): divide una cadena a partir de un patrón
print("\nre.split()")

# Creación del string3 para el ejemplo
string3 = "No busques el momento perfecto, solo busca el momento y hazlo perfecto"
print("\nLa frase 3 es: ", string3)

# Uso del método split para dividir la frase cada que encuentre una 'to'
split1 = re.split("to", string3)

# Con un condicional verificamos si el split planteado peude realizarse en el string3
if split1:
  print("\nDividir la cadena, cada vez que se encuentre un 'to' en el string 3: \n",split1)
else:
  print("\nNo encontramos 'to' en la frase 3 para realizar la división")

# El output del split, podemos limitarlo a que solo nos arroje una cantidad específica de partes en las que se dividió.

# Para limitar esa cantidad de output, utilizamos maxsplit, en este caso, imprimiremos las primeras 2 partes resultantes de la división en 'to' y el resto de la cadena, normalmente
split2 = re.split("to", string3, maxsplit=2)

# split con maxsplit = 2
print("\nDividir la cadena cada vez que encuentre 'to', y  mostrar las 2 primeras partes de la división: ", split2)

print()
# re.findall(patrón,string): busca todas las coincidencias en una cadena
print("\nre.findall()")

# Creación del string4 para el ejemplo
string4 = "Cuando cuentas cuentos, cuenta cuántos cuentos cuentas, porque si no cuentas cuántos cuentos cuentas, no sabrás cuántos cuentos sabes contar"
print("\nLa frase 4 es: ", string4)

# Uso del método findall para obtener todas las coincidencias 'cuentas' en la frase 4 
findall1 = re.findall("cuentas", string4)

# Con un condicional verificamos si el findall planteado puede realizarse en el string4
if findall1:
  print("\nLista que contiene todas las coincidencias de 'cuentas' de la frase 4: \n",findall1)
else:
  print("\nNo se encontraron coincidencias con tal patrón")

print()
# re.sub(patrón, reemplazo, string): sustituye todas las coincidencias en una cadena
print("\nre.sub()")

# Para este ejemplo usaremos la frase 4, para notar mejor su funcionalidad
print("\nFrase 4: ", string4)

# Uso del método sub para cambiar 'cuentos' por 'poemas' en la frase 4
sub1 = re.sub("cuentos","poemas",string4)

# Con un condicional verificamos si el sub() planteado puede realizarse en el string4
if sub1:
  print("\nReemplazar 'cuentos' por 'poemas' en la frase 4: \n",sub1)
else:
  print("\nNo se encontraron coincidencias con tal patrón para hacer el reemplazo")

# Patrones con varios valores: en un mismo método, indicar 2 patrones a encontrar en el string, con findall()
print("\nre.findall() y 2 patrones")

# Frase 5
string5 = "Bienvenidos a todos, welcome everyone"
print("\nLa frase 5 es: ", string5)

# Uso de finall() con 2 patrones
findall2 = re.findall("Bienvenidos|welcome", string5)

# Mostrar el resultado luego del método
print("Resultado: ", findall2)

print()
print("----------"*7)

# Meta-carácter
print("\nMeta-carácter - findall()\n")

# meta-carácter *: definir ninguna o más repeticiones de la letra a la izquierda del meta-carácter:
# meta-carácter +: definir una o más repeticiones de la letra a la izquierda del meta-carácter
# meta-carácter ?: definir una o ninguna repetición de la letra a la izquierda del meta-carácter

# Creación del string a modificar
string = "lva lava laava laaava laaaaaava"

# Método findall() y mostrar el resultado del meta-caracter 1
meta1 = re.findall(r'la*', string)
print(meta1)

# Método findall() y mostrar el resultado del meta-caracter 2
meta2 =  re.findall(r'la+', string)
print(meta2)

# Método findall() y mostrar el resultado del meta-caracter 3
meta3 =  re.findall(r'la?', string)
print(meta3)

# Método findall() y mostrar el resultado del meta-caracter 3 de otro modo
meta4 =  re.findall(r'la?va', string)
print(meta4)

print()
print("----------"*7)

# Rangos: la capacidad de definir algunos rangos. Ej: [a-z]: Cualquier carácter alfabético en minúscula (no especial ni número); [0-9]: Cualquier carácter numérico (no especial ni alfabético).
print("\nRangos")

# Ejemplo 1
print("\nEjemplo")

# Creación del string 6
string6 = "comida c0mid4"

# Patrón 1 con findall() usando el rango [a-z] y mostrar el resultado
rango1 = re.findall("c[a-z]mida", string6)
print("Con el rango [a-z]: ",rango1)

# Patrón 2 con findall() usando el rango [0-9] y mostrar el resultado
rango2 = re.findall("c[0-9]mid[0-9]", string6)
print("Con el rango [0-9]: ",rango2)

print()
print("----------"*7)

# Caracteres escapados con significado único. Evita crear grandes y diversos rangos
print("\nCarácteres escapados")

#\d	numérico
#\D	no numérico
#\s	espacio en blanco
#\S	no espacio en blanco
#\w	alfanumérico
#\W	no alfanumérico

# Crear y mostrar el string 7
string7 = "Hace 109 años, se hundió el Titanic"
print("La frase 7 es: ",string7)

# En todos los ejemplos siguientes, utilizaremos el método findall()

#\d numérico: sirve para encontrar solo caracteres numéricos
print("\nUso \d : numérico")
escapado1 = re.findall(r"\d+",string7)
print(escapado1)

#\D no numérico: sirve para encontrar caracteres de letras 
print("\nUso \D : no numérico")
escapado2 = re.findall(r"\D+",string7)
print(escapado2)

#\s espacio en blanco: sirve para mostrar los caracteres que corresponden a espacios en blanco del string 7
print("\nUso \s : espacios en blanco")
escapado3 = re.findall(r"\s+",string7)
print(escapado3)

#\S no espacio en blanco: sirve para mostrar los caracteres que no corresponden a espacios en blanco del string 7
print("\nUso \S : no espacios en blanco")
escapado4 = re.findall(r"\S+",string7)
print(escapado4)

#\w alfanumérico: sirve para mostrar los caracteres alfanuméricos del string 7
print("\nUso \w : alfanumérico")
escapado5 = re.findall(r"\w+",string7)
print(escapado5)

#\W no alfanumérico: sirve para mostrar los caracteres no alfanuméricos del string 7
print("\nUso \W : no alfanumérico")
escapado6 = re.findall(r"\W+",string7)
print(escapado6)
