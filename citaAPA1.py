print("Ingrese los datos solicitados")

condition = input(1)
if condition:1
else:
    print("Libro con autor personal")
    lastName = input("Ingrese apellidos: ")
    initialName = input("Ingrese iniciales del nombre Ej. R.A.: ")
    year = input("Ingrese año: ")
    title = input("Ingrese título: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    print(" (" + lastName + ", "  + year + ").")
    print(lastName + ", " + initialName +" (" + year + "). " + title +  ". " + city + ". " + publisher + ".")
condition = input(2)
if condition:2
else:
    print("Libro con institución como autor")
    corporativeName = input("Ingrese Institución: ")
    year = input("Ingrese año: ")
    title = input("Ingrese título: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    print(" (" + corporativeName + ", "  + year + ").")
    print(corporativeName +" (" + year + "). " + title +  ". " + city + ". " + publisher + ".")
condition = input(3)
if condition:3
else:
    print(3)
    print("Libro sin autor: ")
    title = input("Ingrese título: ")
    year = input("Ingrese año: ")
    city = input("Ingrese ciudad: ")
    publisher = input("Ingrese editorial: ")
    print(" (" + title + ", "  + year + ").")
    print(title +" (" + year + "). " + city + ". " + publisher + ".")