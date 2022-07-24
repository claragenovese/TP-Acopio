from os import system, name
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

seleccionPrincipal = -1
camionesSoja = 0
camionesMaiz = 0
pNetoSoja = 0
pNetoMaiz = 0
mayorCantSoja = -1
menorCantMaiz = -1
patenteMayorSoja = '0'
patenteMenorMaiz = '0'
menuPrincipal = ["1 - Administraciones","2 - Entrega de Cupos","3 - Recepcion","4 - Registrar Calidad","5 - Registrar Peso Bruto","6 - Registrar Descarga","7 - Registrar Tara","8 - Reportes","0 - Fin del programa"]
menuAdministraciones = ["A - Titulares","B - Productos","C - Rubros","D - Rubros x Producto","E - Silos","F - Sucursales","G - Producto Por Titular","V - Volver al Menu Principal"]
menuABM = ["A - Alta", "B - Baja","C - Consulta","M - Modificacion","V - Volver al Menu Anterior"]

poolProductos = ["TRIGO","SOJA","MAIZ","GIRASOL","CEBADA"]
productos = ["SOJA","",""]
patenteData = [["paten1","","","","","","",""],["","","","","","","",""]]
productosCamiones = ["SOJA","","","","","","",""]
pesosArr=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]] # PESO BRUTO / TARA
# FUNCIONES GENERALES



def clear():
   if name == 'nt':
        _ = system('cls')
   else:
        _ = system('clear')

def imprimirMenu(arrMenu,longArr):
    prYellow("------")
    for i in range(0,longArr):
        prPurple(arrMenu[i])
    prYellow("------")

def elegirElementoDeMenu(esEntero = False):
    if(esEntero == True):
        resultado = int(input("--- Seleccionar un submenu ---\n"))
    if(esEntero == False):
        resultado = input("--- Seleccionar un submenu ---\n")
    return resultado
    
def imprimirMenuEnConstruccion(menu):
    print("El menu:",menu,"esta en construccion\n")
    
def elementoEnArreglo(elemento,arr,longArr):
    for i in range(longArr):
        if(elemento == arr[i]):
            return True
    return False

def ingresarPrimerLugarVacio(elemento,arr,longArr):
    for i in range(longArr):
        if(arr[i] == ""):
            arr[i] = elemento
            return 
    return print("No habia posiciones vacias")

        
def esArregloLleno(arr,longArr):
    for i in range(0,longArr):
        if(arr[i]==""):
            return False
    return True

def esArregloVacio(arr,longArr):
    for i in range(0,longArr):
        if(arr[i]!=""):
            return False
    return True
    
def imprimirElementosDeArreglo(arr,longArr):
    if(esArregloVacio(arr,longArr)):return prYellow("Sin elementos")
    for i in range(longArr):
        if(arr[i]!=""):
            print(i, "-" ,arr[i])

def buscarElementoEnArreglo(el,arr,longArr):
    for i in range(0,longArr):
        if(arr[i]==el):
            return i
    return -1
   
def acumularSiCondicion(arr,condicion,distinto = False):
    acumulador = 0
    for i in range(0,8):
        if(distinto):
            if(arr[i] != condicion):
                acumulador = acumulador + 1
        else:
            if(arr[i] == condicion):
                acumulador = acumulador + 1
    return acumulador

def ordenarArreglo(arr):
        for i in range(0,8):
            for j in range(i+1,8):
                if(arr[i]!="" and arr[j]!=""):
                    if(arr[i]<arr[j]):
                        aux = arr[j]
                        arr[j] = arr[i]
                        arr[i] = aux 

def cambiarEstado(posicion, nuevoEstado):
    patenteData[1][posicion] = nuevoEstado
    
def tieneProductosAsociados(prodTentativo):
    for i in range(0,8):
        if(productosCamiones[i]==prodTentativo): return False
    return True
    

# FUNCIONES GENERALES

def realizarAccionABM(seleccion,nombreMenu):
    clear()
    if seleccion=='A': imprimirMenuEnConstruccion("Alta\n")
    elif seleccion=='B': imprimirMenuEnConstruccion("Baja\n")
    elif seleccion=='C': imprimirMenuEnConstruccion("Consulta\n")
    elif seleccion=='M': imprimirMenuEnConstruccion("Modificacion\n")
    elif seleccion=='V': print("Volviendo al menu de:",nombreMenu)
    else: print("Ingresar una seleccion valida\n")

def abrirMenuABM(nombreMenu):
    clear()
    prYellow("Menu ABM de: ")
    prPurple(nombreMenu)
    seleccionABM = '0'
    while(seleccionABM != 'V'):
        imprimirMenu(menuABM,5)
        seleccionABM = input("Seleccionar una accion ABM:\n")
        realizarAccionABM(seleccionABM,nombreMenu)


# FUNCIONES MENU PRINCIPAL

def seleccionarMenuPrincipal(seleccion):
    clear()
    if seleccion==1: abrirMenuAdministraciones()
    elif seleccion==2: abrirEntregaDeCupos()
    elif seleccion==3: abrirMenuRecepcion()
    elif seleccion==4: imprimirMenuEnConstruccion("Registrar Calidad\n")
    elif seleccion==5: abrirMenuPesoBruto()
    elif seleccion==6: imprimirMenuEnConstruccion("Registrar Descarga\n")
    elif seleccion==7: abrirMenuPesoTara()
    elif seleccion==8: imprimirReporte()
    else: print("Ingresar una seleccion valida\n")

# FUNCIONES MENU PRINCIPAL




# FUNCIONES ADMINISTRACION


# FUNCIONES ADMINISTRACION - ALTA

def imprimirProductosNoSeleccionados():
    prPurple("Los productos posibles a ingresar son:")
    for idxPool in range(0,5):
        encontrado = False
        for idxProductos in range(0,3):
            if(poolProductos[idxPool]==productos[idxProductos]):
                encontrado = True
            if(idxProductos==2 and encontrado == False):
                prYellow(poolProductos[idxPool])
    
def validarProductoIngresado(productoAIngresar):
    if(elementoEnArreglo(productoAIngresar,productos,3)):
        prCyan("El producto ya fue ingresado")
        return False
    if(not elementoEnArreglo(productoAIngresar,poolProductos,5)):
        prCyan("El producto no existe")
        return False
    return True
        
def darDeAltaProducto():
    clear()
    if(esArregloLleno(productos,3) == True):
        return print("El arreglo de productos está lleno")
    imprimirProductosNoSeleccionados()
    productoAIngresar = input("Seleccione uno de ellos:").upper()
    if(validarProductoIngresado(productoAIngresar)):
        ingresarPrimerLugarVacio(productoAIngresar,productos,3)
        print("INGRESADO!")        

# FUNCIONES ADMINISTRACION - BAJA

def darDeBajaProducto():
    clear()
    if(esArregloVacio(productos,3)):return print("no hay nada que dar de baja")
    imprimirElementosDeArreglo(productos,3)
    idxEliminar = int(input("Ingresar el indice del producto a eliminar: "))
    if(idxEliminar >= 3 or idxEliminar < 0): return prYellow("Ingresar un indice entre 0 y 2")
    if(productos[idxEliminar]==""): return prYellow("La casilla no contiene un producto")
    if(not tieneProductosAsociados(productos[idxEliminar])): return prYellow("El producto tiene camiones asociados")
    clear()
    productos[idxEliminar]=""
    return prCyan("Producto eliminado")

# FUNCIONES ADMINISTRACION - MODIFICACION

def modificarProducto():
    clear()
    if(esArregloVacio(productos,3)):return print("no hay nada que modificar")
    imprimirElementosDeArreglo(productos,3)
    idxModificar = int(input("Ingresar el indice del producto a modificar: "))
    if(idxModificar >= 3 or idxModificar < 0): return prYellow("Ingresar un indice entre 0 y 2")
    if(productos[idxModificar]==""): return prYellow("La casilla no contiene un producto")
    if(not tieneProductosAsociados(productos[idxModificar])): return prYellow("El producto tiene camiones asociados")
    clear()
    imprimirProductosNoSeleccionados()
    productoAIngresar = input("Seleccione uno de ellos:").upper()
    if(validarProductoIngresado(productoAIngresar)):
        productos[idxModificar] = productoAIngresar
        return prCyan("MODIFICADO!")        

def administracionProductoRouter(seleccion):
    clear()
    if seleccion=='A': darDeAltaProducto()
    elif seleccion=='B': darDeBajaProducto()
    elif seleccion=='C': imprimirElementosDeArreglo(productos,3)
    elif seleccion=='M': modificarProducto()
    elif seleccion=='V': print("Volviendo al menu de: ADMINISTRACION")
    else: print("Ingresar una seleccion valida\n")

def abrirAdministracionProductoABM():
    clear()
    prYellow("Menu ABM de: ")
    prCyan("ADMINISTRACION - PRODUCTO")
    seleccionABM = '0'
    while(seleccionABM != 'V'):
        imprimirMenu(menuABM,5)
        seleccionABM = input("Seleccionar una accion ABM:\n").upper()
        administracionProductoRouter(seleccionABM)

def seleccionarMenuAdministracion(seleccion):
    clear()
    if seleccion=='A': abrirMenuABM("Administracion\n")
    elif seleccion=='B': abrirAdministracionProductoABM()
    elif seleccion=='C': abrirMenuABM("Administracion\n")
    elif seleccion=='D': abrirMenuABM("Administracion\n")
    elif seleccion=='E': abrirMenuABM("Administracion\n")
    elif seleccion=='F': abrirMenuABM("Administracion\n")
    elif seleccion=='G': abrirMenuABM("Administracion\n")
    elif seleccion=='V': print("Volviendo al menu principal\n")
    else: print("Ingresar una seleccion valida\n")

def abrirMenuAdministraciones():
    seleccionAdministraciones = "0"
    while(seleccionAdministraciones!='V'):
        imprimirMenu(menuAdministraciones,8)
        seleccionAdministraciones = elegirElementoDeMenu().upper()
        seleccionarMenuAdministracion(seleccionAdministraciones)

# FUNCIONES ADMINISTRACION

# FUNCIONES ENTREGA DE CUPOS

def cargarPatenteYEstado(patente):
    idx = 0
    while(patenteData[0][idx]!= ""):
        idx = idx + 1
    patenteData[1][idx] = "P"
    patenteData[0][idx] = patente


def abrirEntregaDeCupos():
    if patenteData[0][7] != "" : 
        print("Se alcanzo la cantidad maxima de cupos diarios.")
    else :
        esValida = False
        while (not esValida or posEnArreglo != -1):
            patenteIngresada = input("Ingrese una patente (o 0 para volver al menu anterior): ")   
            posEnArreglo = buscarElementoEnArreglo(patenteIngresada, patenteData[0], 7)
            esValida = verificarPatente(patenteIngresada)
            if(patenteIngresada == '0'): return
            if(not esValida): print("La patente debe tener 6 o 7 caracteres")
            else : print("La patente ya fue registrada")
        cargarPatenteYEstado(patenteIngresada)
        print("Patente ingresada exitosamente")
        print(patenteData)

# FUNCIONES ENTREGA DE CUPOS


# FUNCIONES RECEPCION

def abrirMenuRecepcion():
    print("--- En el Menu De Recepcion ---\n")
    esValida = False
    estado = 'X'
    while (not esValida or posEnArreglo == -1 or estado != 'P'):
        patenteIngresada = input("Ingrese una patente (o 0 para volver al menu anterior): ")   
        posEnArreglo = buscarElementoEnArreglo(patenteIngresada, patenteData[0], 7)
        esValida = verificarPatente(patenteIngresada)
        if(patenteIngresada == '0'): return
        if(posEnArreglo != -1): 
            estado = patenteData[1][posEnArreglo]
        if(not esValida): print("La patente debe tener 6 o 7 caracteres")
        elif(posEnArreglo == -1): print("La patente no se encuentra registrada")
        elif(estado != 'P') : print("El estado del camion no es Pendiente")
    cambiarEstado(posEnArreglo, 'E')
    print("Camion ingresado exitosamente")
    print(patenteData)

# FUNCIONES RECEPCION


# FUNCIONES INGRESAR PESO BRUTO

def verificarPatente(patente):
    return len(patente)>=6 and len(patente)<=7

def abrirMenuPesoBruto():
    clear()
    patenteTentativa = input("Ingresar una patente: ")
    if(not verificarPatente(patenteTentativa)): return prYellow("La patente tiene que estar entre 6 y 7 caracteres")
    indicePatente = buscarElementoEnArreglo(patenteTentativa,patenteData[0],3)
    if(indicePatente==-1): return prYellow("La patente ingresada no existe")
    if(patenteData[1][indicePatente]!="E"): return prYellow("El estado de la patente seleccionada no es En Proceso")
    if(pesosArr[0][indicePatente]!=0): return prYellow("El camion ya tiene registrado un peso bruto")
    pesosArr[0][indicePatente] = int(input("Ingresar el peso bruto del camion: "))
    prCyan("Guardado!")

# FUNCIONES INGRESAR PESO BRUTO

# FUNCIONES INGRESAR PESO TARA

def abrirMenuPesoTara():
    clear()
    patenteTentativa = input("Ingresar una patente: ")
    if(not verificarPatente(patenteTentativa)): return prYellow("La patente tiene que estar entre 6 y 7 caracteres")
    indicePatente = buscarElementoEnArreglo(patenteTentativa,patenteData[0],3)
    if(indicePatente==-1): return prYellow("La patente ingresada no existe")
    if(patenteData[1][indicePatente]!="E"): return prYellow("El estado de la patente seleccionada no es En Proceso")
    if(pesosArr[0][indicePatente]==0): return prYellow("El camion no tiene registrado un peso bruto")
    if(pesosArr[1][indicePatente]!=0): return prYellow("El camion ya tiene registrado un peso tara")
    taraTentativa = int(input("Ingresar el peso tara del camion: "))
    if(taraTentativa>=pesosArr[0][indicePatente]): return prYellow("La tara no puede ser mayor o igual al peso bruto")
    pesosArr[0][indicePatente] = taraTentativa
    patenteData[1][indicePatente] = "C"
    prCyan("Guardada y cambiado estado del camion a completado!")

# FUNCIONES INGRESAR PESO TARA


# FUNCIONES REPORTE


def copiarSiCamionCompleto(arrACopiar,esPesoNeto=False):
    arr = ["","","","","","","",""]
    for i in range(0,8):
        if(patenteData[1][i]=="C"):
            if(esPesoNeto==False):
                ingresarPrimerLugarVacio(arrACopiar[i],arr,8)
            else:
                ingresarPrimerLugarVacio(pesosArr[0][i]-pesosArr[1][i],arr,8)
    return arr
    
def imprimirReporte():
    clear()
    prCyan("------------")       
    print("Se otorgaron ",acumularSiCondicion(patenteData[1],"",True)," cupos")
    print("Se recibieron ",acumularSiCondicion(patenteData[1],"E") + acumularSiCondicion(patenteData[1],"C")," camiones")
    for prodIdx in range(0,3):
        pesoNetoTot = 0
        cantidad = 0
        arrMayorMenor = [0,999999]
        arrPatenteMayorMenor = ["",""]
        if(productos[prodIdx]!=""):
            for camIdx in range(0,8):
               if(patenteData[1][camIdx]=="C" and productosCamiones[camIdx]==productos[prodIdx]):
                   pesoNetoCamion = pesosArr[0][camIdx] - pesosArr[1][camIdx]
                   patenteCamion = patenteData[0][camIdx]
                   cantidad = cantidad + 1
                   pesoNetoTot = pesoNetoTot + pesoNetoCamion
                   if(pesoNetoCamion>arrMayorMenor[0]): 
                       arrMayorMenor[0] = pesoNetoCamion
                       arrPatenteMayorMenor[0] = patenteCamion
                   if(pesoNetoCamion<arrMayorMenor[1]): 
                       arrMayorMenor[1] = pesoNetoCamion
                       arrPatenteMayorMenor[1] = patenteCamion
            prCyan("------------")       
            print("Hay ",cantidad," camiones de ",productos[prodIdx])
            print("El peso neto de ",productos[prodIdx],"es ", pesoNetoTot ,"kg")
            print("El peso neto promedio de camion de ",productos[prodIdx],"es ", pesoNetoTot/cantidad ,"kg")
            print("El camion que mas ",productos[prodIdx],"descargo es ", arrPatenteMayorMenor[0],"con ",arrMayorMenor[0] ,"kg")
            print("El camion que menos ",productos[prodIdx],"descargo es ", arrPatenteMayorMenor[1],"con ",arrMayorMenor[1] ,"kg")
            prCyan("------------")  

    prCyan("------------")       
    patenteCopia = copiarSiCamionCompleto(patenteData[0])
    productoCopia = copiarSiCamionCompleto(productosCamiones)
    pesosNetos = copiarSiCamionCompleto([],True)
    ordenarArreglo(pesosNetos)
    ordenarArreglo(productoCopia)
    ordenarArreglo(patenteCopia)
    for i in range(0,8):
        if(patenteCopia[i]!=""):
            print(patenteCopia[i] ,"-", productoCopia[i] , "-", pesosNetos[i])

# FUNCIONES REPORTE
while(seleccionPrincipal!=0):
    imprimirMenu(menuPrincipal,9)
    seleccionPrincipal = elegirElementoDeMenu(True)
    seleccionarMenuPrincipal(seleccionPrincipal)

prCyan("Finalizacion del programa\n")