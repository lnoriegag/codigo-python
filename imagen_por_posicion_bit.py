"""
Este programa lee una imagen a color, convierte sus pixeles en valores de un rango entre 0 y 255
    imagen_1 : bit 1
    imagen_2 : bit 2
    imagen_3 : bit 3
    imagen_4 : bit 4
    imagen_5 : bit 5
    imagen_6 : bit 6
    imagen_7 : bit 7
    imagen_8 : bit 8
y posteriormente crea imagenes, las cuales representan el bit del valor original de la imagen, de tal forma que:
"""

import warnings
from skimage import util
from skimage import io
from skimage.color import rgb2gray
import numpy as np

def regresa_bit(numero, posicion):
    if ((posicion>0 and posicion <=8)):
        if ((numero>=0 and numero <=255)):
            binario = [0,0,0,0,0,0,0,0]
            num_bin= bin(numero)
            num_bin = num_bin[2:len(num_bin)]
            for i in range(1,len(num_bin)+1):
                binario[len(binario)-i] = num_bin[len(num_bin)-i] 
            return binario[len(binario)-posicion]
        else:
            print 'Error. El numero debe ser entre un rango de 0 a 255',numero
    else:
        print 'Error. La posicion debe ser entre un rango de 1 a 8', posicion

if __name__ == '__main__':
    # Leer imagen
    path = 'C:\\'
    image= path + 'nombre_de_la_imagen.jpg'
    imagen = io.imread(image)


    if len(imagen.shape) == 3:
        # Obtiene tamanio de imagen
        f = imagen.shape[0]
        c = imagen.shape[1]

        # Se crean las matrices para las imagenes
        for i in range(1,9):
            nombre = "imagen_"
            nombre = nombre+str(i)
            globals()[nombre]= np.zeros((f, c)) 

        # Convierte la imagen en valores entre 0 a 1
        imagenGris = rgb2gray(imagen)

        # Convierte imagenGris en rango de 0 a 255
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            img = util.img_as_ubyte(imagenGris)
        
        # Extrae los bits de cada uno de los pixeles de la imagen
        for fila in range(0, f):
            for columna in range(0, c):
                for i in range(1,9):
                    nombre = "imagen_"
                    nombre = nombre+str(i)
                    tem =  globals()[nombre]
                    tem[fila,columna] = regresa_bit(img[fila,columna],i)
                    globals()[nombre]= tem

        # Almacena las imagenes 
        for i in range(1,9):
            nombre = "imagen_"
            nombre = nombre+str(i)
            io.imsave(nombre+".jpg",globals()[nombre])
    else:
        print 'La imagen ingresada, debe ser a color'
