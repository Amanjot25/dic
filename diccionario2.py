#coding:utf8

dic1={}
dic2={}
cant=input("Dime las palabras y definiciones que quieres introducir?")
for i in range(1,cant+1):
    palabra=raw_input("Dime la palabra ")
    defin=raw_input("Dime la definición para la palabra ")
    defin_idioma2=raw_input("Dime la definición para la palabra ")
    dic1[palabra]=defin
    dic2[palabra]=defin_idioma2
print "El diccionario creado en el primer idioma es: ",dic1
print "El diccionario en el segundo idioma es: ",dic2


