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

def elegirElementoDeMenu(esEntero = False):
    if(esEntero == True):
        resultado = int(input("--- Seleccionar un submenu ---\n"))
    if(esEntero == False):
        resultado = input("--- Seleccionar un submenu ---\n")
    return resultado
    
def imprimirMenuEnConstruccion(menu):
    print("El menu:",menu,"esta en construccion\n")
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
    print("Estamos en el menu de: ",nombreMenu)
    seleccionABM = '0'
    while(seleccionABM != 'V'):
        imprimirMenu(menuABM,5)
        seleccionABM = input("Seleccionar una accion ABM:\n")
        realizarAccionABM(seleccionABM,nombreMenu)


# FUNCIONES MENU PRINCIPAL

def seleccionarMenuPrincipal(seleccion):
    clear()
    if seleccion==1: abrirMenuAdministraciones()
    elif seleccion==2: imprimirMenuEnConstruccion("Entrega de cupos\n")
    elif seleccion==3: abrirMenuRecepcion()
    elif seleccion==4: imprimirMenuEnConstruccion("Registrar Calidad\n")
    elif seleccion==5: imprimirMenuEnConstruccion("Registrar Peso Bruto\n")
    elif seleccion==6: imprimirMenuEnConstruccion("Registrar Descarga\n")
    elif seleccion==7: imprimirMenuEnConstruccion("Registrar Tara\n")
    elif seleccion==8: imprimirReporte()
    else: print("Ingresar una seleccion valida\n")

# FUNCIONES MENU PRINCIPAL


# FUNCIONES ADMINISTRACION

def seleccionarMenuAdministracion(seleccion):
    clear()
    if seleccion=='A': abrirMenuABM("Titulares\n")
    elif seleccion=='B': abrirMenuABM("NOMBRE\n")
    elif seleccion=='C': abrirMenuABM("NOMBRE\n")
    elif seleccion=='D': abrirMenuABM("NOMBRE\n")
    elif seleccion=='E': abrirMenuABM("NOMBRE\n")
    elif seleccion=='F': abrirMenuABM("NOMBRE\n")
    elif seleccion=='G': abrirMenuABM("NOMBRE\n")
    elif seleccion=='V': print("Volviendo al menu principal\n")
    else: print("Ingresar una seleccion valida\n")

def abrirMenuAdministraciones():
    seleccionAdministraciones = "0"
    while(seleccionAdministraciones!='V'):
        imprimirMenu(menuAdministraciones,8)
        seleccionAdministraciones = elegirElementoDeMenu()
        seleccionarMenuAdministracion(seleccionAdministraciones)

# FUNCIONES ADMINISTRACION

# FUNCIONES RECEPCION
def cargaDatosYMostrarPesoNetoCamion():
    patente = input("Cargar la patente del camion\n")
    producto = input("Ingresar el producto (soja|maiz)\n")
    validarIngresoProducto(producto)
    pesoBruto = int(input("Cargar el peso bruto del camion\n"))
    tara = int(input("Cargar la tara del camion\n"))
    pesoNeto = obtenerPesoNeto(patente,pesoBruto,tara)
    actualzarValoresReportes(patente,producto,pesoNeto)

def actualzarValoresReportes(patente,producto,pesoNeto):
    global camionesSoja, pNetoMaiz, pNetoSoja, patenteMayorSoja, patenteMenorMaiz, camionesMaiz, camionesSoja, mayorCantSoja, menorCantMaiz
    if(producto=="soja"):
        camionesSoja = camionesSoja+1
        pNetoSoja = pNetoSoja+pesoNeto
        if(pesoNeto>mayorCantSoja): 
            mayorCantSoja = pesoNeto
            patenteMayorSoja = patente
    if(producto=="maiz"):
        camionesMaiz = camionesMaiz + 1
        pNetoMaiz = pNetoMaiz + pesoNeto
        if(pesoNeto<menorCantMaiz): 
            menorCantMaiz = pesoNeto
            patenteMenorMaiz = patente

def validarIngresoProducto(producto):
    while(producto!="soja" and producto!='maiz'):
        producto = input("Por favor ingresar un producto valido (soja|maiz)\n")

def obtenerPesoNeto(patente,pesoBruto,tara):
    resultado = pesoBruto-tara
    print("El peso neto de", patente ,"es:", pesoBruto-tara)
    return resultado

def abrirMenuRecepcion():
    seguirCargando = 'Y'
    print("--- En el Menu De Recepcion ---\n")
    while(seguirCargando == 'Y'):
        cargaDatosYMostrarPesoNetoCamion()
        seguirCargando = input("Si se desea seguir cargando camiones escribir Y, de lo contrario escribir N: \n")


# FUNCIONES RECEPCION

# FUNCIONES REPORTE

def imprimirReporte():
    clear()
    global camionesMaiz , camionesSoja, pNetoSoja, pNetoMaiz
    print("La cantidad total de camiones es:\n",camionesSoja+camionesMaiz)
    print("La cantidad total de camiones de soja es:\n",camionesSoja)
    print("La cantidad total de camiones de maiz:\n",camionesMaiz)
    print("El peso neto de soja es:\n",pNetoSoja)
    print("El peso neto de maiz es:\n",pNetoMaiz)
    if camionesSoja != 0: 
        print("El promedio del peso neto de soja por camion es:\n",pNetoSoja/camionesSoja)
    if camionesMaiz != 0: 
        print("El promedio del peso neto de maiz por camion es:\n",pNetoMaiz/camionesMaiz)
    print("El camion que mas soja descargo es:\n",patenteMayorSoja)
    print("El camion que menos maiz descargo es:\n",patenteMenorMaiz)

# FUNCIONES REPORTE

while(seleccionPrincipal!=0):
    imprimirMenu(menuPrincipal,9)
    seleccionPrincipal = elegirElementoDeMenu(True)
    seleccionarMenuPrincipal(seleccionPrincipal)

prCyan("Finalizacion del programa\n")