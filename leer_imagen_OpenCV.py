"""
Este programa lee una imagen utilizando la libreria de codigo abierto OpenCV y 
muestra la informacion de la imagen.
"""

import cv2

path = 'C:\\'
image= path + 'nombre_de_la_imagen.jpg'
img = cv2.imread(image,1)
print 'Tipo de la imagen por Python: ',type(img)
print 'Tipo de la imagen por OpenCV:',img.dtype
print 'Tamanio de la Imagen:',img.shape
print 'Tamanio X:',img.shape[0]
print 'Tamanio Y:',img.shape[1]
print 'Numero de Canales:',img.shape[2]
print 'Multiplicacion todos los pixeles (Ancho * Alto * Numero de Canales):',img.size
print 'Valor Minimo:',img.min()
print 'Valor Maximo:',img.max()
print 'Valor Promedio de toda la imagen:',img.mean()