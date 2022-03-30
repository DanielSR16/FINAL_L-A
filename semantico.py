from email.mime import base
import os
from pickle import TRUE
import re
from iteration_utilities import duplicates


transcripcion = {'entero':'int','cadena':'CHAR','dobleFlotante':'DOUBLE','cadenaDefinida':'VARCHAR',

'enteroSuperPequeño':'SMALLINT','enteroPequeño':'TINYINT','enteroMediano':'MEDIUMINT','bigInt':'BIGINT',

'enteroDecimal':'FLOAT','fecha':'DATE','fechaHora':'DATETIME','hora':'TIME','año':'YEAR','textoPequeño':'TINYTEXT',

'texto':'TEXT','textoMediano':'MEDIUMTEXT','textoLargo':'LONGTEXT','FLOAT':'FLOAT','decimalDoble':'DOBLE','incrementarse':'AUTO_INCREMENT','noVacio':'NOT NULL','decimal':'DECIMAL' }

datoAutoIncrement = ['int','SMALLINT','TINYINT','MEDIUMINT','BIGINT']

def semanticoPrincipal(lista_datos):
    resultado = 'Exitoso'
    baseDatos = ''
    tabla = ''
    Aux_campos = ''
    llave = ''
    meterDatos = False
    auxPalabra = ''
    print(lista_datos)
    for i in range(0,4):
        for valor in lista_datos[i]:
            if meterDatos == True:
                auxPalabra =   auxPalabra + valor
            if valor == ':':
                meterDatos = True
        if i == 0:
            baseDatos = auxPalabra
        elif i == 1:
            tabla = auxPalabra
        elif i == 2:
            Aux_campos =  auxPalabra
        elif i == 3:
            llave = auxPalabra
        
        meterDatos = False
        auxPalabra = ''
    campos = Aux_campos[:-1] + ','

    listaGeneralCampos = []
    palabraAux_campo = ''


    
    for posicion_campo in range(0,len(campos)):
        # print(campos[posicion_campo])
        if(campos[posicion_campo] != ','):
            palabraAux_campo = palabraAux_campo + campos[posicion_campo]
        elif(campos[posicion_campo] == ','):
       
            data = palabraAux_campo.split('-')
            listaGeneralCampos.append(data)
            palabraAux_campo = ''
       
    
        
    # for campo in campos:
    llavesTranscripcion = list(transcripcion.keys())    

    for fila in listaGeneralCampos:
        for valor in range(0,len(fila)):
            if('(' in fila[valor]):
              
                aux_valor_string = ''
                aux_valor_parentesis = '('
                tamañoParentesisEncontrado = 0
                vuelta = True
                parentesis = False
                contador = 0
                for contador in range(0,len(fila[valor])):
                    if(fila[valor][contador] != '(' and parentesis == False):
                        aux_valor_string = aux_valor_string + fila[valor][contador]
                        contador += 1
                    elif fila[valor][contador] == '(':
                        vuelta = False
                        parentesis  = True
                    elif parentesis == True:
                        aux_valor_parentesis = aux_valor_parentesis + fila[valor][contador]
                        contador += 1 
                       
            
                fila[valor] = transcripcion[aux_valor_string] + aux_valor_parentesis
                
            seEncuentra = fila[valor] in llavesTranscripcion
            if seEncuentra == True:
                fila[valor] = transcripcion[fila[valor]]
     
    print(listaGeneralCampos)

    lista_nombres_campos = []
    lista_tipo_dato = []
    lista_contienen_autoIncrement = []
    for posicion_nombre in range(0,len(listaGeneralCampos)):
        contiene_autoIncrement = 'AUTO_INCREMENT' in listaGeneralCampos[posicion_nombre]
        
        if contiene_autoIncrement == True:
            lista_contienen_autoIncrement.append(posicion_nombre)

         
        lista_nombres_campos.append(listaGeneralCampos[posicion_nombre][0])
        lista_tipo_dato.append(listaGeneralCampos[posicion_nombre][1])
 
        print(lista_nombres_campos)
    resultado_duplicados = list(duplicates(lista_nombres_campos))
    if len(resultado_duplicados) > 0:
        resultado = 'Nombres de campos duplicados: '+ str(resultado_duplicados)
    
    for datos_increment in lista_contienen_autoIncrement:
        esIncrement = lista_tipo_dato[datos_increment] in  datoAutoIncrement
        if(esIncrement == False):
            resultado = 'El tipo de dato: '+lista_tipo_dato[datos_increment] +' no puede contener AUTO_INCREMENT'

    vuelta = True
    contador = 0
    resulta_llave = False
    
    while (vuelta == True):
        estaEnllavePrimaria = llave in lista_nombres_campos
        if estaEnllavePrimaria == True:
            vuelta = False
        elif contador == len(lista_nombres_campos)-1:
                resultado = 'La llave primaria: '+ llave + ' ,no se encuentra dentro de la lista de campos'
                vuelta = False
        contador = contador + 1
    
        
    if(resultado == 'Exitoso'):
        camposFinalesString = ''
        for camposFinalesLista in listaGeneralCampos:
            for valoresFinales in range(0,len(camposFinalesLista)):
                camposFinalesString = camposFinalesString + camposFinalesLista[valoresFinales] + ' '
                if(len(camposFinalesLista)) == valoresFinales+1:
                    camposFinalesString  = camposFinalesString + ','+''
    

            
        texto_aux = 'CREATE DATABASE '+ baseDatos + ';\n'+'use '+baseDatos+';\n' + 'CREATE TABLE '+tabla+'('+camposFinalesString+'PRIMARY KEY ('+llave+')\n)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;'
        print(texto_aux)
        texto = texto_aux.replace('  ',' ')
        
        file = open("D:/UPCHIAPAS/Compiladores e Interpretes/Corte 3/Tareas/programa_sintactico/archivo/scrip.sql", "w")
        file.write(texto)
        file.close()
    return resultado
    
# semanticoPrincipal(['BaseDeDatos:animales', 'NombreTabla:felinos', 'ListaCampo:id-int-noVacio-incrementarse,mes-fecha-noVacio-,doblexd-dobleFlotante-noVacio-,a-enteroSuperPequeño---', 'LlavePrimaria:id'])



