import json

def inputData(type):
    year = input("Ingrese año")
    title = input("Ingrese título")
    city = input("Ingrese ciudad")
    publisher = input("Ingrese editorial")
    link = input("Ingrese enlace")
    returnJson='{​​"year":'+year+',"title":'+title+'"city":'+city+'"publisher":'+publisher+'"link":'+link+'}​​​'
    
condition = int(input("Ingrese los datos solicitados para generar la cita de un libro electrónico: 1. autor personal, 2. autor Institucional, 3. sin autor"))
if condition==1:
    lastName = input("Ingrese los apellidos")
    initialsName = input("Ingrese iniciales del nombre seguido de punto")
    year = input("Ingrese año")
    title = input("Ingrese título")
    city = input("Ingrese ciudad")
    publisher = input("Ingrese editorial")
    link = input("Ingrese enlace")
    print(lastName + ", " + initialsName +" (" + year + "). " + title +  ". " + city + ". " + publisher + ". " + "Recuperado de: " + link)
elif condition==2:
    print("Ingrese los datos solicitados")
    corporativeName = input("Ingrese Instituciòn")
    year = input("Ingrese año")
    title = input("Ingrese título")
    city = input("Ingrese ciudad")
    publisher = input("Ingrese editorial")
    link = input("Ingrese enlace")
    print(corporativeName +" (" + year + "). " + title +  ". " + city + ". " + publisher + ". " + "Recuperado de: " + link)
elif condition==3:
    print(3)
    print("Ingrese los datos solicitados")
    title = input("Ingrese título")
    year = input("Ingrese año")
    city = input("Ingrese ciudad")
    publisher = input("Ingrese editorial")
    link = input("Ingrese enlace")
    print(title +" (" + year + "). " + city + ". " + publisher + ". " + "Recuperado de: " +  link)
else: 
    print("error en el ingreso de datos")
