service Calculadora{
    void ping () ,
    double suma (1: double num1 , 2: double num2 ) ,
    double resta (1: double num1 , 2: double num2 ) ,
    double multiplicacion(1: double num1 , 2: double num2 ) ,
    double division(1: double num1 , 2: double num2 ),

    list<double> sumaV(1: list<double> v1 , 2: list<double> v2 ),
    list<double> restaV(1: list<double> v1 , 2: list<double> v2 ),
    list<double> multiplicacionV(1: list<double> v1 , 2: list<double> v2 )
}