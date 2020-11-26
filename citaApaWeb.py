process = int(input("Ingrese los datos solicitados para generar la cita y la referencia de una pagina web: 1. Página web con un autor individual, 2. Pagina Web de una organizacion con autor corporativo"))

if (process==1):

    lastName = input("Ingrese los apellidos") 
    initialsName = input("Ingrese iniciales del nombre Ejm R.A") 
    day = input("ingrese dia") 
    mount = input("ingrese mes") 
    year = input("Ingrese año") 
    title = input("Ingrese título") 
    websiteName = input("Ingrese nombre del sitio web") 
    websiteUrl = input("ingrese url del sitio web") 
    print(lastName + ", " + year) 
    print(lastName + ", " + initialsName +" (" + day + " de " + mount + " de " + year + "). " + title + ". " + websiteName + ". " + "Recuperado de: " + websiteUrl) 
elif (process==2):
    print("Ingrese los datos solicitados") 
    organizationName = input("Ingrese nombre de la organizacion") 
    day = input("ingrese dia") 
    mount = input("ingrese mes") 
    year = input("Ingrese año") 
    title = input("Ingrese título de la pagina web") 
    institutionUrl = input("Ingrese url de la intitucion") 
    organizationabbreviation = input("Ingrese editorial") 
    link = input("Ingrese enlace") 
    print(" (" +organizationName+ " ["+ organizationabbreviation+ "]" +", "+ year+  ")") 
    print(organizationName + " (" + day + " de " + mount + " de " + year + "). " + title + ". " + institutionUrl  ) 
else: 
    print("error en el ingreso de datos, ")
 

