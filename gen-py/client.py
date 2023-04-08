from calculadora import Calculadora
from thrift import Thrift
from thrift . transport import TSocket
from thrift . transport import TTransport
from thrift . protocol import TBinaryProtocol

transport = TSocket . TSocket ( "localhost" , 9090)
transport = TTransport . TBufferedTransport ( transport )
protocol = TBinaryProtocol . TBinaryProtocol ( transport )# creamos el cliente
client = Calculadora . Client ( protocol )

transport.open ()
print (" Hacemos ping al server ")
client.ping ()

modo=input("Con que datos piensa operar? Numeros normales : 0 | Vectores : 1 | Matrices : 2  --> ")
if modo!='0' and modo!='1' and modo!='2' :
    raise ValueError("Tipo desconocido")

modo=int(modo)

if modo==0 :
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

transport . close ()