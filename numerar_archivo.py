"""
Este programa lee un archivo .txt y numera las lineas
"""

def mostrar_archivo(nombrearchivo):

    #Abrir archivo para lectura
    with open(nombrearchivo) as archivo:
        num = 0
        for linea in archivo:
            num += 1
            print('{:03d}:{:<80s}'.format(num, linea.rstrip() ) )

    #Cerrar el archivo a finalizar
    archivo.close()


if __name__=='__main__':
    nombrearchivo = 'nombre_de_archivo.txt'
    mostrar_archivo(nombrearchivo)