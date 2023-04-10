from calculadora import Calculadora
from thrift import Thrift
from thrift . transport import TSocket
from thrift . transport import TTransport
from thrift . protocol import TBinaryProtocol

transport = TSocket . TSocket ( "localhost" , 9090)
transport = TTransport . TBufferedTransport ( transport )
protocol = TBinaryProtocol . TBinaryProtocol ( transport )# creamos el cliente
client = Calculadora . Client ( protocol )

#Obtiene un vector de floats de una cadena

def toVector(cadena):
        aux=cadena.find(',')
        n1=float(cadena[0:aux])

        cadena=cadena[aux+1:]

        aux=cadena.find(',')
        n2=float(cadena[0:aux])

        cadena=cadena[aux+1:]

        n3=float(cadena)

        resul=[n1,n2,n3]

        return resul

#Imprime un vector por pantalla

def printVec(vector):
    print(f"{vector[0]} {vector[1]} {vector[2]}")

transport.open ()
print (" Hacemos ping al server ")
client.ping ()

modo=input("Con que datos piensa operar? Numeros normales : 0 | Vectores : 1 | Matrices : 2  --> ")
if modo!='0' and modo!='1' and modo!='2' :
    raise ValueError("Tipo desconocido")

modo=int(modo)

if modo==0 : #Operaciones Basicas
    print("Que operacion desea realizar? + - x /")
    signo=input()

    if signo!='+' and signo!='-' and signo!='x' and signo!='/':
        raise ValueError("Signo incorrecto")

    print("Con que digitos quieres operar?")
    num1=input("numero 1: ")
    num2=input("numero 2: ")

    num1=float(num1)
    num2=float(num2)

    if signo=='+':
        resultado=client.suma(num1,num2)
    elif signo=='-':
        resultado=client.resta(num1,num2)
    elif signo=='x':
        resultado=client.multiplicacion(num1,num2)
    else:
        if num2==0:
            raise ValueError("No se puede dividir por 0")
        else:
            resultado=client.division(num1,num2)

    print(f"{num1}{signo}{num2} = {resultado}")

elif modo==1 : #Vectores
    print("Que operacion desea realizar? + - x")
    signo=input()

    if signo!='+' and signo!='-' and signo!='x':
        raise ValueError("Signo incorrecto")

    print("Con que vectores quieres operar? Inserte los numeros seguidos separados por comas sin espacios")
    chain=input("Tamaño requerido de 3 --> ")

    v1=toVector(chain)

    chain=input("Tamaño requerido de 3 --> ")

    v2=toVector(chain)

    if signo=='+':
        resultado=client.sumaV(v1,v2)
    elif signo=='-':
        resultado=client.restaV(v1,v2)
    else:
        resultado=client.multiplicacionV(v1,v2)

    printVec(v1)
    print(signo)
    printVec(v2)
    print("------- RESULTADO -------")
    printVec(resultado)

else: #Matrices
    print("Que operacion desea realizar? + - x")
    signo=input()

    if signo!='+' and signo!='-' and signo!='x':
        raise ValueError("Signo incorrecto")
    
    print("Con que matrices quieres operar? Inserte los numeros por filas seguidos separados por comas sin espacios")
    cadena1=input("Primera fila : ")
    cadena2=input("Segunda fila : ")
    cadena3=input("Tercera fila : ")

    m1=[toVector(cadena1),toVector(cadena2),toVector(cadena3)]

    print("----- Segunda matriz ----")

    cadena1=input("Primera fila : ")
    cadena2=input("Segunda fila : ")
    cadena3=input("Tercera fila : ")

    m2=[toVector(cadena1),toVector(cadena2),toVector(cadena3)]

    if signo=='+':
        resultado=client.sumaM(m1,m2)
    elif signo=='-':
        resultado=client.restaM(m1,m2)
    else:
        resultado=client.multiplicacionM(m1,m2)

    for f in m1:
        printVec(f)

    print(signo)

    for f in m2:
        printVec(f)

    print("------- RESULTADO -------")
    
    for f in resultado:
        printVec(f)

transport . close ()