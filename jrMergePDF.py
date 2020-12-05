from PyPDF2 import PdfFileMerger            # pip install PyPDF2
import os        

#Estructura de carpetas del aplicativo y datos (por defecto)
pdfDir      = os.path.join(os.getcwd(),'IN')            #Carpeta dónde dejaremos los pdf para agrupar
OutDir      = os.path.join(os.getcwd(),'OUT')           #Carpeta dónde nos devolverá el pdf generado a partir de la agrupación de pdf's de \IN
GroupName   = "PDF_Agrupado"                            #Nombre del fichero pdf resultado de agrupar los pdf's de \IN

#definimos la función merge
def jrPDFmerge(pdfDir, OutDir, NameFile):

    merge = PdfFileMerger()

    for items in os.listdir(pdfDir):
        if items.upper().endswith('.PDF') :
            merge.append(os.path.join(pdfDir,items))

    merge.write(os.path.join(OutDir,NameFile+'.pdf'))
    merge.close()

    return

#Lanzamos la función para ejecutar el merge de los ficheros
jrPDFmerge(pdfDir, OutDir,GroupName)
