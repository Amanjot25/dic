#coding:utf8

<<<<<<< HEAD
numero = int(input("Díme cuántas palabras quieres introducir: "))
diccionario={}
if numero < 1:
    print("¡Imposible!")
else:
  for i in range (numero):
           print ("Ingrese la palabra")
           palabra = raw_input()
           desc= raw_input()
           diccionario[palabra]=desc
  print("El diccionario es:",diccionario)
=======
numero = int(input("Dígame cuántas palabras quieres introducir: "))

if numero < 1:
    print("¡Imposible!")
else:
  diccionario= ()
  for i in range (numero):
    print ("Ingrese la palabra")
    palabra = raw_input()
    defin= raw_input()
  diccionario[palabra]=defin
print("El diccionario es:",diccionario)
>>>>>>> b713e9be570bc6c30326141c569400eba9231f59
