#coding:utf8

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
