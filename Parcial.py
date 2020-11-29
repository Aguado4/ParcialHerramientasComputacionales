def cafeterias():
    clientes=int(input("Introduzca el número de clientes que se va a atender: "))
    for i in range(clientes):
        rol=int(input("Ingrese el número 1 si es estudiante o 0 si es profesor: "))
        cédula=input("Ingrese su cédula: ")
        código=input("Introduzca el código del producto: ")
        cantidad=int(input("Introduzca la cantidad de unidades: "))
        precio=int(input("Introduzca el precio del producto: "))
        if rol==1:
            rol="estudiante"
            valor=precio*0.5*cantidad
            print("El %s con cédula %s, debe pagar %s por el producto %s"%(rol,cédula,valor,código))
            print(" ")
        elif rol==0:
            valor=precio*0.8*cantidad
            rol="profesor"
            print("El %s con cédula %s, debe pagar %s por el producto %s"%(rol,cédula,valor,código))
            print(" ")
        else:
            print("Error")
cafeterias()
