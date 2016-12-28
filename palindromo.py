import re
from unicodedata import normalize
"""
    Este programa recibe una cadena y verifica si es un palindromo o no
    Acepta palindromos con acento siempre y cuando la palabra inversa tenga acento. No acepta numeros
"""

def entrada_valida(cadena):
    '''Valida si solo se ingresaron palabras sin numeros'''
    cadena = re.findall('(\w+)',cadena)
    for palabra in cadena:
        if not palabra.isalpha():
            raise ValueError
    return ' '.join(str(x) for x in cadena)


def valida_palindromo(cadena):
    '''Valida si la cadena ingresada es un palindromo'''
    # Convierte la cadena en una lista por palabra
    cad_list = list(cadena)

    # Voltea la lista que contiene las letras de la cadena
    cad_list_rev= cad_list[::-1]
    
    # Lo convierte en str para poder compararlo
    cadena_rev = ''.join(str(e) for e in cad_list_rev)

    if cadena == cadena_rev:
        return True
    return False


if __name__=="__main__":
    cadena = raw_input('Ingresa una cadena: ')
    cad_or = cadena


    try:
        cadena = entrada_valida(cadena)
        # Convierte todo a minusculas y elimina el espacio
        cadena =cadena.replace(" ","").lower() 
        if valida_palindromo(cadena):
            print 'La cadena ingresada: \n','{0} "{1}" {2}'.format('*'*10,cad_or,'*'*10),' ES UN PALINDROMO '
        else:
            print 'La cadena ingresada: \n','{0} "{1}" {2}'.format('*'*10,cad_or,'*'*10),' NO UN PALINDROMO '
    except ValueError:
        print 'Verifique la entrada'
        
