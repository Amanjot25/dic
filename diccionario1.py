#coding:utf8

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
