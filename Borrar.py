import csv
lista=[]
acum=0


def menu():
    print("------------ M E N Ú --------------\n\n")
    print("1. Agregar producto")
    print("2. Listar todos los productos")
    print("3. Eliminar un producto por id")
    print("4. Generar archivo csv")
    print("5. Cargar archivo csv")
    print("6. Estadísticas")
    print("0. Salir\n")

def datos():
    print("ID:",p["ide"],". Nombre:",p["nombre"],". Precio:",p["precio"])


while(True):
    menu()
    op=int(input("Ingrese una opción\n"))
    if op==1:
        print("--------- AGREGAR PRODUCTO ---------\n")
        ide=input("Ingrese el id del producto\n")
        nombre=input("Ingrese el nombre del producto\n")
        precio=int(input("Ingrese el precio del producto\n"))
        diccionario={"ide":ide,"nombre":nombre,"precio":precio}
        lista.append(diccionario)

    elif op==2:
        print("--------- LISTAR PRODUCTOS ----------\n")
        for p in lista:
            datos()
            print("-----------------------------------")
            print("")
            
    elif op==3:
        encontrado=False
        print("--------- ELIMINAR UN PRODUCTO POR ID ------------\n")
        ide=input("Ingrese el id del producto\n")
        for p in lista:
            if ide==p["ide"]:
                print("Datos del producto encontrado\n")
                datos()
                print("-----------")
                print("")
                lista.remove(p)
                print("Producto eliminado correctamente\n")
                encontrado=True
                break
        if encontrado==False:
            print("El producto no está en lista\n")
                
        
    elif op==4:
        print("--------- GENERAR ARCHIVO CSV ---------\n")
        with open("bbdd_productos.csv","w",newline="") as bbdd_productos:
            campos=["ide","nombre","precio"]
            escritor_csv=csv.DictWriter(bbdd_productos,fieldnames=campos)
            escritor_csv.writeheader()
            escritor_csv.writerows(lista)
        print("Archivo generado correctamente\n")
              
    elif op==5:
        print("--------- CARGAR ARCHIVO CSV ----------\n")
        with open("bbdd_productos.csv","r",newline="") as bbdd_productos:
            lector_csv=csv.DictReader(bbdd_productos)
            for fila in lector_csv:
                lista.append(fila)
        print("Archivo cargado correctamente\n")

    elif op==6:
        print("--------- ESTADÍSTICAS --------------\n")
        for p in lista:
            acum=p["precio"]+acum
        elementos=len(lista)
        promedio=int(acum/elementos)
        print("Hay",elementos,"productos en la lista")
        print("Precio total de los productos:",acum)
        print("Promedio:",promedio)
        print("")
        
    elif op==0:
        print("Saliendo del sistema")
        break
    else:
        print("Opción no válida. Vuelva a ingresar una opción\n")
    
