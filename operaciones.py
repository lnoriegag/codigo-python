"""
Este programa recibe 2 numeros enteros y realiza una serie de operaciones con ellos
desplegando la operacion y resultado en pantalla.
"""

# Define la funcion realizar_operacion para simplificar tarea de impresion
def realizar_operacion(a,b,operador=''):
    """Realiza una operacion sobre dos numeros, mostrando la operacion realizada"""
    var = eval('a'+operador+'b')
    print '{0} {3} {1} : Dec = {2}'.format(num1,num2,var,operador)+', Bin = '+bin(var)+', Hex = ''%x'%var+', Oct = ''%o'%var+'\n'

num1 = raw_input('Ingresa el primer numero: ')
num2 = raw_input('Ingresa el segundo numero: ')

if str(num1).isdigit() and str(num2).isdigit():
    print '\n'
    # Operadores de comparacion
    print '{0}Operadores de comparacion{1}'.format('*'*15,'*'*15)
    print '{0} es menor que {1} = {2}'.format(num1,num2,num1<num2)
    print '{0} es menor o igual que {1} = {2}'.format(num1,num2,num1<=num2)
    print '{0} es mayor que {1} = {2}'.format(num1,num2,num1>num2)
    print '{0} es mayor o igual que {1} = {2}'.format(num1,num2,num1>=num2)
    print '{0} es igual {1} = {2}'.format(num1,num2,num1==num2)
    print '{0} es diferente {1} = {2}'.format(num1,num2,num1!=num2)
    print '{0} es {1} = {2}'.format(num1,num2,num1 is num2)
    print '{0} no es {1} = {2}'.format(num1,num2,num1 is not num2)+'\n'

    # Operadores de expresion
    print '{0}Operadores de expresion{1}'.format('*'*15,'*'*15)+'\n'
    print 'Dec = "Decimal", Bin = "Binario", Hex = "Hexadecimal", Oct = "Octal"'+'\n'


    # Suma
    realizar_operacion(num1,num2,'+')
    # Resta
    realizar_operacion(num1,num2,'-')
    # Multiplicacion
    realizar_operacion(num1,num2,'*')
    # Division
    realizar_operacion(num1,num2,'/')
    # Residuo
    realizar_operacion(num1,num2,'%')
    # Exponenciacion
    realizar_operacion(num1,num2,'**')
    # OR bit a bit
    realizar_operacion(num1,num2,'|')
    # XOR bit a bit
    realizar_operacion(num1,num2,'^')
    # AND bit a bit
    realizar_operacion(num1,num2,'&')

    # Corrimiento de bits (Izq)
    var = num1 << num2
    print '{0} << {1} : Dec = {2}'.format(num1,num2,var)+', Bin = '+bin(var)+', Hex = ''%x'%var+', Oct = ''%o'%var+'\n'

    # Corrimiento de bits (Der)
    var = num1 >> num2
    print '{0} >> {1} : Dec = {2}'.format(num1,num2,var)+', Bin = '+bin(var)+', Hex = ''%x'%var+', Oct = ''%o'%var+'\n'

else:
    print '\n {0} Verifica entrada, debes ingresar dos numeros enteros {1}'.format('*'*10,'*'*10)