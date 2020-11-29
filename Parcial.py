def cafeterias():
    rol=int(input("Ingrese el número 1 si es estudiante o 0 si es profesor: "))
    cédula=input("Ingrese su cédula: ")
    código=input("Introduzca el código del producto: ")
    cantidad=int(input("Introduzca la cantidad de unidades: "))
    precio=int(input("Introduzca el precio del producto: "))
    valor="Error, entrada invalida"
    if rol==1:
        rol="estudiante"
        valor=precio*0.5*cantidad
        print("El %s con cédula %s, debe pagar %s por el producto %s"%(rol,cédula,valor,código))
    elif rol==0:
        valor=precio*0.8*cantidad
        rol="profesor"
        print("El %s con cédula %s, debe pagar %s por el producto %s"%(rol,cédula,valor,código))
    else:
        print("Error")
cafeterias()
