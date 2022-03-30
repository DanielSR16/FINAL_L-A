from audioop import add
import csv
from queue import PriorityQueue
import string



 
# def filt(word):
#     return unicodedata.normalize('NFKD', word).encode('ascii', errors='ignore').decode('ascii')
mayusculas = list(string.ascii_uppercase)
mayusculas.append('Ñ')
minusculas = list(string.ascii_lowercase)
minusculas.append('ñ')
fila = 0
columna = 0

listLetra = minusculas + mayusculas
listNumeros = ['1','2','3','4','5','6','7','8','9','0']
with open('datos.csv', newline='') as File:  
    reader = csv.reader(File)
    auxLit = []
    ListaTotalDatos = []
    for row in reader:
        for datos in row:
                auxLit.append(datos)
        ListaTotalDatos.append(auxLit)
        auxLit = []  
 
    ListaTotalDatos[0][19] = 'enteroSuperPequeño'
    ListaTotalDatos[0][20] = 'enteroPequeño'
    ListaTotalDatos[0][29] = 'año'
    ListaTotalDatos[0][30] = 'textoPequeño'
    ListaTotalDatos[0][6] = 'a...z|A...Z'


    ListaTotalDatos[12][19] = 'enteroSuperPequeño'
    ListaTotalDatos[12][20] = 'enteroPequeño'
    ListaTotalDatos[12][29] = 'año PA CANTIDAD PC'
    ListaTotalDatos[12][30] =  'textoPequeño'
    ListaTotalDatos[7][6] = 'a...z|A...Z'

    # print(ListaTotalDatos[13][7])
    lista_no_terminales = []
    for i in ListaTotalDatos:
        lista_no_terminales.append(i[0])
    # print(lista_no_terminales)
    # print(ListaTotalDatos[0])

    # for i in ListaTotalDatos[] 

def metodos_sintantico(valoresBuscar):
    print(valoresBuscar)
    resultado = 'Exitoso'
    apuntador = 0
    entrada = valoresBuscar
    entrada.append('$')
    pila = ['ENTRADAS','$']
    primeroPila = pila[0]
    while(primeroPila != '$'):

        primeroPila = pila[0]
        # if apuntador < len(entrada):
        simboloApuntado = entrada[apuntador]
        # if(apuntador == len(entrada)):
        #     pila.pop(0)

        encuentra_terminales = primeroPila in ListaTotalDatos[0]

        
        print('__________________________________________')
        print('PRIMERO EN LA PILA: ',primeroPila)
        print('APUNTADOR: ',simboloApuntado)
        # print(fila)
        # print(columna)
        print(pila)

        if primeroPila == 'vacio':
                # print('entre a vacio')
                pila.pop(0)
         
        elif encuentra_terminales == True or primeroPila == '$':
            print('entre a terminales')
            if primeroPila == 'a...z|A...Z':
                in_listaLetra =  simboloApuntado in listLetra
                if in_listaLetra == True:
                    pila.pop(0)
                    apuntador = apuntador + 1

            elif primeroPila == '0...9':
                in_listaNumeros = simboloApuntado in listNumeros
                if in_listaNumeros == True:
                    pila.pop(0)
                    apuntador = apuntador + 1
         
            elif primeroPila == simboloApuntado:
                pila.pop(0)
                apuntador = apuntador + 1
                
            else:
                resultado = 'Erroneo'
          
                break
        elif encuentra_terminales == False:
            print('entre a NO terminales')
            exsiste_no_Terminales = primeroPila in  lista_no_terminales
          
            if exsiste_no_Terminales == True:
                print(primeroPila)
                print(simboloApuntado)
                fila = buscarFila(primeroPila)
                columna = buscarColumna(simboloApuntado)
                print('FILA: ',fila)
                print('COLUMNA: ',columna)
                datoAddPila = ListaTotalDatos[fila][columna]
                
                # print(datoAddPila)
                listaAddPila = datoAddPila.split()
                # print(listaAddPila)
                pila.pop(0)
                listaAddPila.extend(pila)
                pila = listaAddPila
                
            else:
                resultado = 'Erroneo'
                break
                # regla = 
    return resultado


        
def buscarFila(valor_pila):
    # posicionFila = 0
    for i in range(1,len(ListaTotalDatos)):
        # print(i)
        if ListaTotalDatos[i][0] == valor_pila:
            posicionFila = i
    return posicionFila   

def buscarColumna(simboloApuntado:str):
    simboloBuscar = ''
    # print('soy el simbolo',simboloApuntado)
    letra = False
    if(len(simboloApuntado) == 1 and simboloApuntado.isalpha() == True):
 
        letra = True
    numero = simboloApuntado.isdigit()

    if letra == True:
  
        simboloBuscar = 'a...z|A...Z'
    elif numero == True:
        simboloBuscar = '0...9'
     
    else:
         simboloBuscar = simboloApuntado

    for x in range(1,len(ListaTotalDatos[0])):
        # print(x)
        # print(ListaTotalDatos[0][x] )
        # print(ListaTotalDatos[0][x])
        # print('siembolo a buscar xd: ',simboloBuscar)
        if ListaTotalDatos[0][x] == simboloBuscar:
            
            # print('simbolo en columa: ',ListaTotalDatos[0][x])
            # print('simbolo a buscar: ',simboloBuscar)
            posicionColumna = x
            
    return posicionColumna
        
         


