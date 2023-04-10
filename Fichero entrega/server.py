import glob
import sys
from calculadora import Calculadora
# from calculadora . ttypes import Operation
# Lo de ttypes es si hubieramos anadido tipos en el fichero . thrift

# hay que instalar antes el paquete thrift de python
#( no confundir con el compilador thrift )
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging
logging . basicConfig ( level = logging . DEBUG )
# Esto es para imprimir cuando haya errores en el
# servidor y poder depurar !

class CalculadoraHandler :
    def __init__ ( self ):
        self.log = {}
    def ping ( self ):
        print (" Me han hecho ping () ")
    def suma ( self , n1 , n2 ):
        print (" sumando "+str ( n1 )+ " con "+ str ( n2 ))
        return n1 + n2
    def resta ( self , n1 , n2 ):
        print (" restando "+ str ( n1 )+ " con "+ str( n2 ))
        return n1 - n2
    def multiplicacion ( self , n1 , n2 ):
        print (" multiplicando "+ str ( n1 )+ " con "+ str( n2 ))
        return n1 * n2
    def division ( self , n1 , n2 ):
        print (" dividiendo "+ str ( n1 )+ " con "+ str( n2 ))
        return n1 / n2
    
    #Definicion de calculadora vector

    def sumaV ( self, v1 , v2 ):
        resul=[v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2]]
        return resul
    def restaV ( self, v1 , v2 ):
        resul=[v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2]]
        return resul
    def multiplicacionV ( self, v1 , v2 ):
        a=v1[1]*v2[2]-v1[2]*v2[1]
        b=-v1[0]*v2[2]-v1[2]*v2[0]
        c=v1[0]*v2[1]-v1[1]*v2[0]
        resul=[a,b,c]
        return resul
    
    #Definicion de calculadora matrices

    def sumaM ( self, m1 , m2 ):
        resul=[
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        for i in range(3):
            for j in range(3):
                resul[i][j]=m1[i][j]+m2[i][j]

        return resul
    def restaM ( self, m1 , m2 ):
        resul=[
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        for i in range(3):
            for j in range(3):
                resul[i][j]=m1[i][j]-m2[i][j]

        return resul
    def multiplicacionM ( self, m1 , m2 ):
        resul=[
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    resul[i][j]+=m1[i][k]*m2[k][j]

        return resul

if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = Calculadora.Processor ( handler )
    transport = TSocket.TServerSocket ( host ="127.0.0.1", port =9090)
    tfactory = TTransport.TBufferedTransportFactory ()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory ()
    server = TServer.TSimpleServer ( processor,transport,tfactory,pfactory )
    print (" Iniciando servidor ... ")
    server.serve()
    print (" done . ")