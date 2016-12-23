"""
Este programa recibe un archivo '.txt' y muestra una tabla con el 
caracter y el numero de incidencias en el archivo.
"""

def mostrar_entradas(caracteres, titulo = 'Letras'):
    
    '''Muestra con un formato de tabla, todas las entradas del usuario'''

    # Ordena los elementos del diccionario para presentarlos en orden
    elementos = [(v, k) for k, v in caracteres.items()]
    elementos.sort()
    elementos.reverse() # El caracter con mayor ocurrencia al principio
    caracteres = [(k, v) for v, k in elementos]

    # Formato de presentacion
    ancho = 25
    print'~'*ancho
    print titulo.center(ancho,'~')
    print'~'*ancho

    print '~ {:<10s} ~ {:>8s} ~'.format('Letra','Num')

    # Recorremos todos los elementos del diccionario
    for clave, valor in caracteres:
        print'~ {clave:10s} ~'.format(clave = clave),'{:>8} ~'.format(valor)

    print('~'*ancho)

if __name__=='__main__':
    # Abrir el archivo para lectura
    '''Cambiar 'texto.txt' por el nombre del archivo a analizar'''
    nombrearchivo = 'texto.1.txt'
    with open(nombrearchivo) as archivo:
        caracteres = {}
        for linea in archivo:
            palabras = linea.split() # separa la linea en palabras, por el espacio en blanco
            for palabra in palabras:
                letras = list(palabra)
                for letra in letras:
                    # Si ya se encuentra la letra en el diccionario caracteres
                    if caracteres.has_key(letra):
                        val = caracteres[letra]
                        caracteres[letra] = val + 1
                    else:
                        caracteres[letra] = 1
    # Cerrar el archivo para finalizar
    archivo.close()
    # Muestra los resultados encontrados
    mostrar_entradas(caracteres)