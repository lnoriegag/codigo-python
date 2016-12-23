"""
Este programa realiza el factorial de un numero
"""

# Funcion recursiva para obtener el factorial de un nmero
def factorial(x):
    if x == 0:
        return 1
    else:
        return x* factorial(x - 1)

if __name__=='__main__':

    try:
        num = int(raw_input("Ingresa un numero:"))
        print 'El factorial de {0} es: {1}'.format(num, factorial(num))    
    except ValueError:
        print 'Error.Se debe ingresar un numero'
