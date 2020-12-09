from PyPDF2 import PdfFileMerger            # pip install PyPDF2
import os        
import sys      
import jrHelp                               # Importamos el fichero de ayuda                     
import re

#Estructura de carpetas del aplicativo y datos (por defecto)
pdfDir      = os.path.join(os.getcwd(),'IN')            #Carpeta dónde dejaremos los pdf para agrupar
OutDir      = os.path.join(os.getcwd(),'OUT')           #Carpeta dónde nos devolverá el pdf generado a partir de la agrupación de pdf's de \IN
GroupName   = "PDF_Agrupado"                            #Nombre del fichero pdf resultado de agrupar los pdf's de \IN
RegEx_Name = re.compile(r'[a-zA-Z]{1}[0-9a-zA-Z]{1,}') #Cadena Alfanumérica de mín 2 carácteres (el primero debe ser siempre una letra)
xlError     = False

#Obtenemos los parametros que nos pasan y le restamos 1 (ya que el primero implicitamente siempre es el nombre del programa en .py)
xnNumArgs = len(sys.argv)-1
#print("\nCuantos parametros has enviado: {}".format(xnNumArgs))

#definimos la función merge
def jrPDFmerge(pdfDir, OutDir, NameFile):

    merge = PdfFileMerger()

    for items in os.listdir(pdfDir):
        if items.upper().endswith('.PDF') :
            merge.append(os.path.join(pdfDir,items))

    merge.write(os.path.join(OutDir,NameFile+'.pdf'))
    merge.close()

    return

if xnNumArgs > 0 and (sys.argv[1] == '?' or sys.argv[1] == '-?'):
    jrHelp.jrPrintHelp()
else:
    if xnNumArgs > 0 and sys.argv[1] != '':
        if RegEx_Name.match(sys.argv[1]):
            GroupName = sys.argv[1]
        else:
            print("El Nombre del fichero a crear, no es correcto.\nDebe tener mín. 2 carácteres y empezar por una letra.")
            xlError     = True 
    
    if xnNumArgs > 1 and sys.argv[2] != '':
        if not os.path.isdir(sys.argv[2]):
            print("El Directorio de origen {0}, no existe".format(sys.argv[2]))
            xlError     = True 
        else:
            pdfDir = sys.argv[2]

    if xnNumArgs > 2 and sys.argv[3] != '':
        if not os.path.isdir(sys.argv[3]):
            print("El Directorio de destino {0}, no existe".format(sys.argv[3]))
            xlError     = True 
        else:
            OutDir = sys.argv[3]

# Si no hemos detectado ningun error en los parametros, lanzamos el proceso
if not xlError :
    #Lanzamos la función para ejecutar el merge de los ficheros
    jrPDFmerge(pdfDir, OutDir,GroupName)
