import csv
acum=0
def cate(por):
    if porcentaje>=0 and porcentaje<=25:
        categoria="Chiste"
    elif porcentaje>=26 and porcentaje<=50:
        categoria="Anécdota"
    elif porcentaje>=51 and porcentaje<=75:
        categoria="Peligro"
    elif porcentaje>=76 and porcentaje<=99:
        categoria="Atención"
    elif porcentaje==100:
        categoria="Esclavitud"
    return categoria

lista=[]
while(True):
    print("---------- M E N Ú ----------\n\n")
    print("1. Agregar plan ")
    print("2. Listar planes")
    print("3. Eliminar plan por ID")
    print("4. Generar bbdd")
    print("5. Cargar bbdd")
    print("6. Estadísticas")
    print("0. Salir\n")
    op=int(input("Ingrese una opción\n"))
    if op==1:
        print("-------- AGREGAR PLAN ---------\n")
        ide=int(input("Ingrese el id\n"))
        nombre=input("Ingrese el nombre\n")
        porcentaje=int(input("Ingrese el porcentaje\n"))
        while(porcentaje<0 or porcentaje>100):
            print("Error. El porcentaje debe estar entre 0 y 100")
            porcentaje=int(input("Vuelva a ingresar el porcentaje\n"))
        cate(porcentaje)
        categoria=cate(porcentaje)
        diccionario={"ide":ide,"nombre":nombre,"porcentaje":porcentaje,"categoria":categoria}
        lista.append(diccionario)
        
    elif op==2:
        print("-------- LISTAR PLANES --------\n")
        for l in lista:
            print("ID:",l["ide"],". Nombre:",l["nombre"],". Porcentaje:",l["porcentaje"],". Categoria:",l["categoria"])
            print("---------------------------------------------------------------")
            print("")
                  
    elif op==3:
        encontrado=False
        print("-------- ELIMINAR PLAN POR ID --------\n")
        ide=int(input("Ingrese el id del plan\n"))
        for l in lista:
            if ide==l["ide"]:
                print("Datos del plan encontrado:\n")
                print("ID:",l["ide"],". Nombre:",l["nombre"],". Porcentaje:",l["porcentaje"],". Categoria:",l["categoria"])
                print("")
                encontrado=True
                break
        if encontrado:
            while(True):
                print("¿Está seguro de querer eliminar el plan?\n")
                print("1. Sí")
                print("2. No\n")
                op=int(input("Ingrese una opción\n"))
                if op==1:
                    for l in lista:
                        if ide==l["ide"]:
                            lista.remove(l)
                            print("Plan eliminado correctamente\n")
                            print("")
                            break
                    break
                elif op==2:
                    print("Volviendo al menú principal\n")
                    break
                else:
                    print("Ingreso no válido. Vuelva a ingresar una opción\n")
        if encontrado==False:
            print("El plan no está en la lista\n")

    elif op==4:
        print("-------- GENERAR BBDD ---------\n")
        with open("bbdd_plan.csv","w",newline="") as bbdd_plan:
            campos=["ide","nombre","porcentaje","categoria"]
            escritor_csv=csv.DictWriter(bbdd_plan,fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(lista)
        print("Archivo generado corretamente\n")
        
    elif op==5:
        print("-------- CARGAR BBDD ----------\n")
        with open("bbdd_plan.csv","r",newline="") as bbdd_plan:
            lector_csv=csv.DictReader(bbdd_plan)
            for fila in lector_csv:
                lista.append(fila)
        print("Archivo cargado correctamente\n")

    elif op==6:
        print("-------- ESTADÍSTICAS ---------\n")
        elementos=len(lista)
        for l in lista:
            acum=acum+int(l["porcentaje"])
            alto=max(int(l["porcentaje"]) for l in lista)
        promedio=int(acum/elementos)
        print("El porcentaje de efectividad promedio es de:",promedio)
        print("El plan con el mayor porcentaje de efectividad:",alto)
        print("")
        
    elif op==0:
        print("Saliendo del sistema")
        break
    else:
        print("Opción no válida. Vueva a ingresar una opción\n")
