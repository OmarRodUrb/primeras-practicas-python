print ('''
vienvenido a tu calculadora personal
 podemos poyarte con las siguientes operacines

 SUMA (1)
 RESTA (2)
 MULTIPLICACION (3)
 DIVISION (4)

 PARA EFECTUAR TU OPERACION COLOCA EL NUMERO
 DE LA OPERACION DESEADA ''')
operacion = int(input ())
if operacion >= 5:
    print ("tu seleccion no es valida")
    exit ()
if operacion == 1 :
    print ("perfecto elejiste una suma, introduce el primer numero")
    n1 = int (input ())
    print ("introduce el segundo numero")
    n2 = int (input())
    resultado = n1 + n2
    resultado = int (resultado)
    print ("tu resultado es : ",resultado)
if operacion == 2 :
    print ("perfecto elejiste una resta, introduce el primer numero")
    n1 = int (input ())
    print ("introduce el segundo numero")
    n2 = int (input())
    resultado = n1 - n2
    resultado = int (resultado)
    print ("tu resultado es : ",resultado)
if operacion == 3 :
    print ("perfecto elejiste una multiplicacion, introduce el primer numero")
    n1 = int (input ())
    print ("introduce el segundo numero")
    n2 = int (input())
    resultado = n1 * n2
    resultado = int (resultado)
    print ("tu resultado es : ",resultado)
if operacion == 4 :
    print ("perfecto elejiste una division, introduce el primer numero")
    n1 = int (input ())
    print ("introduce el segundo numero")
    n2 = int (input())
    resultado = n1 / n2
    resultado = float (resultado)
    print ("tu resultado es : ",resultado)
print ("gracias por utilizar bnuestro programa, estamos mejorando para ti")
exit ()
